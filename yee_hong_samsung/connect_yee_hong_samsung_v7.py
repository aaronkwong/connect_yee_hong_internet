from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import json
import time
from datetime import datetime
import os


#vars
working_directory="C:/Users/wong/My Drive/yee_hong_samsung"
five_ghz_adapter_name="Wi-Fi 4"
path_to_turn_OFF_hotspot_script="C://Users//wong//My Drive//yee_hong//active_scripts//turn_OFF_hotspot.ps1"
path_to_turn_ON_hotspot_script="C://Users//wong//My Drive//yee_hong//active_scripts//turn_on_hotspot.ps1"
run_hotspot=True
path_reboot_bat='"C://Users//wong//My Drive//yee_hong//active_scripts//reboot.bat"'
backup_wifi="dragon"

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

url='https://www.google.ca/'
output_name="_output_v2.txt"

chrome_options = webdriver.ChromeOptions()
chrome_options.headless = True
fail_count=0

def check_internet_connection(url):
    date_today=datetime.today().strftime('%Y-%m-%d')
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    try:
        a=requests.get(url)
        if(a.url==url):
            print(current_time,"Connected.", file=open(date_today+output_name,"a"))
            # print("connected")
            time.sleep(10)
            global fail_count
            fail_count=0
            return(True)
        else:
            print(current_time,"No internet connection.",file=open(date_today+output_name,"a"))
            return(False)
    except:
        print(current_time,"Failure in checking internet connection.",file=open(date_today+output_name,"a"))
        return(False)

def reset_network_adapter(five_ghz_adapter_name):
    date_today=datetime.today().strftime('%Y-%m-%d')
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    try:
        print(current_time,"Trying to reset the connection.",file=open(date_today+output_name,"a"))
        os.system('netsh interface set interface name="'+five_ghz_adapter_name+'" admin=DISABLED &')
        print(current_time,"adapter disabled "+datetime.now().strftime("%H:%M:%S"),file=open(date_today+output_name,"a"))
        time.sleep(15)
        os.system('netsh interface set interface name="'+five_ghz_adapter_name+'" admin=ENABLED &')
        print(current_time,"adapter enabled "+datetime.now().strftime("%H:%M:%S"),file=open(date_today+output_name,"a"))
        time.sleep(15)
        return(True)
    except:
        print(current_time,"Failure of sending network adapter reset command, or to restore connectivity.", file=open(date_today+output_name,"a"))
        return(False)

def connect_to_network(five_ghz_adapter_name, ssid, name):
    date_today=datetime.today().strftime('%Y-%m-%d')
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    try:
        print(current_time,"Trying to connect to network with ssid: ",ssid,".",file=open(date_today+output_name,"a"))
        os.system('netsh wlan connect ssid='+ssid+' name='+name+' interface="'+five_ghz_adapter_name+'" &')
        time.sleep(10)
        return(True)
    except:
        print(current_time,"Failure of sending command to connect to network with ssid ",ssid,".", file=open(date_today+output_name,"a"))
        return(False)

def turn_on_hotspot(run_hotspot,path_to_turn_ON_hotspot_script):
    date_today=datetime.today().strftime('%Y-%m-%d')
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    try:
        if (run_hotspot):
            print(current_time, "turning on hotspot...",file=open(date_today+output_name,"a"))
            os.system('powershell -File "'+path_to_turn_ON_hotspot_script+'" &')
            return(True)
    except:
        print(current_time,"Failure to send hotspot ON command.", file=open(date_today+output_name,"a"))
        return(False)

def turn_off_hotspot(path_to_turn_OFF_hotspot_script):
    date_today=datetime.today().strftime('%Y-%m-%d')
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    try:
        print(current_time,"turning off hotspot...",file=open(date_today+output_name,"a"))
        os.system('powershell -File "'+path_to_turn_OFF_hotspot_script+'" &')
        return(True)
    except:
        print(current_time,"Failure to send hotspot OFF command.", file=open(date_today+output_name,"a"))
        return(False)


def accept_yee_hong_agreement(url,chrome_options):
    date_today=datetime.today().strftime('%Y-%m-%d')
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    try:
        print(current_time,"accepting yee hong agreement...",file=open(date_today+output_name,"a"))
        driver=webdriver.Chrome(chrome_options=chrome_options)
        time.sleep(5)
        driver.get(url)
        time.sleep(10)
        driver.find_element_by_xpath("//input[@value='Accept']").click()
        time.sleep(5)
        driver.close()
        print(current_time,"Successfully accepted yee hong agreement.", file=open(date_today+output_name,"a"))
        return(True)
    except:
        print(current_time,"Failure to accept yee hong agreement.", file=open(date_today+output_name,"a"))
        return(False)

def check_if_reboot_needed(path_reboot_bat):
    date_today=datetime.today().strftime('%Y-%m-%d')
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    try:
        global fail_count
        fail_count=fail_count+1
        print(current_time,"fail count is..."+str(fail_count),file=open(date_today+output_name,"a"))
        if(fail_count>10):
            fail_count=0
            os.system('"'+path_reboot_bat+'"'+' &')
    except:
        print(current_time,"Failure to send reboot command.", file=open(date_today+output_name,"a"))


fail_count=0
#the main loop
while True:
    # check if the connected to the internet, if connected, it just loops between this first line
    # if no connection, then start troublshooting
    if (not check_internet_connection(url)):
        #first troubleshoot is reset adapter, turn off hotspot, reconnect to yee hong, turn on hotspot
        reset_network_adapter(five_ghz_adapter_name=five_ghz_adapter_name)
        turn_off_hotspot(path_to_turn_OFF_hotspot_script=path_to_turn_OFF_hotspot_script)
        connect_to_network(five_ghz_adapter_name=five_ghz_adapter_name, ssid="YHCGuest", name="YHCGuest")
        turn_on_hotspot(run_hotspot=run_hotspot,path_to_turn_ON_hotspot_script=path_to_turn_ON_hotspot_script)
        #if internet still fails, then try to accept the yee hong agreeement
        if(not check_internet_connection(url)):
            accept_yee_hong_agreement(url,chrome_options)
            #if internet stil fails, do a fail count and then attempt to connect to dragon back up
            if(not check_internet_connection(url)):
                check_if_reboot_needed(path_reboot_bat=path_reboot_bat)
                turn_off_hotspot(path_to_turn_OFF_hotspot_script=path_to_turn_OFF_hotspot_script)
                connect_to_network(five_ghz_adapter_name=five_ghz_adapter_name, ssid=backup_wifi, name=backup_wifi)
                turn_on_hotspot(run_hotspot=run_hotspot,path_to_turn_ON_hotspot_script=path_to_turn_ON_hotspot_script)
                #if internet stil fails connect to Aaron back up
                if(not check_internet_connection(url)):
                    turn_off_hotspot(path_to_turn_OFF_hotspot_script=path_to_turn_OFF_hotspot_script)
                    connect_to_network(five_ghz_adapter_name=five_ghz_adapter_name, ssid="Aaron", name="Aaron")
                    turn_on_hotspot(run_hotspot=run_hotspot,path_to_turn_ON_hotspot_script=path_to_turn_ON_hotspot_script)
    






# while True:
#     date_today=datetime.today().strftime('%Y-%m-%d')
#     try:
#         url= 'http://www.google.ca/'
#         a=requests.get(url)
#         if(a.url==url):
#             pass
#         else:
#             raise ValueError("we are being redirected!!")
#         now = datetime.now()
#         current_time = now.strftime("%H:%M:%S")
#         print("Connected. Current Time =", current_time,file=open(date_today+"_output.txt","a"))
#         # print("connected")
#         time.sleep(10)
#         # raise ValueError('A very specific bad thing happened.')
#         # time.sleep(1)
#     except:
#         try:
#             print("No internet connection. Trying to reset the connection.",file=open(date_today+"_output.txt","a"))
#             os.system('netsh interface set interface name="'+five_ghz_adapter_name+'" admin=DISABLED &')
#             print("adapter disabled "+datetime.now().strftime("%H:%M:%S"),file=open(date_today+"_output.txt","a"))
#             time.sleep(15)
#             os.system('netsh interface set interface name="'+five_ghz_adapter_name+'" admin=ENABLED &')
#             print("adapter enabled "+datetime.now().strftime("%H:%M:%S"),file=open(date_today+"_output.txt","a"))
#             time.sleep(15)
#             os.system('netsh wlan connect ssid=YHCGuest name=YHCGuest interface="'+five_ghz_adapter_name+'" &')
#             time.sleep(10)
#             b=requests.get(url)
#             if(b.url==url):
#                 pass
#             else:
#                 raise ValueError("we are being redirected!!"+datetime.now().strftime("%H:%M:%S"),file=open(date_today+"_output.txt","a"))
#             now = datetime.now()
#             current_time = now.strftime("%H:%M:%S")
#             print("Connected. Current Time =", current_time,file=open(date_today+"_output.txt","a"))
#             if (run_hotspot):
#                 print("turning on hotspot..."+datetime.now().strftime("%H:%M:%S"),file=open(date_today+"_output.txt","a"))
#                 os.system('powershell -File "'+path_to_turn_ON_hotspot_script+'" &')
#         except:
#            fail_count=fail_count+1
#            print("fail count is..."+str(fail_count),file=open(date_today+"_output.txt","a"))
#            if(fail_count>10):
#                fail_count=0
#                os.system(path_reboot_bat+' &')
#             try:
#                 driver=webdriver.Chrome(chrome_options=chrome_options)
#                 time.sleep(5)
#                 driver.get('http://google.ca')
#                 time.sleep(10)
#                 driver.find_element_by_xpath("//input[@value='Accept']").click()
#                 time.sleep(5)
#                 driver.close()
#                 url= 'http://www.google.ca/'
#                 c=requests.get(url)
#                 if(c.url==url):
#                     fail_count=0
#                 else:
#                     raise ValueError("no connection even after attempting to accept yee hong agreement")
#                 if (run_hotspot):
#                     print("turning on hotspot...",file=open(date_today+"_output.txt","a"))
#                     os.system('powershell -File "'+path_to_turn_ON_hotspot_script+'" &')
#             except:
#                 try:
#                     print("attempting to connect to dragon_backup....",file=open(date_today+"_output.txt","a"))
#                     #here we try to connecty to another win 10 hotspot. while win10 is connected to another win10 hotspot, you cannot use your own hotspot
#                     os.system('powershell -File "'+path_to_turn_OFF_hotspot_script+'" &')
#                     os.system('netsh wlan connect ssid=dragon_backup name=dragon_backup interface="'+five_ghz_adapter_name+'" &')
#                     time.sleep(10)
#                     c=requests.get(url)
#                     if(c.url==url):
#                         pass
#                     else:
#                         raise ValueError("no connection even after attempting to connect to other computer")
#                 except:
#                     try:
#                         print("attempting to connect to Aaron_backup....",file=open(date_today+"_output.txt","a"))
#                         os.system('powershell -File "'+path_to_turn_OFF_hotspot_script+'" &')
#                         os.system('netsh wlan connect ssid=Aaron name=Aaron interface="'+five_ghz_adapter_name+'" &')
#                         time.sleep(10)
#                         c=requests.get(url)
#                         if(c.url==url):
#                             pass
#                         else:
#                             raise ValueError("no connection even after attempting to Aaron")
#                     except:
#                         pass