from md2pdf.core import md2pdf


def markdown_to_pdf(markdown_file_path, output_pdf_path):

    md2pdf(pdf_file_path=output_pdf_path, md_file_path=markdown_file_path)

# Example usage
if __name__ == "__main__":
    markdown_file = './Rapport_Tmp/192.168.50.2/resultat_scan_penchecker_2024-06-12_modified.md'  # Replace with your Markdown file path
    output_pdf = 'example.pdf'  # Replace with your desired output PDF file path
    markdown_to_pdf(markdown_file, output_pdf)
