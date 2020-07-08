import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime

url = 'https://covidtracking.com/api/v1/states/daily.csv'
data = pd.read_csv(url, parse_dates=['date'], usecols=['date', 'state', 'positive', 'negative', 'totalTestResults'])
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
                x='positive',
                y='negative',
                animation_frame='date',
                animation_group='state',
                size='totalTestResults',
                size_max=60,
                color='totalTestResults',
                color_continuous_scale=px.colors.sequential.haline,
                range_color=(df['totalTestResults'].min(), df['totalTestResults'].max()),
                log_x=True,
                log_y=True,
                range_x=[1000, 1000000],
                range_y=[1000, 100000000],
                hover_name='state',
                labels={'positive': 'Positive Cases',
                        'date': 'Date',
                        'state': 'State',
                        'totalTestResults': 'Total Tests Done',
                        'negative': 'Negative Cases'}
                )
# Builds a bubble chart animation with a logarithmic scale

fig.update_layout(xaxis_title="Positive Cases",
                  yaxis_title="Negative Cases",
                  title="U.S. COVID-19 Tests",
                  xaxis_showgrid=False,
                  yaxis_showgrid=False)
# Labels the graph

fig.layout.sliders[0].currentvalue['prefix'] = 'Date: '
# Reformats the "Date" on the slider

fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 150
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 150
# Adjusts the time in between frames in the animation

fig.show()
