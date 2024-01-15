import pandas as pd
company_data=pd.read_csv('27.txt')
print(company_data)
print()
company_data['profit']=company_data['profit'].apply(lambda x:x>0)
print(company_data)