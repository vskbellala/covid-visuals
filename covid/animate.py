import requests
import csv
import numpy as np
import pandas as pd
import datetime
import plotly.express as px

def df_filter (csv, cols = []):
	df = pd.DataFrame(csv)
	return df[cols]
	# returns dataframe with specified columns
def check_var(var):
	print(var)
	print(type(var))
	# for debugging variables
def reset_my_index(df):
  res = df[::-1].reset_index(drop=True)
  return(res)

url = 'https://covidtracking.com/api/v1/us/daily.csv' # historical COVID 19 data for US
us_cases = pd.read_csv(url,parse_dates=['date'],converters={'positive':float}) 
# parse_dates formats the date column

df_us = reset_my_index(df_filter(us_cases,['date','positive','death'])) # extract only 3 specified columns
# df_us['date'] = df_us['date'].dt.strftime('%Y-%m-%d') # reformat date columns

check_var(df_us['date'])

start_date = df_us.tail(1).iloc[0, 0] # extract earliest date from the data set
end_date = df_us.iloc[0,0] # extract latest date from the data set

fig = px.line(df_us, x="date", y=['positive','death'],title='COVID Positive and Deaths in US',labels={"value": "Count", "date": "Time",'variable':'Legend'},range_y=[0,3000000],range_x=[min(df_us['date']),max(df_us['date'])],animation_frame='date')
fig.show()