from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import json
import time
from datetime import datetime
import os

#change this to point to the identity file for the computer it is running on
# filepath_to_identity="identity.py"

# exec(open(filepath_to_identity).read())

#vars
#directory where logs will be saved
working_directory="C://Users//Aaron Wong//Desktop//connect_yee_hong_internet//universal_connection"
#name of the wifi adapter
five_ghz_adapter_name="Wi-Fi 3"
#the script to initate hotspot turn off
path_to_turn_OFF_hotspot_script="C://Users//Aaron Wong//Desktop//connect_yee_hong_internet//universal_connection//active_scripts//turn_OFF_hotspot.ps1"
#ther script to initiate hotspot tunr on 
path_to_turn_ON_hotspot_script="C://Users//Aaron Wong//Desktop//connect_yee_hong_internet//universal_connection//active_scripts//turn_on_hotspot.ps1"
#whether to run the hotspot
run_hotspot=False
#path to revboot script
path_reboot_bat="C://Users//Aaron Wong//Desktop//connect_yee_hong_internet//universal_connection//active_scripts//reboot.bat"
#name of profile of internet to connect to in case Yee Hong is unsuccessful. Must have connected previously to establish a saved profile
backup_wifi="Dragon_backup"


print("backup wifi is: "+backup_wifi)
print("The chrome driver path is: "+chrome_driver_path)

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

url='https://twitter.com/'
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
            time.sleep(30)
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
        os.system("docker run -ti --rm --network host yh1 python3 ./temp/run_connect_yee_hong.py")
        return(check_internet_connection(url))
    except:
        print(current_time,"Failure to accept yee hong agreement.", file=open(date_today+output_name,"a"))


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

#######################################################################
#if you wanto test a function uncomment, and we can inject code here.
# exec(open("test_functions.py").read())
date_today=datetime.today().strftime('%Y-%m-%d')
print("2023", file=open(date_today+output_name,"a"))
fail_count=0
#the main loop
while True:
    # check if the connected to the internet, if connected, it just loops between this first line
    # if no connection, then start troublshooting
    if (not check_internet_connection(url)):
        #first troubleshoot is reset adapter, turn off hotspot, reconnect to yee hong, turn on hotspot
        reset_network_adapter(five_ghz_adapter_name=five_ghz_adapter_name)
        if run_hotspot:
            turn_off_hotspot(path_to_turn_OFF_hotspot_script=path_to_turn_OFF_hotspot_script)
        connect_to_network(five_ghz_adapter_name=five_ghz_adapter_name, ssid="YHCGuest", name="YHCGuest")
        if run_hotspot:
            turn_on_hotspot(run_hotspot=run_hotspot,path_to_turn_ON_hotspot_script=path_to_turn_ON_hotspot_script)
        #if internet still fails, then try to accept the yee hong agreeement
        if(not check_internet_connection(url)):
            accept_yee_hong_agreement(url,chrome_options)
            #if internet stil fails, do a fail count and then attempt to connect to dragon back up
            if(not check_internet_connection(url)):
                check_if_reboot_needed(path_reboot_bat=path_reboot_bat)
                if run_hotspot:
                    turn_off_hotspot(path_to_turn_OFF_hotspot_script=path_to_turn_OFF_hotspot_script)
                connect_to_network(five_ghz_adapter_name=five_ghz_adapter_name, ssid=backup_wifi, name=backup_wifi)
                if run_hotspot:
                    turn_on_hotspot(run_hotspot=run_hotspot,path_to_turn_ON_hotspot_script=path_to_turn_ON_hotspot_script)
                #if internet stil fails connect to Aaron back up
                if(not check_internet_connection(url)):
                    if run_hotspot:
                        turn_off_hotspot(path_to_turn_OFF_hotspot_script=path_to_turn_OFF_hotspot_script)
                    connect_to_network(five_ghz_adapter_name=five_ghz_adapter_name, ssid="Aaron", name="Aaron")
                    if run_hotspot:
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