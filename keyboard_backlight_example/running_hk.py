import os
import time 
time.sleep(3)
total_hk = 0
mypass = "0"
num_hk = os.popen("ps -elf | grep -i '[h]k_1.py'").read()
command_1 = "python3 /home/promax1st/python/hk_2.py"
command_2 = "python3 /home/promax1st/python/hk_1.py"

total_hk_2 = 0
num_hk_2 = os.popen("ps -elf | grep -i '[h]k_2.py'").read()

for hkls in num_hk:
    total_hk = total_hk + 1

for hk_2ls in num_hk_2:
    total_hk_2 = total_hk_2 +1

if total_hk <= 10: 
    os.popen("sudo -S %s"%(command_2),"w").write(mypass)

if total_hk_2 <= 10:
    os.popen("sudo -S %s"%(command_1),"w").write(mypass)


#print(total_hk)
#print(total_hk_2)
exit()
