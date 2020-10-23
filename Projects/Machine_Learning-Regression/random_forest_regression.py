# Random Forest Regression-even this is a non-linear regression model
# Ensemble algorithms are more stable becasue any changes in your dataset could really impact one tree but for them to impact a forest of trees is much harder so therefore ensemble is much more powerful in that way

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Splitting the dataset into the Training set and Test set
"""from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)"""

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Random Forest Regression to the dataset
from sklearn.ensemble import RandomForestRegressor  #import the class and create an object of that class
regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)  #N-estimators-its the no of tress you want to have in your forest
regressor.fit(X, y)  #We are builiding a random forest with 10 trees,  fit(matrix of features,the dependent vector)

# Predicting a new result
y_pred = regressor.predict([[6.5]]) # So here if we give 6.6/6.75/6.9 it will return the same value which is 21K dollars(they are in the same range 6.5-7 so they all will return the same predicted value)
y_pred # here we got the predicted value as 167K dollars,so almost all the algorithms worked fine and have predicted in the range 150-170K dollars

# Visualising the Random Forest Regression results (higher resolution)
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (Random Forest Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()