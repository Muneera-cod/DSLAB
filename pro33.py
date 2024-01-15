import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
# Load the Iris dataset
iris=load_iris()
x=iris.data
y=iris.target

x=x[:,2]
#Description
feature_name=iris.feature_names[2]
df = pd.DataFrame({feature_name: x, 'target': y})


print("Description:")
print(df.describe())
print("feature names:")
print(df.columns[0])
print("target names:")
print(df['target'].unique())
# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2)
# Reshape
x_train=np.array(x_train).reshape(-1,1)
y_train=np.array(y_train).reshape(-1,1)
x_test=np.array(x_test).reshape(-1,1)
# Linear Regression
lr = LinearRegression()
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)

print("Coefficient:",lr.coef_)
print("intercept: ",lr.intercept_)
# Evaluate linear regression performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Linear Regression Mean Squared Error: {mse:.2f}")
print(f"Linear Regression R-squared: {r2*100:.2f}")
# Plotting
plt.scatter(x_test, y_test, color='black', label='True values')
plt.plot(x_test, y_pred, color='blue', linewidth=3, label='Linear Regression')
plt.title('Linear Regression - Iris Dataset')
plt.show()