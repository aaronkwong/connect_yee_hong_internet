from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import json
import time
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
        print("wifi is good")
        time.sleep(1)
        # raise ValueError('A very specific bad thing happened.')
        # time.sleep(1)
    except:
        try:
            os.system("netsh wlan connect ssid=YHCGuest name=YHCGuest")
            print("reconnecting")
            time.sleep(20)
        except:
            pass