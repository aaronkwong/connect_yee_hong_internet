#when setting up a new pc navigate to this foler (universal_connection)

There should be several things in this directory:
-active_scripts directory: the directory containing subscripts or bat files needed for various functions
-identity directory: contains the identity files depending on where the script is run. MAke a new one and store it in this folder. Then copy one out (up one level) into universal_connection and rename it identity.py
-connect_yee_hong.bat: the bat file called by task scheduler which runs the whole show
-connect_yee_hong_universal.py: the python script with the main loop
-identity.py: called by "connect_yee_hong_universal.py" every run to give specific paths needed to run on the PC
-psshutdown.exe utility to call upon to restart PC when necessary
-test_functions.py: called by connect_yee_hong_universal.py every run before the main loop. Put any functions you want to test here. MAke sure everything is commented out once testing is done. Be careful testing restarts as this will put the PC into a boot loop.


Windows Specific Changes off the top of my head:
-disable windows update
-disable chrome update
-stop windows from opening wifi portal when connecting to yee hong
-set up task scheduler to run script every boot
-find windows interface device name 