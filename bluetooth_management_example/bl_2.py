import os
import time 
time.sleep(0.1)
mypass = "0"
command_2 = "systemctl restart bluetooth.service"
#os.system(command_2)
os.popen("sudo -S %s"%(command_2),"w").write(mypass)

exit()
