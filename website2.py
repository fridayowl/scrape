import requests
from bs4 import BeautifulSoup
from datetime import datetime , timedelta
url = "https://yofreesamples.com/courses/free-discounted-udemy-courses-list/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

response = requests.get(url, headers=headers) 
soup = BeautifulSoup(response.content, "html.parser")
print(soup)
print(response)
h1_tags = soup.find_all("h1", class_="entry-title")
for h1 in h1_tags:
    print(h1.text.strip())
    date_string= h1.text.strip()

date_str = date_string.split("–")[1].strip()

# parse the date string using datetime.strptime()
date_obj = datetime.strptime(date_str, "%m/%d/%Y")

# print the resulting datetime object
print(date_obj)
now = datetime.now()
delta = now - date_obj
count=0
# check if the time difference is less than 72 hours (3 days)
if delta < timedelta(days=3):
    print("The date and time is less than 72 hours old.")
    divs = soup.find_all('div', {'class': 'kt-inside-inner-col'})
    # Extract the contents of the divs
    for div in divs:
        print(div.text)
        count+=1
print(count)
#     div_element = soup.find('div', {'class': 'wp-block-kadence-rowlayout'})
#     for result in div_element:
#         h4_tags = result.find_all('h4')
#         for tag in h4_tags:
#             print(tag.text)

