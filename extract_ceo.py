

from bs4 import BeautifulSoup
import pandas as pd


def extract_company_name(content_list):
    company_names = []
    for content in content_list:
        words = content.split()
        if len(words) >= 2 and words[-1][0].isupper() and words[-2][0].isupper():
            company_names.append(' '.join(words[-2:]))
        elif len(words) >= 1 and words[-1][0].isupper():
            company_names.append(words[-1])
        elif len(words) >= 2 and words[-2][0].isupper():
            company_names.append(' '.join(words[-2:]))
        else:
            company_names.append('N/A')
    return company_names


input_file_path = 'page_content-ln.html'
output_file_path = 'output_data.xlsx'

with open(input_file_path, 'r', encoding='utf-8') as input_file:
    page_content = input_file.read()

soup = BeautifulSoup(page_content, 'html.parser')

output_data = []  # To store extracted data

# Find all <div class="mb1"> tags
mb1_divs = soup.find_all('div', class_='mb1')

for div in mb1_divs:
    a_tag = div.find('a', class_='app-aware-link')
    primary_subtitle = div.find(
        'div', class_='entity-result__primary-subtitle')

    if a_tag and primary_subtitle:
        full_name = a_tag.text.strip()
        company_name = primary_subtitle.text.strip()
        url = a_tag.get('href')

        # Extract first and last names from the full name
        name_parts = full_name.split('View')
        if len(name_parts) > 1:
            name = name_parts[0].strip()
            name_parts = name.split()
            first_name = name_parts[0] if name_parts else ""
            last_name = name_parts[-1] if len(name_parts) > 1 else ""
        else:
            first_name = ""
            last_name = ""

        output_data.append({'First Name': first_name, 'Last Name': last_name,
                           'Company Name': company_name, 'URL': url})

# Extract clean company names using the provided function
company_names = extract_company_name(
    [data['Company Name'] for data in output_data])

# Update the 'Company Name' field with clean names
for i, data in enumerate(output_data):
    data['Company Name'] = company_names[i]

# Convert data to a pandas DataFrame
df = pd.DataFrame(output_data)

# Save DataFrame to Excel file
df.to_excel(output_file_path, index=False)
print(f"Extracted data saved to '{output_file_path}' file.")
