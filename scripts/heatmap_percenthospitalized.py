import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import us

url = 'https://api.covidtracking.com/v1/states/daily.csv'
data = pd.read_csv(url, parse_dates=['date'], usecols=['date', 'hospitalizedCurrently', 'state', 'positive'])
df = pd.DataFrame(data)
df = df[::-1]

df['date'] = df['date'].dt.strftime('%B %d, %Y')
df['date'] = df['date'].astype('str')

df['percent'] = df['hospitalizedCurrently']/df['positive']*100

df = df.fillna(0)

print(df)

fig = px.choropleth(df,
                    locationmode='USA-states',
                    locations='state',
                    animation_frame='date',
                    color=np.log10(df['percent']),
                    color_continuous_scale=px.colors.sequential.dense,
                    range_color=(0, 3),
                    labels={'percent': 'Percent of Positive Cases Hospitalized',
                            'date': 'Date',
                            'state': 'State'},
                    template='none',
                    hover_name='state',
                    hover_data={'date': True, 'percent': True, 'state': False}
                    )

fig.update_layout(
    title=dict(
        text='Percent of Positive Cases Hospitalized Per State',
        font=dict(
            size=24 # Font size for title
            )
        ),
    geo=dict(
        scope='usa',
        projection=go.layout.geo.Projection(type='albers usa'),
        showlakes=False,
        lakecolor='rgb(255, 255, 255)',
        bgcolor='#ffffff' # Background color of map
        ),
    hoverlabel=dict(
        bgcolor='#ffffff', # Background color of hoverlabel
        font_size=10, # Font size for hoverlabel
        font_family='Rockwell' # Font for hoverlabel
        ),
    coloraxis=dict(
        colorbar=dict(
            thicknessmode='pixels',
            thickness=12,
            title=dict(
                text='Percent*'
                ),
            tickvals=[0, 1, 2, 3],
            ticktext=[0, 10, 20, 30]
            )
        ),
    font_family='Rockwell', # Font for plot
    paper_bgcolor='#ffffff', # Background color of whole thing
    annotations=[dict(
        text='* Positive Cases Hospitalized Per State',
        showarrow=False,
        x=0.02,
        y=-0.07
        )]
)
# Updates the layout of the heatmap

fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 110
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 110
# Adjusts the time in between frames in the animation

# animation configuration parameters
a_opts = {"frame": {"duration": 110}, "transition": {"duration": 110}}


fig.layout.sliders[0].currentvalue['prefix'] = 'Date: '
# Reformats the "Date" on the slider

fig.update_traces(hovertemplate='<b>%{hovertext}</b><br>Date: %{customdata[0]}<br>Percent*: %{customdata[1]}<extra></extra>')
for frame in fig.frames:
    frame['data'][0].hovertemplate = '<b>%{hovertext}</b><br>Date: %{customdata[0]}<br>Percent*: %{customdata[1]}<extra></extra>'

fig.layout.updatemenus[0].showactive = True
fig.layout.sliders[0].tickcolor = '#ffffff'  # Blends ticks in with background
fig.layout.coloraxis.colorbar.title.font.size = 15

