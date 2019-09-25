import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.ensemble import AdaBoostRegressor
dataset = pd.read_csv("C:/Users/APOORV/Desktop/Data Analytics/openiit.csv")
X = dataset.iloc[:, :]
X = X.drop('Customer',axis = 1)
X = X.drop('State',axis = 1)
X = X.drop('CustomerLifetimeValue',axis = 1)
X = X.drop('Education',axis = 1)
X = X.drop('EffectiveToDate',axis = 1)
X = X.drop('EmploymentStatus',axis = 1)
X = X.drop('Gender',axis = 1)
X = X.drop('MaritalStatus',axis = 1)
X = X.drop('PolicyType',axis = 1)
X = X.drop('RenewOfferType',axis = 1)
X = X.drop('VehicleSize',axis = 1)
X = X.drop('SalesChannel', axis = 1)
y = dataset.iloc[:, 2]
X.Response = X.Response.replace(to_replace = ['No','Yes'], value = [0,1])
X.Coverage = X.Coverage.replace(to_replace = ['Basic','Extended','Premium'], value = [0,1,2])
X.LocationCode = X.LocationCode.replace(to_replace = ['Rural','Suburban','Urban'], value = [0,1,2])
X.Policy = X.Policy.replace(to_replace = ['Personal L3','Personal L2','Personal L1','Corporate L3','Corporate L2','Corporate L1','Special L3','Special L2','Special L1'], value = [0,1,2,3,4,5,6,7,8])
X.VehicleClass = X.VehicleClass.replace(to_replace = ['Four-Door Car','Two-Door Car','SUV','Sports Car','Luxury SUV','Luxury Car'], value = [0,1,2,3,4,5])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2,random_state=0)
ada2 = AdaBoostRegressor()
ada2.fit(X_train,y_train)
y_pred = ada2.predict(X_test)
y_predtrain = ada2.predict(X_train)
r2_adaboost=r2_score(y_test,y_pred)
r2_adaboosttrain = r2_score(y_train, y_predtrain)
MAPE_value_adaboost =np.mean(np.abs((y_test - y_pred) / y_test)) * 100
adjr2_adaboost =1- ((1-r2_adaboost)*(9132)/(9119))
