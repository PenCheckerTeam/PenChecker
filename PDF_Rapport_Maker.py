import gh_md_to_html
import subprocess
import mistune
import pdfkit
import datetime
from rich.console import Console
from rich.panel import Panel

date_du_jour = datetime.datetime.now().strftime('%Y-%m-%d')
output_filename = "Rapport_Pdf_"+date_du_jour
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

def main(MdFile_path):
    """
    Fonction qui appelle les différentes bibliothèques et dépendances pour transformer le markdown en pdf

    :param MdFile_path: Chemin du fichier rapport en markdown
    :type MdFile_path: str

    :return: rien, enregistre le rapport final en PDF à la racine du programme
    """
    subprocess.run(['gh-md-to-html', MdFile_path, '-p', output_filename, '-o', 'OFFLINE'])
    rapport_html = "Rapport_Final_"+date_du_jour+".html"
    subprocess.run(['rm', '-f', rapport_html])
    text=f"\nLe rapport final pdf a été créé : {output_filename}"
    messenger(text)

if __name__ == "__main__":
    main()
