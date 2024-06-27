import subprocess
import os
import datetime
import re
import ipaddress
from rich.progress import Progress
from rich.console import Console
from rich.panel import Panel
import logging

# Configuration du logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Configuration de la console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

# Configuration du logger en mode fichier
file_handler = logging.FileHandler('./logs/starter.log', mode='w')
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

def messenger(text):
    """
    Fonction qui permet de formatter le texte en input dans un cadre nommé "info" pour l'afficher dans le terminal

    :param text: Le texte a mettre en forme
    :type text: str

    :return: Affiche le cadre avec le texte formatté à l'intérieur
    """
    console = Console()
    console.rule("[bold red]Initialisation du programme[/bold red]")
    panel = Panel(text, title="Infos", style="bold white", border_style="bright_white", expand=False)
    console.print(panel)

def get_interface_ip(interface_name):
    """
    Fonction qui récupères le couple adresse IP / Masque de sous réseau, de l'interface selectionnée au lancement du
    programme (eth0 par défaut)

    :param interface_name: Nom de l'interface sur laquelle récupérée les infos réseau
    :type interface_name: str

    :return: Le couple de valeur dans deux variables distinctes IP / Masque
    """
    try:
        result = subprocess.run(['ip', 'a', 'show', interface_name], capture_output=True, text=True)
        if result.returncode != 0:
            logger.error(f"Erreur lors de l'exécution de la commande IP pour l'interface {interface_name}")
            return None, None

        ip_match = re.search(r'inet (\d+\.\d+\.\d+\.\d+)/(\d+)', result.stdout)
        if ip_match:
            ip_address = ip_match.group(1)
            subnet_mask = ip_match.group(2)
            logger.info(f"Configuration réseau récupérée : @ip = {ip_address} | subnet mask = {subnet_mask}")
            return ip_address, subnet_mask
    except Exception as e:
        logger.error(f"Exception lors de la récupération de l'adresse IP de l'interface {interface_name}: {e}")
    return None, None

def get_network_address(ip_address, subnet_mask):
    """
    Calcul l'adresse du réseau sur lequel on va lancer le scan

    :param ip_address: Adresse IP récupérée par la fonction get_interface_ip()
    :param subnet_mask: Masque de sous réseau récupéré par la fonction get_interface_ip()
    :type ip_address: str
    :type subnet_mask: str

    :return: L'adresse réseau. Exemple : 192.168.20.58/24 devient 192.168.20.0/24
    """
    try:
        network = ipaddress.IPv4Network(f"{ip_address}/{subnet_mask}", strict=False)
        logger.info(f"Adresse du réseau sur lequel est branché le programme : {network}")
        return str(network.network_address)
    except Exception as e:
        logger.error(f"Exception lors de la détermination de l'adresse réseau: {e}")
        return None

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

def detect_hosts(ip_address, subnet_mask):
    """
    Fonction qui permet de faire une préanalyse rapide des hosts up et qui répondent sur le réseau. Pour se faire elle
    utilise dans un premier temps la fonction fping, puis récupères les résultats de la table ARP avec ip -4 neigh.

    :param ip_address: Adresse IP de l'interface définie au lancement du programme (eth0 par défaut)
    :param subnet_mask: Masque de sous réseau de l'interface définie au lancement du programme (eth0 par défaut)
    :type ip_address: str
    :type subnet_mask: str

    :return: Une liste contenant toutes les adresses IPs du réseau qui sont joignables
    """
    try:
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
    except Exception as e:
        logger.error(f"Exception lors de la détection des hôtes: {e}")
        return []

def create_result_directory():
    """
    Fonction qui crée le dossier nommé xml_result_"date_du_jour", dans lequel vont être stockés les résultats nmap
    en .xml par machine scannée

    :return: Retourne le nom du dossier créé pour la suite du programme
    """
    try:
        today = datetime.date.today().strftime("%Y-%m-%d")
        directory_name = f"xml_result_{today}"
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
        return directory_name
    except Exception as e:
        logger.error(f"Exception lors de la création du répertoire de résultats: {e}")
        return None

def scan_hosts_for_vulns(hosts, result_directory):
    """
    Fonction principale de ce programme qui lance les scans de services avec remontées de vulnérabilités sur les
    hosts trouvés par la fonction detect_hosts()

    :param hosts: Listes des machines qui sont joignables, obtenue par detect_hosts()
    :param result_directory: Nom du repertoire où stocké les fichiers .xml de résultats, obtenu par
    create_result_directory()
    :type hosts: list
    :type result_directory: str

    :return: La fonction en elle même ne return rien, mais enregistre les résultats des scans dans le dossier
    "result_directory". Ces fichiers se nomment selon la convention : result_nmap_@ip.xml
    """
    console = Console()
    console.rule("[bold green]Scan des machines[/bold green]\n")
    with Progress() as progress:
        task = progress.add_task("[green]Scan des machines :", total=len(hosts))
        for host in hosts:
            try:
                result_file = os.path.join(result_directory, f"result_nmap_{host}.xml")
                subprocess.run(['nmap', '-PN', '-sS', '-A', '--script', 'vulners', '--script-args', 'mincvss=5.0', host, '-oX', result_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                progress.update(task, advance=1)
            except Exception as e:
                logger.error(f"Exception lors du scan de l'hôte {host}: {e}")

def main(interface):
    """
    Fonction main du programme. C'est elle qui orchestre les différentes fonctions définies ci-dessus.

    :param interface: Entrée utilisateur avec l'option au démarrage "--interface", sinon eth0 par défaut
    :type interface: str

    :return: La liste "hosts" contenant les machines joignables car utilisé dans le programme Main.py
    """
    try:
        interface_name = interface
        ip_address, netmask = get_interface_ip(interface_name)
        if ip_address is None:
            logger.error(f"Impossible de trouver l'adresse IP pour l'interface {interface_name}.")
            return

        hosts = detect_hosts(ip_address, netmask)

        text = f"""
Adresse IP hôte sur {interface_name} : {ip_address}/{netmask}\n
Nombre de machines à scanner : {len(hosts)}\n
Détail : {hosts}
"""
        messenger(text)

        if not hosts:
            logger.error(f"Aucun hôte détecté, voir la sortie de la variable hosts : {hosts}")
            return

        result_directory = create_result_directory()
        if result_directory is None:
            logger.error("Impossible de créer le répertoire de résultats.")
            return

        scan_hosts_for_vulns(hosts, result_directory)
        logger.info(f"Scanning completed. Results are saved in {result_directory}")

        return hosts

    except Exception as e:
        logger.error(f"Exception dans la fonction principale: {e}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.critical(f"Erreur critique dans le programme principal: {e}")
