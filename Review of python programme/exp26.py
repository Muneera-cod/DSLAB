import pandas as pd
dataframe=pd.read_csv('bnm.txt')
print(dataframe)
dataframee=dataframe.dropna(inplace=True)
# dataframe=dataframe.fillna(0)
print()
print(dataframe)