import pandas as pd
import matplotlib.pyplot as plt
emp_data = pd.read_csv('asd.txt')
company_data = pd.read_csv('zxc.txt')
print(emp_data)
print(emp_data)
print()
print(company_data)
print()
emp_data.plot()
plt.show()
dataframe = pd.merge(emp_data, company_data,how='inner',on='eid')
print(dataframe)