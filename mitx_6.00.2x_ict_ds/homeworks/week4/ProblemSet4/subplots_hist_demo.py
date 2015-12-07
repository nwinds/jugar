import matplotlib.pyplot as plt
import numpy as np

diff  = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
comp = ["foo", "bar", "baz"]
fig, ax = plt.subplots(3, 1)
for foo in range(0, len(diff)):
        x = [diff[foo]]
        name = comp
        color = ['0.1', '0.2', '0.3']
        label = ['1000000', '1200000', '1400000']
        y = zip(*x)
        pos = np.arange(len(x))
        width = 1. / (1 + len(x))
        for idx, (serie, color,label) in enumerate(zip(y, color,label)):
                ax[foo].bar(pos + idx * width, serie, width, color=color,label=label)
        fig.set_size_inches(28.5, 10.5)
        ax[foo].set_xticks(pos + 1.5*width)
        plt.ylabel(name[foo])
        ax[foo].set_xticklabels(comp)
        ax[foo].legend()
        plt.gray()
# fig.savefig("file" + '.jpg', bbox_inches='tight', pad_inches=0.5, dpi=100)
plt.show()
plt.clf()

import random
lst = [random.randrange(0,10) for i in range(100)]
data = np.array([lst, lst, lst, lst])
# data=np.random.random((4,10))
xaxes = ['x1','x2','x3','x4']
yaxes = ['y1','y2','y3','y4']
titles = ['t1','t2','t3','t4'] 

f,a = plt.subplots(2,2)
a = a.ravel()
for idx,ax in enumerate(a):
    ax.hist(data[idx])
    ax.set_title(titles[idx])
    ax.set_xlabel(xaxes[idx])
    ax.set_ylabel(yaxes[idx])
plt.tight_layout()
plt.show()