import tkinter as tk
from tkinter import CENTER, SE, StringVar, ttk
import time
import json

time.sleep(2)

with open("input.txt",encoding="utf-8") as file_in:
    #list_file_r = str(file_in.read().splitlines())
    list_file_r = json.load(file_in)
 
total_1 = list_file_r[0][1]
total_2 = list_file_r[1][1]
total_3 = list_file_r[2][1]
total_4 = list_file_r[3][1]

ap1 = 0
ap2 = 0
ap3 = 0
ap4 = 0

bp1 = 0
bp2 = 0
bp3 = 0
bp4 = 0

cp1 = 0
cp2 = 0
cp3 = 0
cp4 = 0


root = tk.Tk()
root.title("promax1st")
root.geometry("440x1000")

a1d = StringVar()
a1d.set("P1: 0%")
a2d = StringVar()
a2d.set("P2: 0%")
a3d = StringVar()
a3d.set("P3: 0%")
a4d = StringVar()
a4d.set("P4: 0%")

b1d = StringVar()
b1d.set("P1: 0%")
b2d = StringVar()
b2d.set("P2: 0%")
b3d = StringVar()
b3d.set("P3: 0%")
b4d = StringVar()
b4d.set("P4: 0%")

c1d = StringVar()
c1d.set("P1: 0%")
c2d = StringVar()
c2d.set("P2: 0%")
c3d = StringVar()
c3d.set("P3: 0%")
c4d = StringVar()
c4d.set("P4: 0%")

per_1 = StringVar()
per_2 = StringVar()
per_3 = StringVar()
per_4 = StringVar()


l_fifo = tk.Label(text="-------FIFO-------",font=("Arial","18"))
l_fifo.pack(pady=5)


l_ap1 = tk.Label(textvariable=a1d,font=("Arial","11"))
l_ap1.pack()

p_ap1 = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
p_ap1.pack(pady=5)


l_ap2 = tk.Label(textvariable=a2d,font=("Arial","11"))
l_ap2.pack()

p_ap2 = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
p_ap2.pack(pady=5)


l_ap3 = tk.Label(textvariable=a3d,font=("Arial","11"))
l_ap3.pack()

p_ap3 = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
p_ap3.pack(pady=5)


l_ap4 = tk.Label(textvariable=a4d,font=("Arial","11"))
l_ap4.pack()

p_ap4 = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
p_ap4.pack(pady=5)


sl_1 = tk.Label(text="",font=("Arial","18"))
sl_1.pack(pady=10)


l_filo = tk.Label(text="-------FILO-------",font=("Arial","18"))
l_filo.pack(pady=5)

l_bp1 = tk.Label(textvariable=b1d,font=("Arial","11"))
l_bp1.pack()

p_bp1 = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
p_bp1.pack(pady=10)

l_bp2 = tk.Label(textvariable=b2d,font=("Arial","11"))
l_bp2.pack()

p_bp2 = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
p_bp2.pack(pady=10)

l_bp3 = tk.Label(textvariable=b3d,font=("Arial","11"))
l_bp3.pack()

p_bp3 = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
p_bp3.pack(pady=10)

l_bp4 = tk.Label(textvariable=b4d,font=("Arial","11"))
l_bp4.pack()

p_bp4 = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
p_bp4.pack(pady=10)


sl_2 = tk.Label(text="",font=("Arial","18"))
sl_2.pack(pady=10)


l_lot = tk.Label(text="-------LOT-------",font=("Arial","18"))
l_lot.pack(pady=5)

l_cp1 = tk.Label(textvariable=c1d,font=("Arial","11"))
l_cp1.pack()

p_cp1 = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
p_cp1.pack(pady=10)

l_cp2 = tk.Label(textvariable=c2d,font=("Arial","11"))
l_cp2.pack()

p_cp2 = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
p_cp2.pack(pady=10)

l_cp3 = tk.Label(textvariable=c3d,font=("Arial","11"))
l_cp3.pack()

p_cp3 = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
p_cp3.pack(pady=10)

l_cp4 = tk.Label(textvariable=c4d,font=("Arial","11"))
l_cp4.pack()

p_cp4 = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
p_cp4.pack(pady=10)


l_name = tk.Label(root,text="Alireza Mansoori",font=("Arial","18"))
#l_name.anchor('se')
l_name.place(rely=0.96,relx=0.01)





p_ap1.start()
p_ap2.start()
p_ap3.start()
p_ap4.start()
p_bp1.start()
p_bp2.start()
p_bp3.start()
p_bp4.start()
p_cp1.start()
p_cp2.start()
p_cp3.start()
p_cp4.start()




with open("result.txt") as in_file:
    for line in in_file:
        line = line.strip()
        print(line)
        time.sleep(0.05)  
        if line == "AP1":
            ap1 += 1
            a1d.set("P1: " + str(int((ap1/total_1)*100))+"%")
            p_ap1['value'] = (ap1/total_1)*100
            #print(int((ap1/total_1)*100))
        elif line == "AP2":
            ap2 += 1
            
            a2d.set("P2: " + str(int((ap2/total_2)*100))+"%")
            p_ap2['value'] = (ap2/total_2)*100

        elif line == "AP3":
            ap3 += 1
            a3d.set("P3: " + str(int((ap3/total_3)*100))+"%")
            p_ap3['value'] = (ap3/total_3)*100

        elif line == "AP4":
            ap4 += 1
            a4d.set("P4: " + str(int((ap4/total_4)*100))+"%")
            p_ap4['value'] = (ap4/total_4)*100

        elif line == "BP1":
            bp1 += 1
            b1d.set("P1: " + str(int((bp1/total_1)*100))+"%")
            p_bp1['value'] = (bp1/total_1)*100

        elif line == "BP2":
            bp2 += 1
            b2d.set("P2: " + str(int((bp2/total_2)*100))+"%")
            p_bp2['value'] = (bp2/total_2)*100
                                 
        elif line == "BP3":
            bp3 += 1
            b3d.set("P3: " + str(int((bp3/total_3)*100))+"%")
            p_bp3['value'] = (bp3/total_3)*100
                                 
        elif line == "BP4":
            bp4 += 1
            b4d.set("P4: " + str(int((bp4/total_4)*100))+"%")
            p_bp4['value'] = (bp4/total_4)*100


        elif line == "CP1":
            cp1 += 1
            c1d.set("P1: " + str(int((cp1/total_1)*100))+"%")
            p_cp1['value'] = (cp1/total_1)*100

        elif line == "CP2":
            cp2 += 1
            c2d.set("P2: " + str(int((cp2/total_2)*100))+"%")
            p_cp2['value'] = (cp2/total_2)*100
                                 
        elif line == "CP3":
            cp3 += 1
            c3d.set("P3: " + str(int((cp3/total_3)*100))+"%")
            p_cp3['value'] = (cp3/total_3)*100
                                 
        elif line == "CP4":
            cp4 += 1
            c4d.set("P4: " + str(int((cp4/total_4)*100))+"%")
            p_cp4['value'] = (cp4/total_4)*100


        root.update_idletasks()  

#time.sleep(20)
p_ap1.stop()
p_ap2.stop()
p_ap3.stop()
p_ap4.stop()
p_bp1.stop()
p_bp2.stop()
p_bp3.stop()
p_bp4.stop()
p_cp1.stop()
p_cp2.stop()
p_cp3.stop()
p_cp4.stop()

p_ap1['value'] = 100
p_ap2['value'] = 100
p_ap3['value'] = 100
p_ap4['value'] = 100
p_bp1['value'] = 100
p_bp2['value'] = 100
p_bp3['value'] = 100
p_bp4['value'] = 100
p_cp1['value'] = 100
p_cp2['value'] = 100
p_cp3['value'] = 100
p_cp4['value'] = 100
time.sleep(5)
exit()

root.mainloop()
