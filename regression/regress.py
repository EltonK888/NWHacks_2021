# pip install scikit-learn
# pip install statsmodels

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from scipy import stats
import math

# load data set
data = pd.read_csv('regression/regression-data.csv')

# split out training data based on 'type' column
training_data = data[data["type"] == "training"]

# training - explanatory and dependent variables
X_train = training_data[['numberPeople',
                         'hasTheme', 'soundLevel', 'averageAge']]
Y_train = training_data['funFactor']

# calculate regression output with sklearn
regr = LinearRegression()
regr.fit(X_train, Y_train)

# OLS Regression Results
X2_train = sm.add_constant(X_train)
est = sm.OLS(Y_train, X2_train)  # to add intercept as variable
est2 = est.fit()
print(est2.summary())

# create testing dataframe
testing_data = data[data["type"] == "testing"]

# testing - explanatory variables
X_test = testing_data[['numberPeople',
                       'hasTheme', 'soundLevel', 'averageAge']]

# calculate predicted fun factor (on testing data)
y_hats = regr.predict(X_test).round().astype(int)
testing_data['funFactor'] = y_hats
print(testing_data.head())
