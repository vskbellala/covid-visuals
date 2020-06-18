import requests
import csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime

def df_filter (csv, cols = []):
	df = pd.DataFrame(csv)
	return df[cols]
	# returns dataframe with specified columns
def check_var(var):
	print(var)
	print(type(var))
	# for debugging variables


url = 'https://covidtracking.com/api/v1/us/daily.csv' # historical COVID 19 data for US
us_cases = pd.read_csv(url,parse_dates=['date']) 
# parse_dates formats the date column

df_us = df_filter(us_cases,['date','positive','death']) # extract only 3 specified columns
# df_us['date'] = df_us['date'].dt.strftime('%m/%d/%Y') # reformat date columns
print(df_us)
start_date = df_us.tail(1).iloc[0, 0] # extract earliest date from the data set
end_date = df_us.iloc[0,0] # extract latest date from the data set


#plot info deaths and pos cases
x = np.array(df_us['date'])#pd.date_range(start_date, end_date) # properly formats our x-axis range
y1 = np.array(df_us['positive']) #reverse list so older data is first
y2 = np.array(df_us['death']) #reverse list so older data is first




plt.plot(x,y1,label="Positive cases")
plt.plot(x,y2,label="Deaths")
plt.xlabel("date")
plt.ylabel("count")
plt.title('US corona cases')
plt.legend() # to display labels
plt.show()
