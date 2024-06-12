import os
from datetime import datetime

# Importing functions from the provided scripts
import Starter
import XML_traitement
import Chart_maker

print(":::::::::  :::::::::: ::::    :::  ::::::::  :::    ::: :::::::::: ::::::::  :::    ::: :::::::::: :::::::::       :::     :::   :::        :::::::  ")
print(":+:    :+: :+:        :+:+:   :+: :+:    :+: :+:    :+: :+:       :+:    :+: :+:   :+:  :+:        :+:    :+:      :+:     :+: :+:+:       :+:   :+: ")
print("+:+    +:+ +:+        :+:+:+  +:+ +:+        +:+    +:+ +:+       +:+        +:+  +:+   +:+        +:+    +:+      +:+     +:+   +:+       +:+  :+:+ ")
print("+#++:++#+  +#++:++#   +#+ +:+ +#+ +#+        +#++:++#++ +#++:++#  +#+        +#++:++    +#++:++#   +#++:++#:       +#+     +:+   +#+       +#+ + +:+ ")
print("+#+        +#+        +#+  +#+#+# +#+        +#+    +#+ +#+       +#+        +#+  +#+   +#+        +#+    +#+       +#+   +#+    +#+       +#+#  +#+ ")
print("#+#        #+#        #+#   #+#+# #+#    #+# #+#    #+# #+#       #+#    #+# #+#   #+#  #+#        #+#    #+#        #+#+#+#     #+#   #+# #+#   #+# ")
print("###        ########## ###    ####  ########  ###    ### ########## ########  ###    ### ########## ###    ###          ###     ####### ###  #######  ")
print("")
def get_ip_from_xml(xml_file):
    ip_tmp = (xml_file.split("_")[2]).split(".")[:4]
    ip = ip_tmp[0] + "." + ip_tmp[1] + "." + ip_tmp[2] + "." + ip_tmp[3]
    return ip


def create_directory_structure(ip):
    base_dir = os.path.join('Rapport_Tmp', ip)
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    return base_dir


def main():
    today = datetime.today().strftime('%Y-%m-%d')
    xml_dir = f'xml_result_{today}'
    rapport_dir = 'Rapport_Tmp'

    if not os.path.exists(rapport_dir):
        os.makedirs(rapport_dir)

    Starter.main()

    for filename in os.listdir(xml_dir):
        xml_tmp = filename
        xml_file = os.path.join(xml_dir, filename)

        # Get IP from XML file
        ip = get_ip_from_xml(xml_tmp)

        # Create directory structure for this IP
        ip_dir = create_directory_structure(ip)

        # Run the main functions from each script

        XML_traitement.main(xml_file, ip_dir)
        #Résultats sauvegardés dans Result_tmp/@ip/resulat_scan_penchecker_@ip.md

        today = datetime.today().strftime('%Y-%m-%d')
        md_name = f"resultat_scan_penchecker_{today}.md"
        md_file = os.path.join(ip_dir, md_name)

        img_path_output = os.path.join('Rapport_Tmp', ip)
        Chart_maker.main(md_file, img_path_output)


if __name__ == '__main__':
    main()