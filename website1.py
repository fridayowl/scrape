import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime, timedelta
from scrapingbee import ScrapingBeeClient
from bs4 import BeautifulSoup
import time
import csv

url = 'https://999coursesale.com/freebie-courses-list.php?pd12=free-v5-ret-orig-2-udemy-ans-no&orig_utm_content=&orig_utm_medium=&orig_utm_campaign=&utm_source=nonzu&_redir='

# Make the request to the website and parse the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
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
    # Given date parts
    day_str =date_parts[0]
    month_str = date_parts[1]
    year_str = date_parts[2]

    # Convert day to integer
    day = int(day_str[:-2])

    # Convert month to integer
    months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
              'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
    month = months[month_str]

    # Convert year to integer
    year = int(year_str)

    # Create a datetime object from the given date
    dt = datetime(year, month, day)

    # Calculate the difference between the current time and the given datetime object
    delta = datetime.now() - dt
    # Check if the difference is less than 72 hours
    if delta < timedelta(hours=72):
        count+=1
    else:
        pass
        #print('The given date is not less than 72 hours from now.')
button = soup.find('div', {'class': 'button'})

buttons = soup.find_all('div', {'class': 'button'})

for button in buttons:
    onclick_value = button.get('onclick')
    if onclick_value:
        # Extract the URL from the handleRedirect JavaScript function using a regular expression
        url_match = re.search(r"handleRedirect\('([^']*)'", onclick_value)
        if url_match:
            url = url_match.group(1)
            print(url)      
print(count)
divs = soup.find_all('div', {'class': 'mt-3 text-center'})
# CSV file name
filename = "courses.csv"

header = ['Course Name', 'Course URL', 'Coupon Code', 'Expiration Date']
# Open the file in write mode and write the header
with open('courses.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
for div in divs:
    url=''
    couponcode=''
    link = div.find('a')
    if link:
        onclick_value = link.get('onclick')
        if onclick_value:
            url = onclick_value.split("'")[1]
            span = div.find('span', {'class': 'w-100'})
            if span:
                text = span.text.strip()
                couponcode=text
                #print(f"URL: {url}\nText: {text}\n")
                fullurl=url+'?ranMID=39197&ranEAID=vWFcdslQDtg&ranSiteID=vWFcdslQDtg-GOO6ha9yKIzdo3cHApJ8IQ&LSNPUBID=vWFcdslQDtg&utm_source=aff-campaign&utm_medium=udemyads&couponCode='+couponcode
                print(fullurl)
                client = ScrapingBeeClient(api_key='UVDRFJ0V9G6L6XU0UW8PW3WDP1PQG7IIBMWG4XUA08Z30P0TKT7WPXGHU1OE6HGVJOQWSG41GU52O7G9')
                response = client.get(fullurl)
                time.sleep(2)
                print('Response HTTP Status Code: ', response.status_code)
                #print('Response HTTP Response Body: ', response.content)
                soup = BeautifulSoup(response.content, 'html.parser') 
                span_element = soup.find('span', class_='redeem-coupon--code-text--2HFA4')
                coupon_status ="not applied"
                if span_element and 'applied' in span_element.text:
                    #print('Text "applied" found in span element.')
                    coupon_status="Applied"
                discount ="0%"
                try:
                    discount_percent = soup.find('div', {'data-purpose': 'discount-percentage'}).get_text().strip()
                except :
                    discount_percent="0%"  
                #print(discount_percent)
                discount=0;
                if "100%" in discount_percent:
                    #print("Discount percentage contains 100%")
                    discount=100 
                #print(original_price)
                try:
                    expiry_date = soup.find('div', {'data-purpose': 'discount-expiration'}).text.strip().split()[0]
                    #print(expiry_date)
                except :
                    expiry_date = "null"
                print(coupon_status)
                print(discount)
                if coupon_status=="Applied" and discount == 100 :
                    print('Expiry date:', expiry_date)
                    today = datetime.now().date()
                    next_date = today + timedelta(days=int(expiry_date))
                    date_str = soup.find('div', {'class': 'last-update-date'}).text.split('Last updated ')[1]
                    last_update_date = datetime.strptime(date_str, '%m/%Y').date()
                    days_since_last_update = (datetime.now().date() - last_update_date).days
                    print(f'Last update date: {last_update_date}')
                    print(f'Days since last update: {days_since_last_update}')
                    with open('courses.csv', 'a', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow([couponcode, fullurl, couponcode, expiry_date])
