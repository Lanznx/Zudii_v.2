from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from email.headerregistry import Group
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


options = Options()
options.add_argument("--disable-notifications")

## -------- 路徑、帳密要自己改 --------
chrome = webdriver.Chrome('/Users/lanz/Downloads/檔案/chromedriver')
chrome.get("https://www.facebook.com/")

email = chrome.find_element_by_id("email")
password = chrome.find_element_by_id("pass")

email.send_keys('109305033@g.nccu.edu.tw')
password.send_keys('Zudii@Andiidii')
password.submit()
## -------- 路徑、帳密要自己改 --------

time.sleep(3)
chrome.get('https://www.facebook.com/groups/NCCU.zuker')


## 把頁面滑到最下面 並 按下所有的顯示更多

scroll_time = 2
for i in range(scroll_time):
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1.5)
    more = """
            var div_tags = document.getElementsByTagName("div"); 
            for(var i = 0 ; i < div_tags.length ; i ++) {
                var div_text = div_tags[i].innerText; 

                if (div_tags[i].innerText == "顯示更多") {
                    div_tags[i].click();
                }
            }

            
        """
    chrome.execute_script(more)





soup = BeautifulSoup(chrome.page_source, 'html.parser')
## 找出所有內文（內文裡面還會有很多行）
contents = soup.find_all('div', {'class': 'ecm0bbzt hv4rvrfc ihqw7lf3 dati1w0a'})
for content in contents: 
    ## 把內文的每一行都找出來，並印出來
    posts = content.find_all('div', {'dir': 'auto'}, {'style': "text-align: start"})
    for post in posts:
        print(post.getText())
    print("-------------------------------------------")

import re

def extract(content):
    content = content.replace(",","")
        
    f = lambda x:True if int(x)>2500 else False
    nums=list(map(int,list(filter(f,re.findall(r'-?\d+\.?\d*',content)))))
    if nums:
        return max(nums)
    else:
        return 
    
def digit(content):
    return any(i.isdigit() for i in content)

location, rent, room=[[] for i in range(3)]

for content in contents: 
    posts = content.find_all('div', {'dir': 'auto'}, {'style': "text-align: start"})
    for post in posts:
        if "租金" in post.getText() and digit(post.getText())==True:
            rent.append(extract(post.getText())) 
        elif "家賃" in post.getText() and digit(post.getText())==True:
            rent.append(extract(post.getText()))
        elif "價格" in post.getText() and digit(post.getText())==True:
            rent.append(extract(post.getText()))
            
print(rent)