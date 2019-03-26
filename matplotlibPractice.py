import matplotlib.pyplot as plt 
import numpy as np

x = np.linspace(0, 5, 11);
y = x ** 2;

fig,axes = plt.subplots(nrows=2, ncols=3)
for rowAx in axes :
    for ax in rowAx :
        ax.plot(x,y,'b')
        ax.set_xlabel('X Title')
        ax.set_ylabel('Y Title')
        ax.set_title('The Title')
plt.tight_layout()
plt.show()