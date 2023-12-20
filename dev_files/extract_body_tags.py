# from bs4 import BeautifulSoup

# input_file_path = 'page_content-ln.html'
# output_file_path = 'body_content.html'

# with open(input_file_path, 'r', encoding='utf-8') as input_file:
#     page_content = input_file.read()

# soup = BeautifulSoup(page_content, 'html.parser')

# # Extract content between body tags
# body_content = soup.body

# if body_content:
#     # Create a new HTML file with only body content
#     with open(output_file_path, 'w', encoding='utf-8') as output_file:
#         output_file.write(str(body_content))
#         print(f"Body content extracted and saved to '{
#               output_file_path}' file.")
# else:
#     print("No body content found in the input file.")


from bs4 import BeautifulSoup

input_file_path = 'page_content-ln.html'
output_file_path = 'body_content.html'

with open(input_file_path, 'r', encoding='utf-8') as input_file:
    page_content = input_file.read()

soup = BeautifulSoup(page_content, 'html.parser')

# Find the first occurrence of <div class="mb1">
first_div_mb1 = soup.find('div', class_='mb1')

if first_div_mb1:
    # Remove all elements before the first <div class="mb1">
    for element in soup.descendants:
        if element == first_div_mb1:
            break
        if element.parent:
            element.extract()

    # Save the modified content to a new HTML file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(str(first_div_mb1))
        print(f"Content after <div class='mb1'> extracted and saved to '{
              output_file_path}' file.")
else:
    print("No <div class='mb1'> found in the input file.")
