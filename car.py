# -*- coding: utf-8 -*-
"""Car.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TnXDu6J6ZpP5uTEBcg0mImF6Ypfid-0x
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
import seaborn as sns
from sklearn import metrics

data = pd.read_csv('/content/car data.xls')
data.head()

print(data.Fuel_Type.value_counts())

data.replace({'Petrol':'0','Diesel':'1','CNG':'2','Dealer':'0','Individual':'1',
              'Manual':'0','Automatic':'1'},inplace=True)

data.head()

X = data.drop(['Car_Name','Selling_Price'],axis=1)
Y = data['Selling_Price']

X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.1,random_state=2)

model = LinearRegression() 
model.fit(X_train,y_train)

predict = model.predict(X_train)
error = metrics.r2_score(y_train,predict)
print(error)

plt.scatter(y_train,predict)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted')
plt.show()

test= model.predict(X_test)
eval = metrics.r2_score(y_test,test)
print(eval)

plt.scatter(y_test,test)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted')
plt.show()

model = Lasso() 
model.fit(X_train,y_train)

predict = model.predict(X_train)
error = metrics.r2_score(y_train,predict)
print(error)

test= model.predict(X_test)
eval = metrics.r2_score(y_test,test)
print(eval)

plt.scatter(y_train,predict)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted')
plt.show()

plt.scatter(y_test,test)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted')
plt.show()