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
def filo1(filo1_l):
    palceholder_list1 = []
    for i in range(len(filo1_l)):
        for j in range(filo1_l[i][1]):
            palceholder_list1.append(filo1_l[i][0])
            
    #print(palceholder_list1)
    for i in range(len(palceholder_list1)):
        x = palceholder_list1.pop()
        global result_list
        result_list.append(x)
        #print("B"+x)
        time.sleep(0.01)
        command_result = str("echo 'B"+ x + "' >> result.txt")
        os.popen(command_result)

filo1(list_file_r)

os.popen("echo '1' > status.txt")

exit()
