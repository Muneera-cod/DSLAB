import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
from sklearn import linear_model
from sklearn.datasets import load_iris
x,y=load_iris(return_X_y=True)
x=x[:,0:2]
print(x)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.20)
classifier=linear_model.LinearRegression()
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)
mean_squared_error=mean_squared_error(y_test,y_pred)
print(f"Mean sqyared erro:{mean_squared_error}")
r2_score=r2_score(y_test,y_pred)
print(f"R2 Score:{r2_score}")
plt.scatter(x_test[:,0],y_test,color='black')
plt.plot(x_test[:,0],y_test,color='red')
plt.show()
