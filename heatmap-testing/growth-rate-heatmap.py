import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
from datetime import timedelta
import numpy as np


url = 'https://covidtracking.com/api/v1/states/daily.csv'
data = pd.read_csv(url, parse_dates=['date'], usecols=['date', 'positive'])
df = pd.DataFrame(data)

df = df[::-1]
# Reads data from CSV, outputs to a DataFrame, and reverses order of the rows

df['date'] = df['date'].dt.strftime('%m/%d')
df['date'] = df['date'].astype('str')
# Reformats the date to month/day

yesterday = (datetime.today() - timedelta(days=1)).strftime('%m/%d')
df = df[df.date != yesterday]
pos_cases = df['positive'].to_numpy()




secondary_data = pd.read_csv(url, usecols=['positiveIncrease'])
dfpi = pd.DataFrame(secondary_data)
dfpi = dfpi[::-1]
pos_inc = dfpi.to_numpy()


print(pos_inc/pos_cases)
