import re
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import os

def generate_cve_pie_chart(file_path, output_image_path):
    # Read the markdown file content with the correct encoding
    with open(file_path, 'r', encoding='latin1') as file:
        md_content = file.read()

    # Improved regex pattern to capture all port, service, and CVE count entries
    pattern = re.compile(r'(\d+): (.*?)(?: version=[\w.]+)? \(CVE Count: (\d+)\)')

    # Extract relevant data from the markdown content
    data = pattern.findall(md_content)

    # Convert the extracted data to a DataFrame
    df = pd.DataFrame(data, columns=['Port', 'Service', 'CVE_Count'])
    df['CVE_Count'] = df['CVE_Count'].astype(int)

    # Filter out entries with 0 CVEs
    df_filtered = df[df['CVE_Count'] > 0]

    # Summarize service names longer than 2-3 words
    df_filtered['Service'] = df_filtered['Service'].apply(lambda x: ' '.join(x.split()[:3]))

    # Combine port and service name for the labels
    df_filtered['Label'] = df_filtered.apply(lambda row: f"{row['Port']} | {row['Service']}", axis=1)

    # Group by the new label and sum the CVE counts
    df_grouped = df_filtered.groupby('Label').sum().reset_index()

    # Create a pie chart
    plt.figure(figsize=(10, 7))
    plt.pie(df_grouped['CVE_Count'], labels=df_grouped['Label'], autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of CVE Counts by Service')

    # Save the chart as an image (explicitly use png format)
    final_path = os.path.join(output_image_path, 'pie_chart.png')
    plt.savefig(final_path, format='png')
    plt.close()

    print(f"Pie chart saved as {final_path}")

def create_cve_count_by_cvss_chart(md_file_path, output_image_path):
    # Read the markdown file with the correct encoding
    with open(md_file_path, 'r', encoding='ISO-8859-1') as file:
        content = file.read()

    # Improved regex pattern to extract CVSS scores
    cvss_scores = re.findall(r"\*\*(\d+\.\d+)\*\*", content)
    if not cvss_scores:
        print("No CVSS scores found in the markdown file.")
        return

    # Convert CVSS scores to floats
    cvss_scores = [round(float(score)) for score in cvss_scores if round(float(score)) > 5]

    # Count the occurrences of each CVSS score
    cvss_count = Counter(cvss_scores)

    # Create a DataFrame for the CVSS score counts
    df_cvss = pd.DataFrame(cvss_count.items(), columns=['CVSS_Score', 'Count'])
    df_cvss = df_cvss.sort_values(by='CVSS_Score')

    # Create a bar chart for CVE counts by CVSS score
    plt.figure(figsize=(12, 6))
    plt.bar(df_cvss['CVSS_Score'].astype(str), df_cvss['Count'], color='skyblue')
    plt.xlabel('CVSS Score')
    plt.ylabel('CVE Count')
    plt.title('CVE Count by CVSS Score')

    # Save the bar chart as an image (explicitly use png format)
    final_path = os.path.join(output_image_path, 'cve_count_by_cvss_chart.png')
    plt.savefig(final_path, format='png')
    plt.close()

    print(f"Bar chart saved as {final_path}")

def main(file_path, output_image_path):
    generate_cve_pie_chart(file_path, output_image_path)
    create_cve_count_by_cvss_chart(file_path, output_image_path)

if __name__ == "__main__":
    main()