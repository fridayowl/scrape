import requests
from bs4 import BeautifulSoup

from datetime import datetime, timedelta


url = 'https://999coursesale.com/freebie-courses-list.php?pd12=free-v5-ret-orig-2-udemy-ans-no&orig_utm_content=&orig_utm_medium=&orig_utm_campaign=&utm_source=nonzu&_redir='

# Make the request to the website and parse the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
print(response)
# course_name = soup.select_one('h3.heading').text
# expiry_date = soup.select_one('span.text2').text
# 
# print('Course Name:', course_name)
# print('Expiry Date:', expiry_date)
row_elem = soup.find('div', class_='row')
heading_elems = row_elem.find_all('h3', class_='heading')
# Print the text content of each h3 element
# for heading_elem in heading_elems:
#     print(heading_elem.text)
# Find the span element with class="text2" within the row_elem
text2_spans = row_elem.find_all('span', class_='text2')
count=0
# Print the content of each span element
for text2_span in text2_spans:
    date_str =text2_span.text
    date_parts = date_str.split()

    # convert the day number to an integer
    day = int(date_parts[0][:-2])

    # get the month abbreviation as a string
    month_str = date_parts[1][:-1]
    month = datetime.strptime(month_str, "%b").month

    # get the year as an integer
    year = int(date_parts[2])

    # construct a datetime object from the parsed date components
    formatted_date = datetime(year=year, month=month, day=day)

    #print(formatted_date)
    delta_72_hours = timedelta(hours=72)

    # get the current date and time as a datetime object
    now = datetime.now()

    # calculate the difference between the expiration date and the current date
    time_difference = formatted_date - now

    # check if the time difference is less than 72 hours
    if time_difference < delta_72_hours:
        #print("less than 72 hours!")
        count+=1
    else:
        #print("more than 72 hours.")
        pass
print(count)

