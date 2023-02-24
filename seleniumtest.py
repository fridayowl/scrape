from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# set up the headless browser
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

# load the webpage using Selenium
driver.get('https://example.com')

# wait for the JavaScript to load
driver.execute_script('return document.readyState') # this will wait for the page to be fully loaded

# parse the HTML content using Beautiful Soup
html_content = driver.page_source
soup = BeautifulSoup(html_content, 'html.parser')
print(soup)

# close the browser
driver.quit()

