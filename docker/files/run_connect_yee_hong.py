from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import time
from datetime import datetime
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")

chrome_driver_path="/usr/bin/chromedriver"

def accept_yee_hong_agreement(url,chrome_options,time_wait_base=5):
    try:
        driver=webdriver.Chrome(chrome_options=chrome_options,executable_path=chrome_driver_path)
        time.sleep(time_wait_base)
        driver.get(url)
        time.sleep(time_wait_base*4)
        print(driver.title)
        driver.find_element("xpath","//input[@value='Accept']").click()
        time.sleep(time_wait_base)
        print("yee hong button found!")
        driver.close()
    except:
        #it seems that sometimes there are warning from chromedriver causing this statement to come up even when the yee hong agreement is successfully agreed to
        print("an error occured while accepting the yee hong agreement")
        pass

accept_yee_hong_agreement('http://google.com',chrome_options,time_wait_base=4)
#for testing against a downloaded html of the captive portal
# accept_yee_hong_agreement('file:///temp/portal/Captive Portal.html',chrome_options,time_wait_base=0.01)

#export DISPLAY=172.26.192.1:0.0