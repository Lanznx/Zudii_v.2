from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from email.headerregistry import Group
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
time.sleep(2)
chrome.get('https://www.facebook.com/groups/NCCU.zuker')

WebDriverWait(chrome, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gpro0wi8.oo9gr5id.lrazzd5p"))
) ## Wait for the page loading
clicks_more = chrome.find_elements_by_css_selector('.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gpro0wi8.oo9gr5id.lrazzd5p')

for _ in range(10):
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)











