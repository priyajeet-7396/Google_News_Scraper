import os
from googlesearch import search
import pdfkit

# Replace this with your desired search query
search_query = "pavagada solar park"

# Get search results from Google News
search_results = search(query=search_query, tld='com', lang='en', num=10, stop=10, pause=2.0, extra_params={'tbm': 'nws'})

# Directory to save PDFs
output_directory = "Google_News_PDFs"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Set path to wkhtmltopdf executable
config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

# Convert each search result page to PDF
for idx, link in enumerate(search_results):
    try:
        print(f"Converting page {idx+1}: {link}")
        pdfkit.from_url(link, os.path.join(output_directory, f"page_{idx+1}.pdf"), configuration=config)
        print(f"Page {idx+1} converted to PDF successfully!")
    except Exception as e:
        print(f"Failed to convert page {idx+1} to PDF: {str(e)}")
