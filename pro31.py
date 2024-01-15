import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.datasets import load_iris
data=pd.read_csv('iris.csv')
x=data.iloc[:,2]

y=data.iloc[:,-1]
# print(k)
# x,y=load_iris(return_X_y=True)
# k=pd.DataFrame(x)
# w=pd.DataFrame(y)
# x=x[:,2]
# y=y[:,-1]
# print(k.describe())

# y=data.iloc[:,-1]
print(x)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.20)
x_train=np.array(x_train).reshape(-1,1)
y_train=np.array(y_train).reshape(-1,1)
x_test=np.array(x_test).reshape(-1,1)
Classifier=linear_model.LinearRegression()
Classifier.fit(x_train,y_train)
y_pred=Classifier.predict(x_test)
q=Classifier.coef_
w=Classifier.intercept_
print('coefient',q)
print('intersept',w)
mean_squared_error=mean_squared_error(y_test,y_pred)
print(mean_squared_error)
plt.scatter(x_test,y_test,color='black')
plt.plot(x_test,y_pred,color='red')
plt.show()

