import json
import os
import time
import random
with open("input.txt",encoding="utf-8") as file_in:
    #list_file_r = str(file_in.read().splitlines())
    list_file_r = json.load(file_in)
    #print(list_file_r)
    #list_file_r = "["+list_file_r[2:-2]+"]"
    #print(list_file_r)


result_list = []
def lot1(lot1_l):
    palceholder_list1 = []
    for i in range(len(lot1_l)):
        for j in range(lot1_l[i][1]):
            palceholder_list1.append(lot1_l[i][0])
            
    #print(palceholder_list1)
    #print(palceholder_list1)
    #rand_list = shuffle(palceholder_list1)

    for i in range(len(palceholder_list1)):
        x = palceholder_list1.pop(random.randint(0,len(palceholder_list1)-1))
        global result_list
        result_list.append(x)
        #print("C"+x)
        time.sleep(0.01)
        command_result = str("echo 'C"+ x + "' >> result.txt")
        os.popen(command_result)

lot1(list_file_r)


os.popen("echo '1' > status.txt")

exit()
