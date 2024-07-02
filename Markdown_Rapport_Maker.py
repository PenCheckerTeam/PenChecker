import os
from datetime import datetime
from rich.progress import Progress
from rich.console import Console
from rich.panel import Panel

def messenger(text):
    """
    Fonction qui sert à afficher le message donné en input dans un cadre en sortie terminal

    :param text: Texte à mettre en forme sur la sortie terminal
    :type text: str

    :return: rien, affiche juste le message
    """
    console = Console()
    panel = Panel(text, title="Infos", style="bold white",
                  border_style="bright_white", expand=False)
    console.print(panel)

def sorted_output(list):
    """
    Fonction de tri qui tri une liste composé de doublets, dans l'odre décroissants du deuxième éléments

    Exemple : [['adresse_ip_1', 57], ['adresse_ip_2', 34], ['adresse_ip_3', 78]]
    devient : [['adresse_ip_3', 78], ['adresse_ip_1', 57], ['adresse_ip_2', 34]]

    :param list: liste a trier.
    :type list: list

    :return: La liste triée
    """
    # Tri de la liste selon le deuxième élément de chaque sous-liste en ordre décroissant
    sorted_list = sorted(list, key=lambda x: x[1], reverse=True)
    return sorted_list

def concat_markdown_files(root_dir, hosts, CVEs_ordered_machines):
    """
    Fonction qui parcourt tous les dossiers dans "Rapport_Tmp/" et qui concatène les fichiers rapport en markdown de
    chacune des machines.

    :param root_dir: Dossier parent dans lequel parcourir les sous-dossiers pour trouver les rapports temporaires
    :param hosts: Liste des machines qui ont été scannées par l'outil
    :param CVEs_ordered_machines: Liste des machines triées selon leur ordre de CVEs
    :type root_dir: str
    :type hosts: list
    :type CVEs_ordered_machines: list

    :return: rien, enregistre à la racine du programme le fichier rapport markdown définitif
    """
    # Obtenir la date du jour au format YYYY-MM-DD
    date_du_jour = datetime.now().strftime('%Y-%m-%d')
    filename_pattern = f'resultat_scan_penchecker_{date_du_jour}_modified.md'
    filename_emptycve_pattern = f'resultat_scan_penchecker_{date_du_jour}.md'
    output_filename = f'Rapport_Final_{date_du_jour}.md'

    # Créer/vider le fichier de sortie
    with open(output_filename, 'w', encoding='utf-8') as outfile:
        outfile.write("# Voici le rapport final du scan effectué par PenChecker\n\n")
        outfile.write("Dans ce rapport vous retrouverez dans l'ordre des @IP les différents résultats\n")
        outfile.write("Voici le rapport final du scan effectué par PenChecker, le rapport est articulé ainsi : \n\n")
        outfile.write(""" 
- La machine concernée
  - Port and Services
    - Liste des différents ports/services accessibles avec numéros de versions
  - Répartition des CVEs en fonction des services
    - Représentation graphique camembert
  - Répartition des CVEs en fonction de leur score CVSS
    - Représentation graphique barre
  - CVEs
    - Listing de toutes les CVEs trouvées pour tous les ports/services\n\n
""")
        outfile.write("## Listing des machines\n")
        outfile.write("Voici la liste des adresses IP des machines détectées :\n\n")
        for host in hosts:
            outfile.write(f"- {host}\n")
        outfile.write("\n\n")

    # Parcourir les sous-dossiers de root_dir dans l'ordre donné par CVEs_ordered_machines
    for machine in CVEs_ordered_machines:
        ip_address = machine[0]
        machine_dir = os.path.join(root_dir, ip_address)
        if os.path.isdir(machine_dir):
            target_file = None
            for file in os.listdir(machine_dir):
                if file == filename_pattern:
                    target_file = filename_pattern
                    break
                elif file == filename_emptycve_pattern:
                    target_file = filename_emptycve_pattern

            if target_file:
                file_path = os.path.join(machine_dir, target_file)
                # Read the content of the file and add it to the output file
                with open(file_path, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    with open(output_filename, 'a', encoding='utf-8') as outfile:
                        outfile.write(content)
                        outfile.write("\n\n")

    text = f"\nLe rapport final en markdown a été créé : {output_filename}"
    messenger(text)

def main(hosts, CVEs_ordered_machines):
    CVEs_ordered = sorted_output(CVEs_ordered_machines)
    concat_markdown_files('./Rapport_Tmp/', hosts, CVEs_ordered)

if __name__ == "__main__":
    main()

