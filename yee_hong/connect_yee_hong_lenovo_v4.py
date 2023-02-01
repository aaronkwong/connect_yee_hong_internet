from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import json
import time
from datetime import datetime
import os


#vars
working_directory="C:/Users/jw367/My Drive/yee_hong"
five_ghz_adapter_name="Wi-Fi 2"
path_to_turn_OFF_hotspot_script="C://Users//jw367//My Drive//yee_hong//active_scripts//turn_OFF_hotspot.ps1"
path_to_turn_ON_hotspot_script="C://Users//jw367/My Drive//yee_hong//active_scripts//turn_on_hotspot.ps1"
run_hotspot=True
path_reboot_bat="C://Users//jw367//My Drive//yee_hong//active_scripts//reboot.bat"

if(os.path.isfile(path_to_turn_OFF_hotspot_script)):
    print("good")

if(os.path.isfile(path_to_turn_ON_hotspot_script)):
    print("good")

if(os.path.isfile(path_reboot_bat)):
    print("good")

if (run_hotspot):
    print("hotspot wil be turned on.")

# ORDER OF AUTOMATED INTERNET SEARCH 
# Yee Hong Wifi
#     Small Other PC broadcasted Wifi
#         Aaron comes to yee hong and hotspots from outside

os.chdir(working_directory)


chrome_options = webdriver.ChromeOptions()
chrome_options.headless = True
fail_count=0

while True:
    date_today=datetime.today().strftime('%Y-%m-%d')
    try:
        url= 'http://www.google.ca/'
        a=requests.get(url)
        if(a.url==url):
            pass
        else:
            raise ValueError("we are being redirected!!")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Connected. Current Time =", current_time,file=open(date_today+"_output.txt","a"))
        # print("connected")
        time.sleep(10)
        # raise ValueError('A very specific bad thing happened.')
        # time.sleep(1)
    except:
        try:
            print("No internet connection. Trying to reset the connection.",file=open(date_today+"_output.txt","a"))
            os.system('netsh interface set interface name="'+five_ghz_adapter_name+'" admin=DISABLED')
            print("adapter disabled "+datetime.now().strftime("%H:%M:%S"),file=open(date_today+"_output.txt","a"))
            time.sleep(15)
            os.system('netsh interface set interface name="'+five_ghz_adapter_name+'" admin=ENABLED')
            print("adapter enabled "+datetime.now().strftime("%H:%M:%S"),file=open(date_today+"_output.txt","a"))
            time.sleep(15)
            os.system('netsh wlan connect ssid=YHCGuest name=YHCGuest interface="'+five_ghz_adapter_name+'"')
            time.sleep(10)
            b=requests.get(url)
            if(b.url==url):
                pass
            else:
                raise ValueError("we are being redirected!!"+datetime.now().strftime("%H:%M:%S"),file=open(date_today+"_output.txt","a"))
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Connected. Current Time =", current_time,file=open(date_today+"_output.txt","a"))
            if (run_hotspot):
                print("turning on hotspot..."+datetime.now().strftime("%H:%M:%S"),file=open(date_today+"_output.txt","a"))
                os.system('powershell -File "'+path_to_turn_ON_hotspot_script+'"')
        except:
            fail_count=fail_count+1
            print("fail count is..."+str(fail_count),file=open(date_today+"_output.txt","a"))
            if(fail_count>10):
                fail_count=0
                os.system(path_reboot_bat)
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
                    fail_count=0
                else:
                    raise ValueError("no connection even after attempting to accept yee hong agreement")
                if (run_hotspot):
                    print("turning on hotspot...",file=open(date_today+"_output.txt","a"))
                    os.system('powershell -File "'+path_to_turn_ON_hotspot_script+'"')
            except:
                try:
                    #here we try to connecty to another win 10 hotspot. while win10 is connected to another win10 hotspot, you cannot use your own hotspot
                    os.system('powershell -File "'+path_to_turn_OFF_hotspot_script+'"')
                    os.system('netsh wlan connect ssid=dragon_backup name=dragon_backup interface="'+five_ghz_adapter_name+'"')
                    time.sleep(10)
                    c=requests.get(url)
                    if(c.url==url):
                        pass
                    else:
                        raise ValueError("no connection even after attempting to connect to other computer")
                except:
                    try:
                        os.system('powershell -File "'+path_to_turn_OFF_hotspot_script+'"')
                        os.system('netsh wlan connect ssid=Aaron name=Aaron interface="'+five_ghz_adapter_name+'"')
                        time.sleep(10)
                        c=requests.get(url)
                        if(c.url==url):
                            pass
                        else:
                            raise ValueError("no connection even after attempting to Aaron")
                    except:
                        pass