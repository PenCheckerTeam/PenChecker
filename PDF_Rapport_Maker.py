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
    console = Console()
    panel = Panel(text, title="Infos", style="bold white",
                  border_style="bright_white", expand=False)
    console.print(panel)

def main(MdFile_path):
    subprocess.run(['gh-md-to-html', MdFile_path, '-p', output_filename, '-o', 'OFFLINE'])
    rapport_html = "Rapport_Final_"+date_du_jour+".html"
    subprocess.run(['rm', '-f', rapport_html])
    text=f"\nLe rapport final pdf a été créé : {output_filename}"
    messenger(text)

if __name__ == "__main__":
    main()
