import xml.etree.ElementTree as ET
import os
import datetime
import shutil
import logging

# configuration du logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# configuration de la console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)
console_formatter =logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

# configuration du logger en mode fichier
file_handler = logging.FileHandler('./logs/XMLtraitement.log', mode='w')
file_handler.setLevel(logging.DEBUG)
file_formatter =logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

def store_file_in_directory(filename, ip_dir):
    # Ensure the target directory exists
    if not os.path.exists(ip_dir):
        os.makedirs(ip_dir)

    # Construct the full path for the source and destination
    src_file_path = os.path.join(os.getcwd(), filename)
    dest_file_path = os.path.join(ip_dir, filename)

    # Move the file
    if os.path.exists(src_file_path):
        shutil.move(src_file_path, dest_file_path)
        logger.info(f"Moved {filename} to {ip_dir}") #debug line
    else:
        logger.error(f"File {filename} does not exist in the current directory")
def xml_proccessing(xml_file, ip_dir):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Extract IP address
    try:
        ip_address = root.find('host/address[@addrtype="ipv4"]').get('addr')
    except:
        logger.error("Can't check host directory " + ip_dir)
        return

    # Extract OS information
    os_info = root.find('.//osmatch')
    os_name = os_info.get('name') if os_info is not None else "Unknown OS"
    os_accuracy = os_info.get('accuracy') if os_info is not None else "Unknown Accuracy"
    os_version = f"{os_name} (Accuracy: {os_accuracy}%)"

    # Extract ports and services
    ports_services = []
    cves = {}

    for port in root.findall('host/ports/port'):
        portid = port.get('portid')
        service = port.find('service')
        service_name = service.get('name')
        product = service.get('product', '')
        version = service.get('version', '')
        if version:
            version = f"version={version}"

        # Extract CVEs associated with this port
        script = port.find(".//script[@id='vulners']")
        cve_list = []
        if script is not None:
            # Parse the script output directly for CVEs
            output = script.get('output')
            if output:
                lines = output.split('\n')
                for line in lines:
                    if '*EXPLOIT*' in line:
                        continue
                    parts = line.split()
                    if len(parts) >= 3:
                        try:
                            cvss_score = float(parts[1])
                            cve_id = parts[0]
                            cve_list.append((cvss_score, cve_id))
                            logger.info(f"Found CVE: {cve_id} with CVSS score: {cvss_score} for port: {portid}")  # Debug line
                        except ValueError:
                            logger.info(f"{ValueError}")
                            continue
        cves[portid] = cve_list

        # Correctly count the CVEs and append service information
        cve_count = len(cve_list)
        service_info = f"{service_name} {product} {version}".strip()

        if cve_count == 0:
            colored_info = f"<span style='color:green;'>{portid}: {service_info} (CVE Count: {cve_count})</span>"
        elif cve_count < 10:
            colored_info = f"<span style='color:orange;'>{portid}: {service_info} (CVE Count: {cve_count})</span>"
        else:
            colored_info = f"<span style='color:red;'>{portid}: {service_info} (CVE Count: {cve_count})</span>"

        if cve_count > 0 and cve_count < 10:
            colored_info = f"**{colored_info}**"
        elif cve_count >= 10:
            colored_info = f"**{colored_info}**"

        ports_services.append((portid, colored_info, service_info))

    # Generate the markdown file
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    filename = f"resultat_scan_penchecker_{today}.md"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# Scan Results for IP: {ip_address} (OS: {os_version})\n\n")
        f.write(
            "Voici la liste des services fonctionnant sur les différents ports accessibles de la machine, **si les champs sont vides**, c'est que le scans n'a rien détecté sur la machine. **Le nombre de CVEs** par service est indiqué entre parenthèse. Si le nombre de CVE est de 0, **nous vous recommandons de vérifier**, si elle est identifiée, **que la version du service est à jour**\n\n")
        f.write("## Ports and Services\n")
        for _, entry, _ in ports_services:
            f.write(f"- {entry}\n")

        f.write("\n## CVEs\n")
        for port, cve_list in cves.items():
            if cve_list:
                service_info = next((si for pid, _, si in ports_services if pid == port), None)
                f.write(f"### Port {port} : {service_info}\n")
                for cvss_score, cve in cve_list:
                    if cvss_score > 8:
                        cve_color = 'red'
                    elif 6 <= cvss_score <= 8:
                        cve_color = 'orange'
                    else:
                        cve_color = 'green'
                    f.write(f"<span style='color:{cve_color};'>**{cvss_score}** | {cve}</span>\n\n")

    store_file_in_directory(filename, ip_dir)
    logger.info(f"Markdown file {filename} generated successfully.") #debug line

def main(file_path, ip_dir):
    xml_proccessing(file_path, ip_dir)

if __name__ == "__main__":
    main()
