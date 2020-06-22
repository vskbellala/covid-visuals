import requests
import csv
import numpy as np
import pandas as pd
import datetime
import plotly.express as px
import plotly.graph_objects as go
from cfunctions import *

url = 'https://covidtracking.com/api/v1/us/daily.csv' # historical COVID 19 data for US
us_cases = pd.read_csv(url,parse_dates=['date'],converters={'positive':float}) 
# parse_dates formats the date column

df_us = df_filter(us_cases,['date','positive','death'],True) # extract and reverse only 3 specified columns
# df_us['date'] = df_us['date'].dt.strftime('%Y-%m-%d') # reformat date columns

fig1 = go.Figure(
	frames=[go.Frame(
        data=[go.Scatter(
            x=df_us['date'].loc[0:k],
            y=df_us['positive'].loc[0:k],
            ),
            go.Scatter(
            x=df_us['date'].loc[0:k],
            y=df_us['death'].loc[0:k],
            )])

        for k in range(0,len(df_us))] # Use list comprehension to populate each frame in the animation
)
fig1.add_trace(go.Scatter(x=df_us['date'], y=df_us['positive'],name="Positive Cases")) # pos case graph
fig1.add_trace(go.Scatter(x=df_us['date'], y=df_us['death'],name="Deaths")) # death graph
fig1.update_traces(mode="lines") # change markers to a continuous line
fig1.update_layout(hovermode="x unified", # consistent hover
    xaxis=dict(range=[df_us['date'].min(),df_us['date'].max()], autorange=False), #x axis range
    yaxis=dict(range=[0, df_us['positive'].max()*1.25], autorange=False), # y axis range - use pos max x 1.25 to improve viewability
    xaxis_title="Date",
    yaxis_title="Count",
    title="COVID-19 US Cases & Deaths",
    updatemenus=[{'type':'buttons',"buttons": [ # note - buttons are in a drop down, don't know how to fix that
            {
                "args": [None, {"frame": {"duration": 0, "redraw": False},
                                "fromcurrent": True, "transition": {"duration": 100,
                                                                    "easing": "cubic-in"}}],
                "label": "Play",
                "method": "animate"
            }, # play button
            {
                "args": [[None], {"frame": {"duration": 0, "redraw": False},
                                  "mode": "immediate",
                                  "transition": {"duration": 0}}],
                "label": "Pause",
                "method": "animate"
            }# pause button
        ]
}])
fig1.show() # display figure