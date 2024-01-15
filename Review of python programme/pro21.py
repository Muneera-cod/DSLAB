import pandas as pd
import matplotlib.pyplot as plt

datas=pd.read_csv('data.csv')
dataframecustomIndex=datas.set_index('Duration')
print(datas)

plt.plot(datas)
plt.show()


print(datas.head(4))
print(datas.info())

dataframesorted=datas.sort_values(by=['Pulse'])
print(dataframesorted)
print()
print()
print(dataframecustomIndex)