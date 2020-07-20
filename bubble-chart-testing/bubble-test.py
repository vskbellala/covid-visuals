import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
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

df['date'] = df['date'].dt.strftime('%B %d, %Y')
df['date'] = df['date'].astype('str')
# Reformats the date to month/day

df = df.fillna(0)
# Fills in NaN with 0

fig = px.scatter(df,
                x='positive',
                y='death',
                animation_frame='date',
                animation_group='state',
                size='totalTestResults',
                size_max=60,
                color='totalTestResults',
                color_continuous_scale=px.colors.sequential.dense,
                range_color=(df['totalTestResults'].min(), df['totalTestResults'].max()),
                log_x=True,
                log_y=True,
                range_x=[1000, 1000000],
                range_y=[10, 100000],
                hover_name='state',
                hover_data={'date': True, 'positive': True, 'death': True, 'totalTestResults': True, 'state': False},
                labels={'positive': 'Positive Tests',
                        'date': 'Date',
                        'state': 'State',
                        'totalTestResults': 'Total Tests',
                        'death': 'Deaths'}
                )
# Builds a bubble chart animation with a logarithmic scale

fig.update_layout(
    xaxis_title="Positive Cases",
    yaxis_title="Deaths",
    title=dict(
        text='US COVID-19 Tests',
        font=dict(
            size=24 # Font size for title
            )
        ),
    xaxis_showgrid=False,
    yaxis_showgrid=False,
    hoverlabel=dict(
        bgcolor='#f8f9fb', # Background color of hoverlabel
        font_size=10, # Font size for hoverlabel
        font_family='Rockwell' # Font for hoverlabel
        ),
    coloraxis=dict(
        colorbar=dict(
            thicknessmode='pixels',
            thickness=12,
            outlinecolor='#444',
            outlinewidth=1
            )
        ),
    font_family='Rockwell', # Font for plot
    paper_bgcolor='#f8f9fb', # Background color of whole thing
    plot_bgcolor='#f8f9fb', # Background color of plot
    xaxis=dict(
        showline=False
        ),
    yaxis=dict(
        showline=False
        )
    )
# Labels the graph
# Ideally all 3 colors should be the same and should match the color of the webslide

fig.layout.sliders[0].currentvalue['prefix'] = 'Date: '
# Reformats the "Date" on the slider

fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 150
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 150
# Adjusts the time in between frames in the animation

fig.update_traces(hovertemplate='<b>%{hovertext}</b><br>Date: %{customdata[0]}<br>Total Tests: %{marker.color}<br>Positive Tests: %{customdata[1]}<br>Deaths: %{customdata[2]}<extra></extra>')
for frame in fig.frames:
    frame['data'][0].hovertemplate = '<b>%{hovertext}</b><br>Date: %{customdata[0]}<br>Total Tests: %{marker.color}<br>Positive Tests: %{customdata[1]}<br>Deaths: %{customdata[2]}<extra></extra>'

fig.layout.updatemenus[0].showactive = True
fig.layout.sliders[0].tickcolor = '#f8f9fb' # Blends ticks in with background
fig.layout.coloraxis.colorbar.title.font.size=15

fig.show()
