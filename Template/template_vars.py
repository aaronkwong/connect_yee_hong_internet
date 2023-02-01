import os

#vars
working_directory='C:/Users/wong/My Drive/yee_hong_samsung'
five_ghz_adapter_name='Wi-Fi 4'
path_to_turn_OFF_hotspot_script='C://Users//wong//My Drive//yee_hong//active_scripts//turn_OFF_hotspot.ps1'
path_to_turn_ON_hotspot_script='C://Users//wong//My Drive//yee_hong//active_scripts//turn_on_hotspot.ps1'
run_hotspot=True
path_reboot_bat='C://Users//wong//My Drive//yee_hong//active_scripts//reboot.bat'

os.path.isdir(working_directory)
os.path.exists(path_to_turn_OFF_hotspot_script)
os.path.exists(path_to_turn_ON_hotspot_script)
os.path.exists(path_reboot_bat)