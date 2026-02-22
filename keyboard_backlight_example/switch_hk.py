import os

status = open("/home/promax1st/python/switch_hk.txt","r").read()
w_rs = open("/home/promax1st/python/switch_hk.txt","w")

if str(status) == "on":
    w_rs.write("off")
    os.system("notify-send 'keylight off'")
else:
    w_rs.write("on")
    os.system("notify-send 'keylight on'")

