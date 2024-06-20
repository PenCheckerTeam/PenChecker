import gh_md_to_html
import subprocess
import mistune
import pdfkit

def main(MdFile_path):
    subprocess.run(['gh-md-to-html', MdFile_path, '-p', 'rapport.pdf', '-o', 'OFFLINE'])
    subprocess.run(['rm', '-f', 'resultat_concatenated.html'])

if __name__ == "__main__":
    main()
