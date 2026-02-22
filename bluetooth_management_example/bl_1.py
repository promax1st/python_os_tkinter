import os
import time 
time.sleep(0.1)
total_bl = 0
mypass = "0"
command_1 = "bluetoothctl connect 9C:19:C2:1B:5E:94"
command_2 = "bluetoothctl disconnect 9C:19:C2:1B:5E:94"

bl_tl = os.popen("bluetoothctl info | grep 9C:19:C2:1B:5E:94").read()


for bls in bl_tl:
    total_bl = total_bl +1

if total_bl <= 10: 
    os.system(command_1)
    #os.popen("sudo -S %s"%(command_1),"w").write(mypass)
else:
    os.system(command_2)
    #os.popen("sudo -S %s"%(command_2),"w").write(mypass)

exit()
