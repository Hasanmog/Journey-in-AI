# -*- coding: utf-8 -*-
"""Exploring_Classification_Algorithms.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NMifgZtMLGTyTFbGXCscBomeG6b4NCJe
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.metrics import classification_report

#social media marketing
data = pd.read_csv('/content/social.csv')
data.head()

data.shape

sns.histplot(data , x = 'Age' ,hue = 'Purchased')
# we Can see that the target audience is above 45 years old

sns.histplot(data , x='EstimatedSalary' , hue ='Purchased')
# The target audience are those above 45 years and have a salary above 90,000 inclusive.

X = np.array(data[['Age','EstimatedSalary']])
y = np.array(data['Purchased'])

from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test = train_test_split(X ,y , test_size = 0.1 , 
                                                       random_state = 42)
y_test = y_test.reshape(-1,1)
print(y_test)

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm

dt_1 = DecisionTreeClassifier()
log_1 = LogisticRegression()
nb_1 = BernoulliNB()
kn_1= KNeighborsClassifier()

dt = dt_1.fit(X_train , y_train)
log = log_1.fit(X_train , y_train)
nb = nb_1.fit(X_train , y_train)
kn = kn_1.fit(X_train , y_train)

dt_test = dt.predict(X_test)
log_test = log.predict(X_test)
nb_test = nb.predict(X_test)
kn_test = kn.predict(X_test)

print(classification_report(y_test,dt_test))

print(classification_report(y_test,log_test))

print(classification_report(y_test,nb_test))

print(classification_report(y_test,kn_test))