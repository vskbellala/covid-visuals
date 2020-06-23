import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

url = 'https://covidtracking.com/api/v1/states/daily.csv'
data = pd.read_csv(url, parse_dates=['date'], usecols=['date', 'state', 'positive', 'death', 'totalTestResults'])
df_unfiltered = pd.DataFrame(data)
# Reads data from CSV and outputs to a DataFrame

start_date = '2020-03-14'
end_date = ((df_unfiltered['date'].iloc[0]).to_pydatetime()).strftime('%Y-%m-%d')
after_start_date = df_unfiltered['date'] >= start_date
before_end_date = df_unfiltered['date'] <= end_date
between_two_dates = after_start_date & before_end_date
df = df_unfiltered.loc[between_two_dates]
# Filters DataFrame based on date

df = df[::-1]
# Reverses order of rows in DataFrame

df['date'] = df['date'].dt.strftime('%m/%d')
df['date'] = df['date'].astype('str')
# Reformats the date to month/day

df = df.fillna(0)
# Fills in NaN with 0

fig = px.scatter(df,
                 x='totalTestResults',
                 y='death',
                 animation_frame='date',
                 animation_group='state',
                 size='positive',
                 size_max=60,
                 log_x=True,
                 log_y=True,
                 range_x=[1000, 10000000],
                 range_y=[10, 100000],
                 hover_name='state',
                 labels={'positive': 'Positive Cases',
                         'date': 'Date',
                         'state': 'State',
                         'totalTestResults': 'Total Tests Done',
                         'death': 'Deaths'}
                 )
# Builds a bubble chart animation with a logarithmic scale

fig.update_layout(xaxis_title="Total Tests Done",
                  yaxis_title="Total Deaths",
                  title="COVID-19 Bubble Chart")
# Labels the graph

fig.layout.sliders[0].currentvalue['prefix'] = 'Date: '
# Reformats the "Date" on the slider

fig.show()
