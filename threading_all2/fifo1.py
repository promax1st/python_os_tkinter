import json
import os
import time
with open("input.txt",encoding="utf-8") as file_in:
    #list_file_r = str(file_in.read().splitlines())
    list_file_r = json.load(file_in)
    #print(list_file_r)
    #list_file_r = "["+list_file_r[2:-2]+"]"
    #print(list_file_r)

result_list = []
def fifo1(fifo1_l):
    palceholder_list1 = []
    for i in range(len(fifo1_l)):
        for j in range(fifo1_l[i][1]):
            palceholder_list1.append(fifo1_l[i][0])
            
    #print(palceholder_list1)
    for i in range(len(palceholder_list1)):
        x = palceholder_list1.pop(0)
        global result_list
        result_list.append(x)
        #print("A"+x)
        time.sleep(0.01)
        command_result = str("echo 'A"+ x + "' >> result.txt")
        os.popen(command_result)

fifo1(list_file_r)
os.popen("echo '1' > status.txt")

exit()


