import numpy as np
import pandas as pd
data={'A':np.random.rand(100),'B':np.random.randint(0,2,size=100),'c':np.random.choice(['X','Y','Z'],size=100)}
df=pd.DataFrame(data)
# print(data)
numerical_description=df.describe()
print("Numerical Description",numerical_description)
categorical_description=df.describe(include=['object'])
print("Categorical Description",categorical_description)