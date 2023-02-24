from scrapingbee import ScrapingBeeClient
from bs4 import BeautifulSoup

client = ScrapingBeeClient(api_key='UVDRFJ0V9G6L6XU0UW8PW3WDP1PQG7IIBMWG4XUA08Z30P0TKT7WPXGHU1OE6HGVJOQWSG41GU52O7G9')
response = client.get('https://www.udemy.com/course/digital-marketing-with-google-my-business-seo-website-local-listing/?ranMID=39197&ranEAID=vWFcdslQDtg&ranSiteID=vWFcdslQDtg-H_wirk0hZgIihnSvFsx35Q&LSNPUBID=vWFcdslQDtg&utm_source=aff-campaign&utm_medium=udemyads&couponCode=230223')

print('Response HTTP Status Code: ', response.status_code)
print('Response HTTP Response Body: ', response.content)
soup = BeautifulSoup(response.content, 'html.parser')
# find all text in the HTML content
discount_tags = soup.find_all(attrs={'class': lambda x: x and 'discount' in x})
for tag in discount_tags:
    print(f"Attribute: {tag.attrs}, Class: {tag['class']}")
discount_tag = soup.find('div', class_='ud-clp-percent-discount')

exp = soup.find('div', class_='generic-purchase-section--buy-box-main--2o6Au')
print(exp)
span_element = soup.find('span', class_='redeem-coupon--code-text--2HFA4')
coupon_status ="not applied"
if span_element and 'applied' in span_element.text:
    print('Text "applied" found in span element.')
    coupon_status="Applied"
else:
    print('Text "applied" not found in span element.')

# Print the text inside the tag
print(discount_tag)
