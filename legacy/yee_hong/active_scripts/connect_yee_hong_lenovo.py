from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import json
import time
from datetime import datetime
import os



# ORDER OF AUTOMATED INTERNET SEARCH 
# Yee Hong Wifi
#     Small Other PC broadcasted Wifi
#         Aaron comes to yee hong and hotspots from outside

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
            print("No internet connection. Trying to reset the connection.")
            os.system('netsh interface set interface name="Wi-Fi 2" admin=DISABLED')
            time.sleep(15)
            os.system('netsh interface set interface name="Wi-Fi 2" admin=ENABLED')
            time.sleep(15)
            os.system('netsh wlan connect ssid=YHCGuest name=YHCGuest interface="Wi-Fi 2"')
            time.sleep(10)
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
                time.sleep(5)
                driver.get('http://google.ca')
                time.sleep(10)
                driver.find_element_by_xpath("//input[@value='Accept']").click()
                time.sleep(5)
                driver.close()
                url= 'http://www.google.ca/'
                c=requests.get(url)
                if(c.url==url):
                    pass
                else:
                    raise ValueError("no connection even after attempting to accept yee hong agreement")
            except:
                try:
                    #here we try to connecty to another win 10 hotspot. while win10 is connected to another win10 hotspot, you cannot use your own hotspot
                    os.system('powershell -File "C:\\Users\\jw367\\My Drive\\yee_hong\\active_scripts\\turn_OFF_hotspot.ps1"')
                    os.system('netsh wlan connect ssid=dragon_backup name=dragon_backup interface="Wi-Fi 2"')
                    time.sleep(10)
                    c=requests.get(url)
                    if(c.url==url):
                        pass
                    else:
                        raise ValueError("no connection even after attempting to connect to other computer")
                except:
                    try:
                        os.system('powershell -File "C:\\Users\\jw367\\My Drive\\yee_hong\\active_scripts\\turn_OFF_hotspot.ps1"')
                        os.system('netsh wlan connect ssid=Aaron name=Aaron interface="Wi-Fi 2"')
                        time.sleep(10)
                        c=requests.get(url)
                        if(c.url==url):
                            pass
                        else:
                            raise ValueError("no connection even after attempting to Aaron")
                    except:
                        pass