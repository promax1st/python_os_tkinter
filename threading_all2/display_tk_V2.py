from tkinter import *
from tkinter import ttk
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

label_fg = "#1a1b26"
label_bg = "#3d828a"



root = Tk()
root.title("promax1st")
root.geometry("1000x1000")
root.config(bg="#1a1b26")
fifo_frame = LabelFrame(root,text="FIFO",font=("Arial",16),bd=1,bg=label_bg,fg=label_fg)
fifo_frame.pack(side=TOP,padx=5,pady=20)
filo_frame = LabelFrame(root,text="FILO",font=("Arial",16),bd=1,bg=label_bg,fg=label_fg)
filo_frame.pack(padx=5,pady=20)
lot_frame = LabelFrame(root,text="LOT",font=("Arial",16),bd=1,bg=label_bg,fg=label_fg)
lot_frame.pack(padx=5,pady=20)

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


l_ap1 = Label(fifo_frame,textvariable=a1d,font=("Arial","11"),bg=label_bg)
l_ap1.pack()

p_ap1 = ttk.Progressbar(fifo_frame, orient="horizontal", length=300, mode="determinate")
p_ap1.pack(pady=10,padx=10)


l_ap2 = Label(fifo_frame,textvariable=a2d,font=("Arial","11"),bg=label_bg)
l_ap2.pack()

p_ap2 = ttk.Progressbar(fifo_frame, orient="horizontal", length=300, mode="determinate")
p_ap2.pack(pady=10)


l_ap3 = Label(fifo_frame,textvariable=a3d,font=("Arial","11"),bg=label_bg)
l_ap3.pack()

p_ap3 = ttk.Progressbar(fifo_frame, orient="horizontal", length=300, mode="determinate")
p_ap3.pack(pady=10)


l_ap4 = Label(fifo_frame,textvariable=a4d,font=("Arial","11"),bg=label_bg)
l_ap4.pack()

p_ap4 = ttk.Progressbar(fifo_frame, orient="horizontal", length=300, mode="determinate")
p_ap4.pack(pady=10)


l_bp1 = Label(filo_frame,textvariable=b1d,font=("Arial","11"),bg=label_bg)
l_bp1.pack()

p_bp1 = ttk.Progressbar(filo_frame, orient="horizontal", length=300, mode="determinate")
p_bp1.pack(pady=10,padx=10)

l_bp2 = Label(filo_frame,textvariable=b2d,font=("Arial","11"),bg=label_bg)
l_bp2.pack()

p_bp2 = ttk.Progressbar(filo_frame, orient="horizontal", length=300, mode="determinate")
p_bp2.pack(pady=10)

l_bp3 = Label(filo_frame,textvariable=b3d,font=("Arial","11"),bg=label_bg)
l_bp3.pack()

p_bp3 = ttk.Progressbar(filo_frame, orient="horizontal", length=300, mode="determinate")
p_bp3.pack(pady=10)

l_bp4 = Label(filo_frame,textvariable=b4d,font=("Arial","11"),bg=label_bg)
l_bp4.pack()

p_bp4 = ttk.Progressbar(filo_frame, orient="horizontal", length=300, mode="determinate")
p_bp4.pack(pady=10)



l_cp1 = Label(lot_frame,textvariable=c1d,font=("Arial","11"),bg=label_bg)
l_cp1.pack()

p_cp1 = ttk.Progressbar(lot_frame, orient="horizontal", length=300, mode="determinate")
p_cp1.pack(pady=10,padx=10)

l_cp2 = Label(lot_frame,textvariable=c2d,font=("Arial","11"),bg=label_bg)
l_cp2.pack()

p_cp2 = ttk.Progressbar(lot_frame, orient="horizontal", length=300, mode="determinate")
p_cp2.pack(pady=10)

l_cp3 = Label(lot_frame,textvariable=c3d,font=("Arial","11"),bg=label_bg)
l_cp3.pack()

p_cp3 = ttk.Progressbar(lot_frame, orient="horizontal", length=300, mode="determinate")
p_cp3.pack(pady=10)

l_cp4 = Label(lot_frame,textvariable=c4d,font=("Arial","11"),bg=label_bg)
l_cp4.pack()

p_cp4 = ttk.Progressbar(lot_frame, orient="horizontal", length=300, mode="determinate")
p_cp4.pack(pady=10)


l_name = Label(root,text="Alireza Mansoori",font=("Arial","18"),bg="#1a1b26",fg="#88ddff")
#l_name.anchor('se')
l_name.pack(side=BOTTOM)




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


p_ap1['value'] = 0
p_ap2['value'] = 0
p_ap3['value'] = 0
p_ap4['value'] = 0
p_bp1['value'] = 0
p_bp2['value'] = 0
p_bp3['value'] = 0
p_bp4['value'] = 0
p_cp1['value'] = 0
p_cp2['value'] = 0
p_cp3['value'] = 0
p_cp4['value'] = 0




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
        #fifo_frame.update_idletasks()
        #filo_frame.update_idletasks()
        #lot_frame.update_idletasks()

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



root.mainloop()
