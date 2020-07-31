# The k constant is a fixed fraction of the infected group that will recover during any given day

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import math

# Not needed lol

# class DailyUS:
# 	def __init__(self,url='https://covidtracking.com/api/v1/us/daily.csv',parse_dates=['date'], usecols=['date', 'positive', 'recovered']):
# 		self.url = url
# 		self.parse_dates=parse_dates
# 		self.usecols=usecols
# 		self.data = pd.read_csv(self.url, parse_dates=self.parse_dates, usecols=self.usecols)
# 		self.df = pd.DataFrame(self.data)
# 	def dropNAN(self,col):
# 		df_drop = self.df[col]
# 		df_drop = np.asarray(df_drop.dropna().tolist()).reshape(-1, 1)
# 		return (df_drop,len(df_drop))
# 	def dropCut(self,col,length):
# 		df_cut = self.df[col].drop([0], axis=0)
# 		df_cut = np.asarray(df_cut.iloc[:length].tolist()).reshape(-1, 1)
# 		return df_cut
	
# 	@staticmethod
# 	def lin_reg(df_first,df_second):
# 		model = LinearRegression().fit(df_first, df_second)  # df_first * k = df_second
# 		return float(model.coef_[0][0])
# 	@staticmethod
# 	def average(df_first,df_second):
# 		temp = []
# 		for i in range(0, length):
# 		    temp.append(df_second[i] / df_first[i])  # k = df_second/df_first
# 		return float(sum(temp) / len(temp))


url = 'https://covidtracking.com/api/v1/us/daily.csv'
data = pd.read_csv(url, parse_dates=['date'], usecols=['date', 'positive', 'recovered'])
df = pd.DataFrame(data)
# Reads data from CSV and outputs to a DataFrame

df_recovered = df['recovered']  # Gets an array with the 'recovered' column only
df_recovered = np.asarray(df_recovered.dropna().tolist()).reshape(-1, 1)  # Drops NaN values, converts to numpy array, and reshapes
length = len(df_recovered)  # Gets the length of the new recovered array

df_positive = df['positive'].drop([0], axis=0)  # Drops the first entry of the 'positive' column to match with the 'recovered' entry of the next day
df_positive = np.asarray(df_positive.iloc[:length].tolist()).reshape(-1, 1)  # Converts to numpy array, cuts length of array to match that of df_recovered, and reshapes


def lin_reg():
    model = LinearRegression().fit(df_positive, df_recovered)  # df_positive * k = df_recovered
    return float(model.coef_[0][0])

# Finds the k constant using slope of linear regression model


def average():
    temp = []
    for i in range(0, length):
        temp.append(df_recovered[i] / df_positive[i])  # k = df_recovered/df_positive
    return float(sum(temp) / len(temp))

# Finds the k constant by averaging all daily k constants

def df_length():
	return length
