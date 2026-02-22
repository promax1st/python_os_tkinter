import os
import time
mypass = "0"
os.system("rm -rf result.txt && touch result.txt")
os.system("echo '0' > status.txt")

files_done = 0

command_1 = "python3 filo1.py"
command_2 = "python3 fifo1.py"
command_3 = "python3 lot1.py"

os.popen(command_1)
os.popen(command_2)
os.popen(command_3)




#os.popen("sudo -S %s"%(command_1),"w").write(mypass)
#os.popen("sudo -S %s"%(command_2),"w").write(mypass)
#os.popen("sudo -S %s"%(command_3),"w").write(mypass)

time.sleep(0.2)


while files_done != 3:
    st = os.popen("cat status.txt").readlines()
   
   #print("******" + str(files_done))
    if "1" in str(st):
        files_done += 1
        print(files_done)
print("All 3 Files are done!!")
time.sleep(2.3)

os.system("python3 display_tk_V3.py")

#exit()


#promax1st
