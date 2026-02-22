import os 
import time

kk = ""
time_ls = 0
time_now = time.time()

while True:
    time.sleep(0.1)
    vr = False
    back = float(os.popen('light').read())
    #print(back)
    status = open("/home/promax1st/python/switch_hk.txt","r").read()
    #print(status)
    for sr in str(status):
        if sr == "n":
            vr = True
    #print(vr)
    if vr:
        file_textr = open("/home/promax1st/python/hk_time.txt","r")
        #kk = str(os.popen("cat /home/promax1st/python/hk_time.txt").read()).replace(" ","")
        kk = file_textr.read().replace(" ","")
    
        file_textw = open("/home/promax1st/python/hk_time.txt","w")
        #print(kk)
        #print(int(time_ls))
        #print(int(time.time() - time_now))
        for i in kk:
            if i == "E":
                kk = "E"
                break
            else:
                kk = "S"
    
        if kk == "S":
            if back <= 50 :
                os.popen("light -s sysfs/leds/platform::kbd_backlight -S 50")
            else:
                os.popen("light -s sysfs/leds/platform::kbd_backlight -S 100")

            #os.popen("echo E > /home/promax1st/python/hk_time.txt")
            file_textw.write("E")
            time_ls = 0
 
        if float(time.time() - time_now) >= 0.1 :
            time_ls = time_ls + 1
            time_now = time.time()
    
        if time_ls >= 20 :
            os.popen("light -s sysfs/leds/platform::kbd_backlight -S 0")


#promax1st


