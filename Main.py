import os
import traceback
from datetime import datetime
import logging

# Setup logging
def setup_logging():
    """
    Permet de setup pour la première fois le logger, en créant le dossier logs si il n'existe pas, ou le vide si déjà
    présent

    :return: Le logger utiliser dans la suite du programme
    """
    logs_dir = 'logs'

    try:
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
            print(f"Created logs directory at: {os.path.abspath(logs_dir)}")
        else:
            for file in os.listdir(logs_dir):
                file_path = os.path.join(logs_dir, file)
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                    print(f"Deleted file: {file_path}")
    except Exception as e:
        print(f"Error setting up logs directory: {e}")

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Configuration de la console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)

    # Configuration du logger en mode fichier
    file_handler = logging.FileHandler(os.path.join(logs_dir, 'main.log'), mode='w')
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Initial setup
logger = setup_logging()

# Now import the other modules after setting up logging
# Importing functions from the provided scripts
import Starter
import XML_traitement
import Chart_maker
import Markdown_Rapport_Maker
import PDF_Rapport_Maker
from art import *
from colorama import Fore, Style
from rich.progress import Progress
from rich.console import Console
import argparse
import stat

# Clear the console
os.system('clear')

print(f"""{Fore.RED}
                                ░░░░░░░░░░░░░░░░░
                                ░░░▄░▀▄░░░▄▀░▄░░░
                                ░░░█▄███████▄█░░░
                                ░░░███▄███▄███░░░
                                ░░░▀█████████▀░░░
                                ░░░░▄▀░░░░░▀▄░░░░
    ██████╗░███████╗███╗░░██╗███████╗██╗░░██╗███████╗███████╗██╗░░██╗███████╗██████╗░
    ██╔══██╗██╔════╝████╗░██║██╔════╝██║░░██║██╔════╝██╔════╝██║░██╔╝██╔════╝██╔══██╗
    ██████╔╝█████╗░░██╔██╗██║██║░░░░░███████║█████╗░░██║░░░░░█████═╝░█████╗░░██████╔╝
    ██╔═══╝░██╔══╝░░██║╚████║██║░░░░░██╔══██║██╔══╝░░██║░░░░░██╔═██╗░██╔══╝░░██╔══██╗
    ██║░░░░░███████╗██║░╚███║███████╗██║░░██║███████╗███████╗██║░╚██╗███████╗██║░░██║
    ╚═╝░░░░░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

                                                    [●] Version: 1.6.9
                                                    [●] @Zerxeas | @Dijiox | @IAgonYI\n    

{Style.RESET_ALL}""")

def set_permissions_777(path):
    """
    Change les permissions des dossiers/fichiers en 777 récursivement du chemin donné en input

    :param path: Chemin a partir duquel changer récursivement les droits des dossiers/fichiers
    :type path: str

    :return: Return rien, changes juste les permissions
    """
    try:
        for root, dirs, files in os.walk(path):
            for dir in dirs:
                os.chmod(os.path.join(root, dir), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
            for file in files:
                os.chmod(os.path.join(root, file), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
        os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
        logger.info(f"Set permissions to 777 for {path}")
    except Exception as e:
        logger.info(f"Error setting permissions for {path}: {e}")

def get_ip_from_xml(xml_file):
    """
    Fonction qui permet de retrouver l'adresse IP de la machine concernée par le fichier xml donné en input

    :param xml_file: Fichier .xml donné en input qui contient dans son nom l'adresse IP de la machine concernée
    :type xml_file: str

    :return: L'adresse IP de la machine concernée
    """
    try:
        ip_tmp = (xml_file.split("_")[2]).split(".")[:4]
        ip = ip_tmp[0] + "." + ip_tmp[1] + "." + ip_tmp[2] + "." + ip_tmp[3]
        return ip
    except Exception as e:
        logger.error(f"Error extracting IP from XML file {xml_file}: {e}")
        return None

def create_directory_structure(ip):
    """
    Fonction qui sert a créer l'arborescence pour stocker les différents fichiers temporaires avant l'édition du rapport
    final
    La structure aura la forme :
    -- Rapport_Tmp/
            |---------- 192.168.20.2/
            |---------- 192.168.20.3/
            |---------- 192.168.20.4/
            |---------- ...

    :param ip:
    :return:
    """
    try:
        base_dir = os.path.join('Rapport_Tmp', ip)
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        return base_dir
    except Exception as e:
        logger.error(f"Error creating directory structure for IP {ip}: {e}")
        return None

def main():
    """
    Fonction principale qui orchestre les différents sous programme du projet. Pour plus de détails, vous pouvez
    consulter les différents codes séparemment, avec leur docstrings en commentaire.

    :return: Rien, à la fin de l'exécution, les rapports sont disponible dans la même arborescence que le projet.
    """
    try:
        parser = argparse.ArgumentParser(description="Entrez l'interface à partir de laquelle lancer le scan")
        parser.add_argument("--interface", type=str, default="eth0", help="Nom de l'interface réseau (par défaut : eth0)")
        args = parser.parse_args()
        interface = args.interface

        today = datetime.today().strftime('%Y-%m-%d')
        xml_dir = f'xml_result_{today}'
        rapport_dir = 'Rapport_Tmp'

        CVEs_ordered_machines = []

        if not os.path.exists(rapport_dir):
            os.makedirs(rapport_dir)

        hosts = Starter.main(interface)
        logger.info(f"Rappel de la liste des machines qui vont être auditées : {hosts}")

        with Progress() as progress:
            console = Console()
            console.rule("\n[bold cyan]Traitement des données[/bold cyan]\n")
            task = progress.add_task("[cyan]Post traitement :", total=len(os.listdir(xml_dir)))

            #Début du parcours récursif des fichiers .xml dans le dossier xml_result_{today}
            for filename in os.listdir(xml_dir):
                try:
                    xml_tmp = filename
                    xml_file = os.path.join(xml_dir, filename)

                    # Récupération de l'IP par fichier .xml
                    ip = get_ip_from_xml(xml_tmp)
                    if ip is None:
                        continue

                    # Création de l'architecture de dossier temporaire
                    ip_dir = create_directory_structure(ip)
                    if ip_dir is None:
                        continue

                    # Lancement successif des différentes fonctions dans l'ordre approprié & récupération du nombre de CVEs
                    cve_count = XML_traitement.main(xml_file, ip_dir)
                    machine_infos_tmp = [ip, int(cve_count)]
                    CVEs_ordered_machines.append(machine_infos_tmp)

                    today = datetime.today().strftime('%Y-%m-%d')
                    md_name = f"resultat_scan_penchecker_{today}.md"
                    md_file = os.path.join(ip_dir, md_name)

                    logger.info(f"Résultats sauvegardés dans {md_file}")

                    img_path_output = os.path.join('Rapport_Tmp', ip)
                    try:
                        Chart_maker.main(md_file, img_path_output)
                    except Exception as e:
                        logger.info(f"Aucun graphique à faire pour : {md_file} - {e}")
                        continue

                    progress.update(task, advance=1)
                except Exception as e:
                    logger.error(f"Error processing file {filename}: {e}")
                    continue
        #Création des rapports finaux en markdown / PDF
        Markdown_Rapport_Maker.main(hosts, CVEs_ordered_machines)
        PDF_Rapport_Maker.main(f'./Rapport_Final_{today}.md')
        set_permissions_777('./')
    except Exception as e:
        logger.error(f"Exception in main: {e}")
        raise

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.critical(f"Critical error in main execution: {e}")
