# from bs4 import BeautifulSoup
# import pandas as pd

# # Function to extract data within HTML comment tags


# def extract_data_from_html(html_file):
#     with open(html_file, 'r', encoding='utf-8') as file:
#         html_content = file.read()

#     # Parse HTML content
#     soup = BeautifulSoup(html_content, 'html.parser')

#     # Find all HTML comment tags and extract their text
#     comment_texts = [comment.string.strip() for comment in soup.find_all(
#         string=lambda text: isinstance(text, str))]

#     # Save extracted data to a text file
#     output_text_file = 'rrr.txt'
#     with open(output_text_file, 'w', encoding='utf-8') as text_file:
#         for text in comment_texts:
#             text_file.write(text + '\n')
#     print(f"Data extracted and saved to '{output_text_file}'")


# # Input HTML file
# input_html_file = 'rrr.html'

# # Extract data from HTML file and save to text file
# extract_data_from_html(input_html_file)


# from bs4 import BeautifulSoup

# # Function to extract data from HTML content


# def extract_data_from_html(html_file):
#     with open(html_file, 'r', encoding='utf-8') as file:
#         html_content = file.read()

#     # Parse HTML content
#     soup = BeautifulSoup(html_content, 'html.parser')

#     # Find all <div class="mb1"> tags
#     mb1_divs = soup.find_all('div', class_='mb1')
#     # Extract information from each <div class="mb1"> tag
#     for div in mb1_divs:
#         # Extract href value from <a> tag inside <div class="mb1">
#         href_tag = div.find('a', href=True)
#         if href_tag:
#             url = href_tag['href']
#             print(f"URL: {url}")

#         # Extract value from <span aria-hidden="true"> tag
#         aria_hidden_span = div.find('span', {'aria-hidden': 'true'})
#         if aria_hidden_span:
#             name = aria_hidden_span.get_text(strip=True)
#             print(f"Name: {name}")

#         company_div = div.find('div', class_='entity-result__primary-subtitle')
#         if company_div:
#             company = company_div.get_text(strip=True)
#             print(f"Company: {company}")

#             # Extract business information after "at", "@", or "bij"
#             delimiters = [' at ', ' @ ', ' bij ']
#             business = None
#             for delimiter in delimiters:
#                 if delimiter in company:
#                     business = company.split(delimiter, 1)[-1].strip()
#                     break

#             if business:
#                 print(f"Business: {business}")

#         print()  # Add a newline between each set of extracted data


# # Input HTML file
# input_html_file = '../page_content-ln.html'

# # Call the function with the provided HTML file
# extract_data_from_html(input_html_file)


# from bs4 import BeautifulSoup
# import pandas as pd

# # Function to extract data from HTML content


# def extract_data_from_html(html_file):
#     with open(html_file, 'r', encoding='utf-8') as file:
#         html_content = file.read()

#     # Parse HTML content
#     soup = BeautifulSoup(html_content, 'html.parser')

#     # Create lists to store extracted data
#     urls, names, companies, businesses = [], [], [], []

#     # Find all <div class="mb1"> tags
#     mb1_divs = soup.find_all('div', class_='mb1')

#     # Extract information from each <div class="mb1"> tag
#     for div in mb1_divs:
#         # Extract href value from <a> tag inside <div class="mb1">
#         href_tag = div.find('a', href=True)
#         if href_tag:
#             url = href_tag['href']
#             urls.append(url)

#         # Extract value from <span aria-hidden="true"> tag
#         aria_hidden_span = div.find('span', {'aria-hidden': 'true'})
#         if aria_hidden_span:
#             name = aria_hidden_span.get_text(strip=True)
#             names.append(name)

#         # Extract value from <div class="entity-result__primary-subtitle t-14 t-black t-normal"> tag
#         company_div = div.find('div', class_='entity-result__primary-subtitle')
#         if company_div:
#             company = company_div.get_text(strip=True)
#             companies.append(company)

#             # Extract business information after "at", "@", or "bij"
#             delimiters = [' at ', ' @ ', ' bij ']
#             business = None
#             for delimiter in delimiters:
#                 if delimiter in company:
#                     business = company.split(delimiter, 1)[-1].strip()
#                     break
#             businesses.append(business if business else '')

#     # Create a DataFrame from the extracted data
#     data = {
#         'URL': urls,
#         'Name': names,
#         'Company': companies,
#         'Business': businesses
#     }
#     df = pd.DataFrame(data)

#     # Write the data to an Excel file
#     output_excel_file = 'extracted_data.xlsx'
#     df.to_excel(output_excel_file, index=False, engine='openpyxl')
#     print(f"Data extracted and saved to '{output_excel_file}'")


# # Input HTML file
# input_html_file = '../page_content-ln.html'

# # Call the function with the provided HTML file
# extract_data_from_html(input_html_file)


from bs4 import BeautifulSoup
import json

# Function to extract data from HTML content


def extract_data_from_html(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Create lists to store extracted data
    data_list = []

    # Find all <div class="mb1"> tags
    mb1_divs = soup.find_all('div', class_='mb1')

    # Extract information from each <div class="mb1"> tag
    for div in mb1_divs:
        # Extract href value from <a> tag inside <div class="mb1">
        href_tag = div.find('a', href=True)
        url = href_tag['href'] if href_tag else ''

        # Extract value from <span aria-hidden="true"> tag
        aria_hidden_span = div.find('span', {'aria-hidden': 'true'})
        name = aria_hidden_span.get_text(
            strip=True) if aria_hidden_span else ''

        # Extract value from <div class="entity-result__primary-subtitle t-14 t-black t-normal"> tag
        company_div = div.find('div', class_='entity-result__primary-subtitle')
        company = company_div.get_text(strip=True) if company_div else ''

        # Extract business information after "at", "@", or "bij"
        delimiters = [' at ', ' @ ', ' bij ']
        business = ''
        for delimiter in delimiters:
            if delimiter in company:
                business = company.split(delimiter, 1)[-1].strip()
                break

        data_list.append({
            'URL': url,
            'Name': name,
            'Company': company,
            'Business': business
        })

    # Write the data to a JSON file
    output_json_file = 'extracted_data.json'
    with open(output_json_file, 'w', encoding='utf-8') as json_file:
        json.dump(data_list, json_file, indent=4)
    print(f"Data extracted and saved to '{output_json_file}'")


# Input HTML file
input_html_file = '../page_content-ln.html'

# Call the function with the provided HTML file
extract_data_from_html(input_html_file)
