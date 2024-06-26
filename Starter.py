import subprocess
import os
import datetime
import re
import ipaddress
from rich.progress import Progress
from rich.console import Console
from rich.panel import Panel
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
file_handler = logging.FileHandler('./logs/starter.log', mode='w')
file_handler.setLevel(logging.DEBUG)
file_formatter =logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

def messenger(text):
    console = Console()
    console.rule("[bold red]Initialisation du programme[/bold red]")
    panel = Panel(text, title="Infos", style="bold white",
                  border_style="bright_white", expand=False)
    console.print(panel)
# Get the actual IP address of the specified network interface
def get_interface_ip(interface_name):
    result = subprocess.run(['ip', 'a', 'show', interface_name], capture_output=True, text=True)
    if result.returncode != 0:
        return None

    ip_match = re.search(r'inet (\d+\.\d+\.\d+\.\d+)/(\d+)', result.stdout)
    if ip_match:
        ip_address = ip_match.group(1)
        subnet_mask = ip_match.group(2)
        logger.info(f"Configuration réseau récupérée : @ip = {ip_address} | subnet mask = {subnet_mask}")
        return ip_address, subnet_mask
    return None, None

def get_network_address(ip_address, subnet_mask):
    # Créer un objet IPv4Network à partir de l'adresse IP et du masque de sous-réseau
    network = ipaddress.IPv4Network(f"{ip_address}/{subnet_mask}", strict=False)
    # Retourner l'adresse réseau
    logger.info(f"Adresse du réseau sur lequel est branché le programme : {network}")
    return str(network.network_address)
    
def validate_and_clean_ip(host_ip):
    pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    match = re.search(pattern, host_ip)
    
    if match:
        # Extract the valid IP address
        valid_ip = match.group(0)
        return valid_ip
    else:
        return None

def detect_hosts(ip_address, subnet_mask):
    ip_range = get_network_address(ip_address, subnet_mask) + '/' + subnet_mask
    fping_result = subprocess.run(['fping', '-c 1', '-g', ip_range], capture_output=True)
    result = subprocess.run(['ip', '-4', 'neigh'], capture_output=True, text=True)
    hosts = []
    for extract in result.stdout.split('\n'):
        if 'lladdr' in extract:
            parts = extract.split()
            if parts:
                host_ip = parts[0]
                hosts.append(validate_and_clean_ip(host_ip))
    return hosts

# Create a directory to store XML results
def create_result_directory():
    today = datetime.date.today().strftime("%Y-%m-%d")
    directory_name = f"xml_result_{today}"
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    return directory_name

# Scan each detected host for vulnerabilities
def scan_hosts_for_vulns(hosts, result_directory):
    console = Console()
    console.rule("[bold green]Scan des machines[/bold green]\n")
    with Progress() as progress:
        task = progress.add_task("[green]Scan des machines :", total=len(hosts))
        print("\n")
        for host in hosts:
            result_file = os.path.join(result_directory, f"result_nmap_{host}.xml")
            subprocess.run(['nmap', '-PN', '-sS', '-A', '--script', 'vulners', '--script-args', 'mincvss=5.0', host, '-oX', result_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            progress.update(task, advance=1)
def main(interface):
    interface_name = interface
    ip_address, netmask = get_interface_ip(interface_name)
    if ip_address is None:
        logger.error(f"Could not find IP address for interface {interface_name}.")
        return

    hosts = detect_hosts(ip_address, netmask)

    text=f"""
Adresse IP hôte sur {interface_name} : {ip_address}/{netmask}\n
Nombre de machines a scanner : {len(hosts)}\n
Détail : {hosts}
"""
    messenger(text)

    if not hosts:
        logger.error(f"No hosts detected, see the output of hosts variable here : {hosts}")
        return
    result_directory = create_result_directory()
    scan_hosts_for_vulns(hosts, result_directory)
    logger.info(f"Scanning completed. Results are saved in {result_directory}") #debug line
    return hosts
if __name__ == "__main__":
    main()
