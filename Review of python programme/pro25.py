import pandas as pd
import matplotlib.pyplot as plt
dataframe=pd.read_csv('abc.txt')
print(dataframe)
dataframes=dataframe.groupby('occ')['salary'].mean()
print(dataframes)
dataframe.plot()
# plt.plot(dataframe)
plt.show()
