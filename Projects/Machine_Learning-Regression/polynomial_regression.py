# Polynomial Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values  #here if we put [:,1]-then its treated as a vector and not as a matrix so we put [:,1:2]- so 10 rows and 1 column
y = dataset.iloc[:, 2].values  #here salary,X is the level
#There is a non-linear relation between the level and salary so we use polynomial regression for this data
#Here there is only one dependent column and one independent column-level is independent and salary is depenedent,based on the level we try to predict the salary 

# Splitting the dataset into the Training set and Test set
"""from sklearn.cross_validation import train_test_split #we dont have much observations to split our data into training set and split test so thats why we dont split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)""" #it wont make much sense if we split the dataset

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""  #we use the same library as the simple,multiple linear regression so no need to do any feature scaling here

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)  # fit the regressor to the dataset-so its X,y and not X_train and y_train

# Fitting Polynomial Regression to the dataset
# Its like we are fitting a regression line for the 4th degree polynomial-this is nothing but polynomial regression
from sklearn.preprocessing import PolynomialFeatures  # everytime its the same import some class(PolynomialFeatures) from some library and then create an object of that class
poly_reg = PolynomialFeatures(degree = 4)  # First fit the 4th degree model to X-degree 4 so we will have sa x,x^2,x^3 till x^4(poly terms of the independent variable)
X_poly = poly_reg.fit_transform(X)  # fit and transform-so add the additional polynomial terms
poly_reg.fit(X_poly, y)  # poly_reg object automatically includes a column of 1 into the matrix(50 ones to the start)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)  # we build 2 models here-linear regression and polynomial regression just to compare both the models.

# Visualising the Linear Regression results
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg.predict(X), color = 'blue')  #x coordinates so X,y coordinates so the predicted salaries by the LinReg model
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()  #So in red we have the obs points and the predicted points in blue(the straight line)

# Visualising the Polynomial Regression results
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue') #we just cant put lin_reg_2 here because its of the class LinReg 
plt.title('Truth or Bluff (Polynomial Regression)') #here again the predicted values of the polynomial regression so poly_reg.fit_transform(X)
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()  #we get to know that the polynomial model fits much better than the linear regression model for the dataset

# Visualising the Polynomial Regression results (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))  #reshape the vector into the matrix,so 1 column and 90 levels,all the levels incremented by 0.1
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = 'blue') # This is nothing but the linear regression model but fitting with for a higher power function(which is nothing but Polynomial Regression)
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Predicting a new result with Linear Regression
lin_reg.predict(6.5)  #gives the corresponding salary for the level 6.5 in the linear model

# Predicting a new result with Polynomial Regression
lin_reg_2.predict(poly_reg.fit_transform(6.5)) #gives the corresponding salary for the level 6.5 in the polynomial model
# This gives more accurate results than the linear regression model-so this model is preferred here
# After seeing the visualization we can see that our curve has actually overfitted the model but it seems fine because it has given a decent prediction
