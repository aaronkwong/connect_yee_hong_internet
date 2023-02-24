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
# working_directory="C://Users//Aaron Wong//Desktop//connect_yee_hong_internet//universal_connection"
# #name of the wifi adapter
# five_ghz_adapter_name="Wi-Fi 3"
# #the script to initate hotspot turn off
# path_to_turn_OFF_hotspot_script="C://Users//Aaron Wong//Desktop//connect_yee_hong_internet//universal_connection//active_scripts//turn_OFF_hotspot.ps1"
# #ther script to initiate hotspot tunr on 
# path_to_turn_ON_hotspot_script="C://Users//Aaron Wong//Desktop//connect_yee_hong_internet//universal_connection//active_scripts//turn_on_hotspot.ps1"
# #whether to run the hotspot
# run_hotspot=False
# #path to revboot script
# path_reboot_bat="C://Users//Aaron Wong//Desktop//connect_yee_hong_internet//universal_connection//active_scripts//reboot.bat"
# #name of profile of internet to connect to in case Yee Hong is unsuccessful. Must have connected previously to establish a saved profile
# backup_wifi="Dragon_backup"

#import vars from identity
from identity import working_directory
from identity import five_ghz_adapter_name
from identity import path_to_turn_OFF_hotspot_script
from identity import path_to_turn_ON_hotspot_script
from identity import run_hotspot
from identity import path_reboot_bat
from identity import backup_wifi
from identity import accept_captive_portal_docker_image_name
from identity import path_to_restart_netstack

print("working_directory wifi is: "+working_directory)
print("five_ghz_adapter_name wifi is: "+five_ghz_adapter_name)
print("path_to_turn_OFF_hotspot_script wifi is: "+path_to_turn_OFF_hotspot_script)
print("path_to_turn_ON_hotspot_script wifi is: "+path_to_turn_ON_hotspot_script)
print("run_hotspot wifi is: "+str(run_hotspot))
print("path_reboot_bat wifi is: "+path_reboot_bat)
print("backup wifi is: "+backup_wifi)
print("restart net stack path wifi is: "+path_to_restart_netstack)
print("accept_captive_portal_docker_image_name wifi is: "+accept_captive_portal_docker_image_name)




if(os.path.isfile(path_to_turn_OFF_hotspot_script)):
    print("path_to_turn_OFF_hotspot_script file found.")

if(os.path.isfile(path_to_turn_ON_hotspot_script)):
    print("path_to_turn_ON_hotspot_script file found.")

if(os.path.isfile(path_reboot_bat)):
    print("path_reboot_bat file found.")

if(os.path.isfile(path_to_restart_netstack)):
    print("path_to_restart_netstack file found.")

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
        os.system("path_to_restart_netstack &")
        time.sleep(60)
        print(current_time,"accepting yee hong agreement...",file=open(date_today+output_name,"a"))
        os.system("docker run -ti --rm --network host "+accept_captive_portal_docker_image_name+" python3 ./temp/run_connect_yee_hong.py &")
        time.sleep(10)
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
        # reset_network_adapter(five_ghz_adapter_name=five_ghz_adapter_name)
        # if run_hotspot:
        #     turn_off_hotspot(path_to_turn_OFF_hotspot_script=path_to_turn_OFF_hotspot_script)
        # connect_to_network(five_ghz_adapter_name=five_ghz_adapter_name, ssid="YHCGuest", name="YHCGuest")
        # if run_hotspot:
        #     turn_on_hotspot(run_hotspot=run_hotspot,path_to_turn_ON_hotspot_script=path_to_turn_ON_hotspot_script)
        #if internet still fails, then try to accept the yee hong agreeement
        if(not check_internet_connection(url)):
            #reset network adapter before trying to reconnect to yee hong
            reset_network_adapter(five_ghz_adapter_name=five_ghz_adapter_name)
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
    