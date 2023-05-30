import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x=[0,1,2,3,4]
y=[0,2,4,6,8]


plt.title("Our first graph",fontdict={'fontname':"Comic Sans MS",'fontsize':20})
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.xticks([0,1,2,3,4,])
plt.yticks([0,2,4,6,7,10,12,14])


plt.plot(x,y,label='2X')
plt.legend()
plt.show()