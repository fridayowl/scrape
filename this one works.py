from scrapingbee import ScrapingBeeClient
from bs4 import BeautifulSoup
from datetime import datetime
import time
client = ScrapingBeeClient(api_key='UVDRFJ0V9G6L6XU0UW8PW3WDP1PQG7IIBMWG4XUA08Z30P0TKT7WPXGHU1OE6HGVJOQWSG41GU52O7G9')
response = client.get('https://www.udemy.com/course/css-crash-course-for-beginners-g/?ranMID=39197&ranEAID=vWFcdslQDtg&ranSiteID=vWFcdslQDtg-GOO6ha9yKIzdo3cHApJ8IQ&LSNPUBID=vWFcdslQDtg&utm_source=aff-campaign&utm_medium=udemyads&couponCode=398E44F4EAA96D4EBCC8')
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
print(coupon_status)
print(discount)
try:
    expiry_date = soup.find('div', {'data-purpose': 'discount-expiration'}).text.strip().split()[0]
    #print(expiry_date)
except :
    expiry_date = "null"

if coupon_status=="Applied" and discount == 100 :
    print('Expiry date:', expiry_date)
    date_str = soup.find('div', {'class': 'last-update-date'}).text.split('Last updated ')[1]
    last_update_date = datetime.strptime(date_str, '%m/%Y').date()
    days_since_last_update = (datetime.now().date() - last_update_date).days
    print(f'Last update date: {last_update_date}')
    print(f'Days since last update: {days_since_last_update}')

