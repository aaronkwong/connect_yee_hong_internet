from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import json
import time
from datetime import datetime
import os


# def check_online():
#     while True:
#         try:
#             requests.get('http://google.ca')
#             time.sleep(1)
#         except:
#             driver=webdriver.Chrome()
#             print("No internet connection.")
#             driver.get('file:///H:/grandpa%20wifi/Captive%20Portal.html')
#             driver.find_element_by_xpath("//input[@value='Accept']").click()
#             time.sleep(5)


chrome_options = webdriver.ChromeOptions()
chrome_options.headless = True

while True:
    try:
        requests.get('http://google.ca')
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Connected. Current Time =", current_time)
        # print("connected")
        time.sleep(1)
        # raise ValueError('A very specific bad thing happened.')
        # time.sleep(1)
    except:
        try:
            print("No internet connection.")
            os.system("netsh wlan connect ssid=YHCGuest name=YHCGuest")
            time.sleep(10)
            try:
                requests.get('http://google.ca')
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print("Connected. Current Time =", current_time)
            except:
                driver=webdriver.Chrome(chrome_options=chrome_options)
                time.sleep(3)
                driver.get('http://google.ca')
                time.sleep(10)
                driver.find_element_by_xpath("//input[@value='Accept']").click()
                time.sleep(5)
                driver.close()
            except:
                driver.close()