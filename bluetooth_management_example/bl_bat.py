import os

command_1 = "bluetoothctl connect 9C:19:C2:1B:5E:94"

bl_tl = os.popen("bluetoothctl info | grep -i 'Percentage\|Missing device address argument' > /home/promax1st/python/bl_bat_info.txt")

all_bat = open("/home/promax1st/python/bl_bat_info.txt","r").read()

if len(all_bat) != 0:
    if all_bat[0] != 'M' and len(all_bat) == 31:
        cor_bat = all_bat[all_bat.index("(")+1] + all_bat[all_bat.index("(")+2] + "%"
        print(cor_bat)
    elif all_bat[0] != 'M' and len(all_bat) == 32:
        print("100%")
    elif all_bat[0] != 'M' and len(all_bat) == 30:
        cor_bat = all_bat[all_bat.index("(")+1] + "%"
    else:
        print(":(")

else:
    print(":(")


