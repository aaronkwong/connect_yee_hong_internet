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

# os.system('netsh interface set interface name="Wi-Fi 4" admin=DISABLED')
# time.sleep(15)
# os.system('netsh interface set interface name="Wi-Fi 4" admin=ENABLED')
# time.sleep(15)


chrome_options = webdriver.ChromeOptions()
chrome_options.headless = True

while True:
    try:
        url= 'http://www.google.ca/'
        a=requests.get(url)
        if(a.url==url):
            pass
        else:
            raise ValueError("we are being redirected!!")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Connected. Current Time =", current_time)
        # print("connected")
        time.sleep(10)
        # raise ValueError('A very specific bad thing happened.')
        # time.sleep(1)
    except:
        try:
            print("No internet connection. Resetting internet")
            os.system('netsh interface set interface name="Wi-Fi 4" admin=DISABLED')
            print("adapter disabled")
            time.sleep(15)
            os.system('netsh interface set interface name="Wi-Fi 4" admin=ENABLED')
            print("adapter enabled")
            time.sleep(15)
            os.system("netsh wlan connect ssid=YHCGuest name=YHCGuest")
            time.sleep(10)
            try:
                b=requests.get(url)
                if(b.url==url):
                    pass
                else:
                    raise ValueError("we are being redirected!!")
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print("Connected. Current Time =", current_time)
            except:
                try:
                    driver=webdriver.Chrome(chrome_options=chrome_options)
                    time.sleep(3)
                    driver.get('http://google.ca')
                    time.sleep(10)
                    driver.find_element_by_xpath("//input[@value='Accept']").click()
                    time.sleep(5)
                    driver.close()
                except:
                    pass
        except:
            pass