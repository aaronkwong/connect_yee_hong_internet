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
#name of docker image that accepts the yee hong captive portal
accept_captive_portal_docker_image_name="wonga445/yh1:v1.0"