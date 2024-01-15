import numpy as np
import matplotlib.pyplot as plt
xpoints=np.array([1,2,6,18])
ypoints=np.array([3,10,12,20])
# plt.xlim(0,20)
# plt.ylim(0,30)
plt.plot(xpoints,ypoints,color='red',marker='.',markersize=12,markerfacecolor='green')
plt.show()