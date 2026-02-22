import matplotlib.pyplot as plt
import numpy as np

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


#plot 1:
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 3, 1)
plt.bar(x,y)
plt.title("filo")

#plot 2:
x = np.array(["A", "B", "C", "D"])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 3, 2)
plt.bar(x,y)
plt.title("fifo")

#plot3
x = np.array(["A", "B", "C", "D"])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 3, 3)
plt.bar(x,y)
plt.title("lot")


plt.show()
