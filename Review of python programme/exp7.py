import numpy as np
x=np.arange(21)
print(x)
x[(x>=9) & (x<=20)]*=-1
print(x)