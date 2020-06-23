import requests
import csv
import numpy as np
import pandas as pd
import datetime
import plotly.express as px
import plotly.graph_objects as go
from cfunctions import *

url = 'https://covidtracking.com/api/v1/states/daily.csv' # historical COVID 19 data for all US states
state_cases = pd.read_csv(url) 
# parse_dates formats the date column

df_state = df_filter(state_cases,['date','state','positive','death','hospitalizedCumulative'],True)
# df_us['date'] = df_us['date'].dt.strftime('%Y-%m-%d') # reformat date columns
df_state['positive']=df_state['positive'].fillna(0)
df_state['s'] = df_state['state']
# df_state['death']=df_state['death'].fillna(0)
# df_state['hospitalizedCumulative']=df_state['hospitalizedCumulative'].fillna(0)
# df_temp = df_state['date'].unique()
# df_state.set_index([pd.Index(df_temp)])
# print(df_state.head())
df_state.sort_values(['date','state'],ascending=[True,False])
check_var(df_state)
fig = px.scatter(df_state, x="hospitalizedCumulative", y="death",size='positive', color='s',
	# range_x=[0,df_state['hospitalizedCumulative'].max()*1.25],
	range_y=[0,df_state['death'].max()*1.25], log_x = True,
	animation_frame='date',animation_group='state'
)

fig.show()

# fig = px.scatter(df_state, 
# 	x="hospitalizedCumulative", y="death",
# 	size='positive', color='state',
# 	hover_name='state',range_y=[0,df_state['death'].max()],range_x=[0,df_state['hospitalizedCumulative'].max()], size_max=60,
# 	labels={"death": "COVID-19 Deaths", "hospitalizedCumulative": "COVID-19 Hospitalizations",'state':'States','positive':'COVID-19 Positive Cases'},
# 	# hover_data = {'state':False},
# 	animation_frame = 'date',
# 	animation_group = 'state'
# )
# fig.show()


# url2 = 'https://covidtracking.com/api/v1/states/current.csv'
# data = pd.read_csv(url2,parse_dates=['date']) 
# df = df_filter(data,['date','state','positive','death','hospitalizedCumulative'],True)
# fig1 = go.Figure(data=go.Scatter(x=df['hospitalizedCumulative'], y=df['death'], mode='markers',
# 	marker=dict(size=df['positive'],sizemode='area',sizeref=100)))
# fig1.update_layout(
#     xaxis=dict(range=[0,df['hospitalizedCumulative'].max()*1.25], autorange=False), #x axis range
#     yaxis=dict(range=[-1000, df['death'].max()*1.25], autorange=False), # y axis range - use pos max x 1.25 to improve viewability
#     xaxis_title="Hospitalized",
#     yaxis_title="Deaths",
#     title="COVID-19 Hospitalized",
#     updatemenus=[{'type':'buttons',"buttons": [ # note - buttons are in a drop down, don't know how to fix that
#             {
#                 "args": [None, {"frame": {"duration": 0, "redraw": False},
#                                 "fromcurrent": True, "transition": {"duration": 100,
#                                                                     "easing": "cubic-in"}}],
#                 "label": "Play",
#                 "method": "animate"
#             }, # play button
#             {
#                 "args": [[None], {"frame": {"duration": 0, "redraw": False},
#                                   "mode": "immediate",
#                                   "transition": {"duration": 0}}],
#                 "label": "Pause",
#                 "method": "animate"
#             }# pause button
#         ]
# }])
# fig1.show()

# test = px.data.gapminder()
# check_var(test)
# px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
#            size="pop", color="continent", hover_name="country",
#            log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])