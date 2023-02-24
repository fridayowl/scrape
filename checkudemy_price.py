import requests
import json
from bs4 import BeautifulSoup

url = "https://www.udemy.com/course/amazon-web-services-aws-v/"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# get id of the course
course_id=soup.body.attrs['data-clp-course-id']
print(course_id)

# build proper request, feel free to delete unneeded data requests
# link=f'https://www.udemy.com/api-2.0/pricing/?course_ids={course_id}&fields[pricing_result]=price,discount_price,list_price,price_detail,price_serve_tracking_id,status_label,is_paid'
# # fetch the data
# res=requests.get(link).json()
# print(res)
link=f'https://www.udemy.com/api-2.0/courses/{course_id}?fields[course]=title,headline,price,price_detail,discount_price'
# fetch the data
res=requests.get(link).json()
print(res)
# Accessing the price field from the JSON object
price = res['price']

# Printing the price
print(price)
