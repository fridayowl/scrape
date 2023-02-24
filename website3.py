import requests
from bs4 import BeautifulSoup

url = 'https://freesoff.com/t/100-off-udemy-course-23-02-2023/403506'

# Send a GET request to the website URL
response = requests.get(url)
print(response)
# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the <a> tags in the parsed content
a_tags = soup.find_all('a')

# Extract the href attribute of each <a> tag and check if it contains 'couponCode='
for a in a_tags:
    href = a.get('href')
    if href and 'couponCode=' in href:
        print(a)
