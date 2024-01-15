import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
data=pd.read_csv('iris.csv')
print(data.head())
x=data.iloc[:,:4]
print(x.head())

y=data.iloc[:,-1]
print(y.head())
# print(y.to_string())
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.20)
print(x_train.head())
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.20)
classifier=KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)

accuracy_score=accuracy_score(y_test,y_pred)
print(f"Accuracy Score: {100*accuracy_score}%")

cm=confusion_matrix(y_test,y_pred)
print(f"Confussion Mmatrix:\n{cm}")


# classifier=KNeighborsClassifier(n_neighbors=5)
# classifier.fit(x_train,y_train)
# y_pred=classifier.predict(x_test)
# cm=confusion_matrix(y_test,y_pred)
# print(f"Confusion Matrix:\n{cm}")
#
# print()
# accuracy_score=accuracy_score(y_test,y_pred)
# print(f"Accuracy Score:{accuracy_score*100:.2f}%")
report=classification_report(y_test,y_pred)
print(f"classification report:\n{report}")