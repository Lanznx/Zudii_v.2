from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
 
options = Options()
options.add_argument("--disable-notifications")
 
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get("https://www.facebook.com/")

email = chrome.find_element_by_id("email")
password = chrome.find_element_by_id("pass")

email.send_keys('Email')
password.send_keys('Password')
password.submit()

time.sleep(3)
chrome.get('https://www.facebook.com/groups/NCCU.zuker')

for x in range(1, 4):
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
soup = BeautifulSoup(chrome.page_source, 'html.parser')

titles = soup.find_all('div', {'class': 'kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q'})
for title in titles:
 
    post = title.find('div', {'dir': 'auto'})
 
    if post:
        print(post.getText())
chrome.quit()