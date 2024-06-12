import os
from datetime import datetime

def concat_markdown_files(root_dir):
    # Obtenir la date du jour au format YYYY-MM-DD
    date_du_jour = datetime.now().strftime('%Y-%m-%d')
    filename_pattern = f'resultat_scan_penchecker_{date_du_jour}_modified.md'
    output_filename = 'resultat_concatenated.md'

    # Créer/vider le fichier de sortie
    with open(output_filename, 'w', encoding='utf-8') as outfile:
        outfile.write("# Voici le rapport final du scan effectué par PenChecker\n\n")
        outfile.write("Dans ce rapport vous retrouverez dans l'ordre des @IP les différents résultats\n")
        outfile.write("Voici le rapport final du scan effectué par PenChecker, le rapport est articulé ainsi : \n\n")
        outfile.write(""" 
- La machine concernée
  - Port and Services
    - Listes des différents ports/services accessibles avec numéros de versions
  - Répartition des CVEs en fonction des services
    - Représentation graphique camembert
  - Repartition des CVEs en fonction de leur score CVSS
    - Représentation graphique barre
  - CVEs
    - Listing de toutes les CVEs trouvées pour tous les ports/services\n\n
""")

    # Parcourir les sous-dossiers de root_dir
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file == filename_pattern:
                file_path = os.path.join(subdir, file)
                # Lire le contenu du fichier et l'ajouter au fichier de sortie
                with open(file_path, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    with open(output_filename, 'a') as outfile:
                        outfile.write(content)
                        outfile.write("\n\n")

    print(f"Fichier concaténé créé : {output_filename}")


# Utiliser la fonction
concat_markdown_files('./Rapport_Tmp/')
