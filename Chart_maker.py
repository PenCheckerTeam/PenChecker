import re
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import Counter
import os
import logging

# Configuration du logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Configuration de la console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.CRITICAL)
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

# Configuration du logger en mode fichier
file_handler = logging.FileHandler('./logs/ChartMaker.log', mode='w')
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

def generate_cve_pie_chart(file_path, output_image_path):
    """
    Le but de la fonction est de générer, avec matplotlib.pyplot, un graphique camembert qui donne la répartition des
    CVEs par services. Ce qui permet de mieux identifier les services critiques sur une machines vulnérable

    :param file_path: Donné en input par le code de Main.py, fichier markdown contenu dans le dossier nommé avec l'@ip
    de la machine concernée
    :param output_image_path: Donné en input par le code de Main.py, chemin jusqu'au dossier en question.
    Exemple : ./Rapport_Tmp/192.168.30.15/
    :type file_path: str
    :type output_image_path: str

    :return: Le chemin de l'image. Exemple : ./Rapport_Tmp/192.168.30.15/pie_chart.png
    """
    try:
        # Lire le contenu du fichier markdown avec le bon encodage
        with open(file_path, 'r', encoding='utf-8') as file:
            md_content = file.read()

        # Modèle regex amélioré pour capturer toutes les entrées de port, service et nombre de CVE
        pattern = re.compile(r'(\d+): (.*?)(?: version=[\w.]+)? \(CVE Count: (\d+)\)')
        data = pattern.findall(md_content)

        # Convertir les données extraites en DataFrame
        df = pd.DataFrame(data, columns=['Port', 'Service', 'CVE_Count'])
        df['CVE_Count'] = df['CVE_Count'].astype(int)

        # Filtrer les entrées avec 0 CVEs
        df_filtered = df[df['CVE_Count'] > 0]

        # Vérifier s'il y a des CVEs après le filtrage
        if df_filtered.empty:
            logger.info(f"Aucune CVE trouvée pour {file_path}, le graphique ne sera pas créé.")
            return None

        # Résumer les noms de service de plus de 2-3 mots
        df_filtered['Service'] = df_filtered['Service'].apply(lambda x: ' '.join(x.split()[:3]))

        # Combiner le port et le nom du service pour les étiquettes
        df_filtered['Label'] = df_filtered.apply(lambda row: f"{row['Port']} | {row['Service']}", axis=1)

        # Grouper par la nouvelle étiquette et sommer les comptes CVE
        df_grouped = df_filtered.groupby('Label').sum().reset_index()

        # Créer un graphique en camembert
        plt.figure(figsize=(10, 7))
        plt.pie(df_grouped['CVE_Count'], labels=df_grouped['Label'], autopct='%1.1f%%', startangle=140)
        plt.title('Distribution of CVE Counts by Service')

        # Enregistrer le graphique en tant qu'image (utiliser explicitement le format png)
        final_path = os.path.join(output_image_path, 'pie_chart.png')
        plt.savefig(final_path, format='png')
        plt.close()

        logger.info(f"Pie chart saved as {final_path}")
        return final_path
    except Exception as e:
        logger.error(f"Exception in generate_cve_pie_chart: {e}")
        return None

def create_cve_count_by_cvss_chart(md_file_path, output_image_path):
    """
    Le but de la fonction est de générer, avec matplotlib.pyplot, un graphique bar qui donne le nombre de CVE par score
    CVSSv3 arrondi à l'unité (uniquement si supérieur ou égal à 6. Ce qui permet de mieux identifier les machines avec
    beaucoup de CVE catégorisées avec un haut score CVSSv3

    :param md_file_path: Donné en input par le code de Main.py, fichier markdown contenu dans le dossier nommé avec l'@ip
    de la machine concernée
    :param output_image_path: Donné en input par le code de Main.py, chemin jusqu'au dossier en question.
    Exemple : ./Rapport_Tmp/192.168.30.15/
    :type md_file_path: str
    :type output_image_path: str

    :return: Le chemin de l'image. Exemple : ./Rapport_Tmp/192.168.30.15/cve_count_by_cvss_chart.png
    """
    try:
        # Lire le fichier markdown avec le bon encodage
        with open(md_file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Modèle regex amélioré pour extraire les scores CVSS
        cvss_scores = re.findall(r"\*\*(\d+\.\d+)\*\*", content)
        if not cvss_scores:
            logger.info(f"No CVSS scores found in {md_file_path}.")
            return None

        # Convertir les scores CVSS en flottants
        cvss_scores = [round(float(score)) for score in cvss_scores if round(float(score)) > 5]

        # Compter les occurrences de chaque score CVSS
        cvss_count = Counter(cvss_scores)

        # Créer un DataFrame pour les comptes de scores CVSS
        df_cvss = pd.DataFrame(cvss_count.items(), columns=['CVSS_Score', 'Count'])
        df_cvss = df_cvss.sort_values(by='CVSS_Score')

        # Créer un graphique en barres pour les comptes CVE par score CVSS
        plt.figure(figsize=(12, 6))
        plt.bar(df_cvss['CVSS_Score'].astype(str), df_cvss['Count'], color='skyblue')
        plt.xlabel('CVSS Score')
        plt.ylabel('CVE Count')
        plt.title('CVE Count by CVSS Score')

        # Enregistrer le graphique en tant qu'image (utiliser explicitement le format png)
        final_path = os.path.join(output_image_path, 'cve_count_by_cvss_chart.png')
        plt.savefig(final_path, format='png')
        plt.close()

        logger.info(f"Bar chart saved as {final_path}")
        return final_path
    except Exception as e:
        logger.error(f"Exception in create_cve_count_by_cvss_chart: {e}")
        return None

def import_image(file_path, pie_chart, bar_chart):
    """
    Fonction qui importe les graphiques créés dans le rapport markdow nqui sera utilisé pour faire le rapport complet
    (combinaisons des différents markdown partiels)

    :param file_path: Donné en input par le code de Main.py, chemin vers le markdown sans les graphiques
    :param pie_chart: Chemin vers le graphique camembert qui a été créé, à ajouter dans le rapport
    :param bar_chart: Chemin vers le graphique barres qui a été créé, à ajouter dans le rapport
    :type file_path: str
    :type pie_chart: str
    :type bar_chart: str

    :return: Return le nom du nouveau rapport dans le dossier.
    Exemple : resultat_scan_penchecker_{today}.md -> resultat_scan_penchecker_{today}_modified.md
    """
    try:
        if pie_chart is None or bar_chart is None:
            logger.error("Pie chart or bar chart not provided, cannot import images.")
            return

        pie_chart_path = os.path.abspath(pie_chart)
        bar_chart_path = os.path.abspath(bar_chart)

        # Lire le contenu markdown original
        with open(file_path, 'r', encoding='utf-8') as file:
            markdown_content = file.read()

        # Trouver la position pour insérer le nouveau contenu
        insert_index = markdown_content.find("## CVEs")
        if insert_index == -1:
            logger.error("Section 'CVEs' not found in the markdown content.")
            return "Section 'CVEs' not found in the markdown content."

        # Définir les nouvelles sections avec les images
        images_section = f"""
## Répartition des CVEs en fonction des services
![pie_chart]({pie_chart_path})

## Repartition des CVEs en fonction de leur score CVSS
![bar_chart]({bar_chart_path})
"""
        # Insérer les nouvelles sections dans le contenu original
        modified_content = markdown_content[:insert_index] + images_section + markdown_content[insert_index:]

        # Enregistrer le contenu modifié dans un nouveau fichier markdown
        output_file_path = file_path.replace('.md', '_modified.md')
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)

        logger.info(f"Images imported successfully into {output_file_path}")
        return output_file_path
    except Exception as e:
        logger.error(f"Exception in import_image: {e}")
        return None

def main(file_path, output_image_path):
    """
    Fonction main du programme. Sert à lancer la tentative de génération des graphiques et leur import dans le dossier.
    C'est cette fonction qui est appelée par Main.py

    :param file_path: Chemin vers le fichier markdown dans le dossier nommé par l'@IP de la machine concernée
    :param output_image_path: Chemin vers le dossier dans lequel sauvegarder les graphiques
    :type file_path: str
    :type output_image_path: str

    :return: Ne return rien, créer ou non dans le dossier les graphiques, et si ils sont crées, les import dans un
    nouveau fichier markdown portant le même nom avec "_modified" à la fin
    """
    try:
        pie_chart = generate_cve_pie_chart(file_path, output_image_path)
        bar_chart = create_cve_count_by_cvss_chart(file_path, output_image_path)
        import_image(file_path, pie_chart, bar_chart)
    except Exception as e:
        logger.error(f"Exception in main: {e}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.critical(f"Critical error in main execution: {e}")