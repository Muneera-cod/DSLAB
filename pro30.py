import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report

from sklearn.naive_bayes import GaussianNB
data=pd.read_csv('iris.csv')
x=data.iloc[:,:4]
y=data.iloc[:,-1]



x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.20)
classifier=GaussianNB()
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)
# x,y=load_iris(return_X_y=True)
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.20)
# classifier=GaussianNB()
# classifier.fit(x_train,y_train)
# y_pred=classifier.predict(x_test)
confusion_matrix=confusion_matrix(y_test,y_pred)
print(f"Confusion matrix:\n{confusion_matrix}")
accuracy_score=accuracy_score(y_test,y_pred)
print(f"Accuracy Score:{accuracy_score*100:.2f}%")
report=classification_report(y_test,y_pred)
print(f"report:\n{report}")



