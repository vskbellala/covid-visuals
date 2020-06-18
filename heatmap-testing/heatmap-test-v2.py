import plotly.graph_objects as go
import numpy as np
import pandas as pd
df = pd.read_csv('https://covidtracking.com/api/v1/states/current.csv')

for col in df.columns:
    df[col] = df[col].astype(str)

df['text'] = df['state'] + '<br>' + \
    'Positive Cases: ' + df['positive'] + '<br>' + \
    'Deaths: ' + df['death']

fig = go.Figure(data=go.Choropleth(
    locations=df['state'],
    z=df['positive'].astype(int),
    locationmode='USA-states',
    colorscale='Viridis',
    autocolorscale=False,
    text=df['text'], # hover text
    marker_line_color='black', # line markers between states
    #marker_line_width=0,
    colorbar_title="Positive Cases"
))
print(df['text'])
fig.update_layout(
    title_text='COVID-19 Heatmap',
    geo = dict(
        scope='usa',
        projection=go.layout.geo.Projection(type = 'albers usa'),
        showlakes=True, # lakes
        lakecolor='rgb(255, 255, 255)'),
)

fig.show()