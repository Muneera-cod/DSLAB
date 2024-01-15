import pandas as pd
dataframe = pd.read_csv('test.txt')
dataframe_customindex = dataframe.set_index('Name')
print(dataframe_customindex)
print()
dataframe = dataframe_customindex.reset_index()
print(dataframe)
# D=pd.DataFrame(dataframe,index=['x','y','v'])
# print(D)

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)