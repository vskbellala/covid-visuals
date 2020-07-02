# The k constant is a fixed fraction of the infected group that will recover during any given day

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import math

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
