# -*- coding: utf-8 -*-
"""Titanic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dryF15VZKEDVntRzbPOMDuh6s8oNE59X
"""

#libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Importing Data"""

#import data
titanic_data = pd.read_csv('/content/titanic_train.csv')
titanic_data['Age'].head(10)

"""Checking Missing Values"""

titanic_data.isnull().sum()
#we can see from the results that we have three columns with missing values with different intensities

"""Handling Missing Values"""

#there are too many missing values in the cabin column
titanic_data = titanic_data.drop(columns='Cabin',axis=1)

#We can't delete the age column , so we need to work on it instead of dropping it
#replace the missing values in age column with mean value
titanic_data['Age'].fillna(titanic_data['Age'].mean(),inplace=True)

#Embarked column
#replace the missing values with mode value
titanic_data['Embarked'].fillna(titanic_data['Embarked'].mode()[0],inplace=True)

titanic_data.isnull().sum()

"""Data Analysis"""

#get some statistical measures about the data
titanic_data.describe()

# get the number of people survived 
titanic_data['Survived'].value_counts()

"""Data Visualization"""

sns.set()

#count plot for 'Survived' Column
sns.countplot(titanic_data['Survived'])

titanic_data['Sex'].value_counts()

#count plot for 'Sex' column
sns.countplot(titanic_data['Sex'])

#number of survivers with respect to gender
sns.countplot('Sex',hue='Survived',data=titanic_data)

#Pclass
sns.countplot(titanic_data['Pclass'])

#number of survivers with respect to pclass
sns.countplot('Pclass',hue='Survived',data=titanic_data)

"""Encoding categorical instances to Numerical"""

titanic_data['Sex'].value_counts()

titanic_data['Embarked'].value_counts()

#converting categorical columns
titanic_data.replace({'Sex':{'male':0,'female':1},'Embarked':{'S':0,'C':1,'Q':2}},inplace=True)
titanic_data.head()

"""Seperate features and Target

"""

X=titanic_data.drop(columns=['Name','PassengerId','Ticket','Survived'],axis=1)
Y = titanic_data['Survived']

"""Splitting data into train and test data

"""

X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=2)

print(X.shape,X_train.shape,X_test.shape)

"""Model Training using Logisitic regression"""

model = LogisticRegression()

#training the model with our data
model.fit(X_train,y_train)

"""Model Evaluation"""

X_train_predict = model.predict(X_train)
print(X_train_predict)

training_data_accuracy = accuracy_score(y_train,X_train_predict)
print("Accuracy score of Training Data is: ",training_data_accuracy)

"""Testing"""

X_test_predict = model.predict(X_test)
print(X_test_predict)

testing_data_accuracy = accuracy_score(y_test,X_test_predict)
print("Accuracy score of Training Data is: ",testing_data_accuracy)