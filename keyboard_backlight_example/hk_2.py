import keyboard
import os 
not_in_list = ["left","right","up","down",",",".","alt","ctrl","shift","space","f","1","2","3","4","9","0","/","*","×","÷"]

while True:
    key_rs_1 = keyboard.read_key()
    key_rs_2 = key_rs_1
    
    active_window_id = os.popen("xprop -root | grep -i '_NET_ACTIVE_WINDOW(WINDOW)'").read()
    smplayer_window_id = os.popen("xprop -name smplayer | grep -i 'WM_CLIENT_LEADER(WINDOW)'").read()
    print(len(smplayer_window_id))
    if len(str(smplayer_window_id)) >= 10:
        smplayer_window_id = "  " + smplayer_window_id
    else:
        smplayer_window_id = " WM_CLIENT_LEADER(WINDOW): window id # 0x0000000"
    #total_smp = 0
    #smp = os.popen("ps -elf | grep -i '[s]mplayer'").read()
    #for sm in smp:
        #total_smp = total_smp + 1

    #print(active_window_id)
    #print(smplayer_window_id)
    #command_rs = "echo " + str(key_rs) + " > /home/promax1st/python/hk_time.txt"
    #os.system(command_rs)
    #print("total is: " + str(total_smp))
    #if total_smp <= 10:
    #print(active_window_id.index("0x"))
    #print(smplayer_window_id.index("0x"))
    #print(active_window_id)
    #print(smplayer_window_id)

    its_good = True
    i = active_window_id.index("0x")
    for i in range(i,46):
        if active_window_id[i] == smplayer_window_id[i]:
            its_good = True
        else:
            its_good = False
            break
        

    if its_good:
        if key_rs_1 not in not_in_list:
            my_file_1 = open("/home/promax1st/python/hk_time.txt","w")
            my_file_1.write(str(key_rs_1))
    else:
        my_file_1 = open("/home/promax1st/python/hk_time.txt","w")
        my_file_1.write(str(key_rs_1))

    if its_good:
        write_sm = " SM"
    else:
        write_sm = ""
    my_file_2 = open("/home/promax1st/python/hk_time_raw.txt","w")
    my_file_2.write(str(key_rs_2) + write_sm)
    print(key_rs_2)

    
#promax1st
