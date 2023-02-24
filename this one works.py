from scrapingbee import ScrapingBeeClient
from bs4 import BeautifulSoup

client = ScrapingBeeClient(api_key='UVDRFJ0V9G6L6XU0UW8PW3WDP1PQG7IIBMWG4XUA08Z30P0TKT7WPXGHU1OE6HGVJOQWSG41GU52O7G9')
response = client.get('https://www.udemy.com/course/principles-ppt-design/')

print('Response HTTP Status Code: ', response.status_code)
#print('Response HTTP Response Body: ', response.content)
soup = BeautifulSoup(response.content, 'html.parser')
# find all text in the HTML content
discount_tags = soup.find_all(attrs={'class': lambda x: x and 'discount' in x})
for tag in discount_tags:
    #print(f"Attribute: {tag.attrs}, Class: {tag['class']}")
    pass
discount_tag = soup.find('div', class_='ud-clp-percent-discount')

exp = soup.find('div', class_='generic-purchase-section--buy-box-main--2o6Au')
#print(exp)
span_element = soup.find('span', class_='redeem-coupon--code-text--2HFA4')
coupon_status ="not applied"
if span_element and 'applied' in span_element.text:
    print('Text "applied" found in span element.')
    coupon_status="Applied"
else:
    print('Text "applied" not found in span element.')
old_price_div = soup.find('div', attrs={'data-purpose': 'course-old-price-text'})
if old_price_div:
    print(old_price_div.text)
else:
    print('Old price div not found.')
# Print the text inside the tag
print(discount_tag)
