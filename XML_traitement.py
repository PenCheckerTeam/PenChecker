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
console_handler.setLevel(logging.CRITICAL)
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

# configuration du logger en mode fichier
file_handler = logging.FileHandler('./logs/XMLtraitement.log', mode='w')
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

def store_file_in_directory(filename, ip_dir):
    """
    Fonction qui permet de déplacer un ficher "filename" vers le dossier donné en argument "ip_dir"

    :param filename: Fichier que l'on souhaite déplacer
    :param ip_dir: Dossier dans lequel on veut déplacer le fichier
    :type filename: str
    :type ip_dir: str

    :return: Rien, la fonction déplace juste le fichier
    """
    try:
        # Vérifie si le dossier existe, sinon le crée
        if not os.path.exists(ip_dir):
            os.makedirs(ip_dir)

        # Chemin complet pour la source et la destination
        src_file_path = os.path.join(os.getcwd(), filename)
        dest_file_path = os.path.join(ip_dir, filename)

        # Déplacement du fichier vers le dossier de destination
        if os.path.exists(src_file_path):
            shutil.move(src_file_path, dest_file_path)
            logger.info(f"Moved {filename} to {ip_dir}")
        else:
            logger.error(f"File {filename} does not exist in the current directory")
    except Exception as e:
        logger.error(f"Exception in store_file_in_directory: {e}")

def validate_and_clean_ip(host_ip):
    """
    Fonction qui permet de traiter les adresses IP pour être sûr d'obtenir une adresse de la forme xxx.xxx.xxx.xxx
    et ne pas avoir d'erreur du à la présence d'un caractère en trop

    :param host_ip: IP a vérifier par la fonction
    :type host_ip: str

    :return: Renvoie l'adresse IP au bon format pour la réutiliser
    """
    try:
        pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
        match = re.search(pattern, host_ip)
        if match:
            valid_ip = match.group(0)
            return valid_ip
    except Exception as e:
        logger.error(f"Exception lors de la validation de l'IP: {e}")
    return None

def xml_proccessing(xml_file, ip_dir):
    """
    Grosse fonction qui est appelée successivement par Main.py pour chaque fichier xml dans le dossier xml_result_{today}
    Le but de la fonction est de parser le fichier xml afin d'en extraire toutes les infos : (OS / IP / Services & Versions
    / CVEs). Puis d'écrire tout ça dans un pré rapport qui sera édité par la suite.

    :param xml_file: Fichier xml que la fonction doit parser, input via la boucle dans Main.py
    :param ip_dir: Dossier de destination, nommer par l'IP dans le nom du fichier xml, dans lequel va être stocké le
    fichier .md temporaire
    :type xml_file: str
    :type ip_dir: str

    :return: le compte total des CVEs de la machine et la fonction enregistre juste le résultat dans un fichier markdown.
    """

    try:
        # Parsing du fichier xml
        tree = ET.parse(xml_file)
        root = tree.getroot()
    except ET.ParseError as e:
        logger.error(f"Failed to parse XML file {xml_file}: {e}")
        return
    except Exception as e:
        logger.error(f"Exception in parsing XML file {xml_file}: {e}")
        return

    try:
        # Extraction des adresses IP
        ip_address = root.find('host/address[@addrtype="ipv4"]').get('addr')
    except AttributeError as e:
        logger.error(f"Cannot find IP address in XML file {xml_file}: {e}, choosing directory name based on IP address")
        ip_address = validate_and_clean_ip(ip_dir)
    except Exception as e:
        logger.error(f"Exception in extracting IP address from {xml_file}: {e}")
        return

    try:
        # Extraction des informations d'OS
        os_info = root.find('.//osmatch')
        os_name = os_info.get('name') if os_info is not None else "Unknown OS"
        os_accuracy = os_info.get('accuracy') if os_info is not None else "Unknown Accuracy"
        os_version = f"{os_name} (Accuracy: {os_accuracy}%)"
    except Exception as e:
        logger.error(f"Exception in extracting OS information from {xml_file}: {e}")
        os_version = "Unknown OS (Unknown Accuracy%)"

    try:
        # Extraction des ports et services
        ports_services = []
        cves = {}
        cve_count_tot = 0

        for port in root.findall('host/ports/port'):
            portid = port.get('portid')
            service = port.find('service')
            service_name = service.get('name')
            product = service.get('product', '')
            version = service.get('version', '')
            if version:
                version = f"version={version}"

            # Extraction des CVEs associées aux ports
            script = port.find(".//script[@id='vulners']")
            cve_list = []
            if script is not None:
                # Parsing des informations concernant les CVEs / on enlève les lignes *EXPLOIT* trop de faux positifs
                # / liens morts
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
                                logger.info(f"Found CVE: {cve_id} with CVSS score: {cvss_score} for port: {portid}")
                            except ValueError as e:
                                logger.warning(f"Invalid CVSS score in line: {line}. Error: {e}")
                                continue
            cves[portid] = cve_list

            # Compte des CVEs par services pour les premières lignes du rapport qui donnes le nombres de CVE par services
            cve_count = len(cve_list)
            cve_count_tot += cve_count
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
    except Exception as e:
        logger.error(f"Exception in extracting ports and services from {xml_file}: {e}")
        return

    try:
        # Génération du fichier markdown
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
        logger.info(f"Markdown file {filename} generated successfully.")
    except Exception as e:
        logger.error(f"Exception in generating markdown file {filename}: {e}")

    return cve_count_tot

def main(file_path, ip_dir):
    try:
        cve_count = xml_proccessing(file_path, ip_dir)
        return cve_count
    except Exception as e:
        logger.error(f"Exception in main: {e}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.critical(f"Critical error in main execution: {e}")
