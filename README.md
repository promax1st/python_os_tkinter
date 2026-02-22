using python os library to simulate running multiple algorithms simultaneously

download doc.pdf for more info about threading all2

```python3
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
```

EXAMPLE'S:

Keyboard Backlight:

in this example 
running_hk.py check's if hk1 and hk2 are running and if not running_hk.py uses os.popen() to run them

to check if they are running os and ps are used:
```python3
num_hk = os.popen("ps -elf | grep -i '[h]k_1.py'").read()
num_hk_2 = os.popen("ps -elf | grep -i '[h]k_2.py'").read()

```
ps is a linux command for managing and monitoring proccess



hk_1 is the timer and can change the keyboard backlight using os and light

```python3
time_now = time.time()

main code block


if float(time.time() - time_now) >= 0.1 :
            time_ls = time_ls + 1
            time_now = time.time()
```


```python3

os.popen("light -s sysfs/leds/platform::kbd_backlight -S 50")
if time_ls >= 20 :
    os.popen("light -s sysfs/leds/platform::kbd_backlight -S 0")

```



hk_2 is a listener that record keyboard input signals and can identify the active programm to not active 
a list of keyboard input 
```python3
not_in_list = ["left","right","up","down",",",".","alt","ctrl","shift","space","f","1","2","3","4","9","0","/","*","×","÷"]
```
for the video player 

```python3
active_window_id = os.popen("xprop -root | grep -i '_NET_ACTIVE_WINDOW(WINDOW)'").read()
smplayer_window_id = os.popen("xprop -name smplayer | grep -i 'WM_CLIENT_LEADER(WINDOW)'").read()

print(len(smplayer_window_id))
if len(str(smplayer_window_id)) >= 10:
    smplayer_window_id = "  " + smplayer_window_id
else:
    smplayer_window_id = " WM_CLIENT_LEADER(WINDOW): window id # 0x0000000"


 i = active_window_id.index("0x")
    for i in range(i,46):
        if active_window_id[i] == smplayer_window_id[i]:
            its_good = True
        else:
            its_good = False
            break


```
smplayer is the name of the video player i use in linux(fedora38)

if keyboard input get recorded hk_2 send that input to hk_1
using hk_time.txt as a temp file







Bluetooth example
   
bl_bat uses bluetoothctl to get the battery percentage of any connected divce

```python3
bl_tl = os.popen("bluetoothctl info | grep -i 'Percentage\|Missing device address argument' > /home/promax1st/python/bl_bat_info.txt")

```
bl_bat_info acts as a temp file and it is used to store the info about the divice


bl_1 checks if the bluetooth connectivity of the divice the connects it if its not been already connected and disconnects it if it was connected

```python3
#checking the status of the connection
bl_tl = os.popen("bluetoothctl info | grep 9C:19:C2:1B:5E:94").read()

#running one of this command depending on the connection status
command_1 = "bluetoothctl connect 9C:19:C2:1B:5E:94"
command_2 = "bluetoothctl disconnect 9C:19:C2:1B:5E:94"
```




File BackUp Example

this code makes a copy of the i3(linux window manager) config file 
and uses the date(pc loacal date liek[Sun Feb 22 10:16:29 PM +0330 2026]) as a name 
for the copied file

```python3
import os

mypass = "0"
command_2 = "date > /home/promax1st/python/i3/time.txt"
my_time = open("/home/promax1st/python/i3/time.txt","r").read()

print(command_2)

command_1 = "cp -r /home/promax1st/.config/i3/config /home/promax1st/python/i3/" + "i3_config\|" +str(my_time).replace(" ","\|")

print(command_1)

os.popen("sudo -S %s"%(command_2),"w").write(mypass)
os.popen("sudo -S %s"%(command_1),"w").write(mypass)

exit()
```
