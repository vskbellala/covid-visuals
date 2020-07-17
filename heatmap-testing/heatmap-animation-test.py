import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

url = 'https://covidtracking.com/api/v1/states/daily.csv'
data = pd.read_csv(url, parse_dates=['date'], usecols=['date', 'state', 'positive'])
df = pd.DataFrame(data)
df = df[::-1]
# Reads data from CSV, outputs to a DataFrame, and reverses order of the rows

df['date'] = df['date'].dt.strftime('%m/%d')
df['date'] = df['date'].astype('str')
# Reformats the date to month/day

fig = px.choropleth(df,
                    locationmode='USA-states',
                    locations='state',
                    animation_frame='date',
                    color='positive',
                    color_continuous_scale=px.colors.sequential.dense,
                    range_color=(0, df['positive'].max()),
                    labels={'positive': 'Positive Cases',
                            'date': 'Date',
                            'state': 'State'},
                    template='none',
                    hover_name='state',
                    hover_data={'date': True, 'positive': True, 'state': False}
                    )
# Builds and animates a choropleth(heatmap) map with COVID-19 positive cases over time

fig.update_layout(
    title=dict(
        text='COVID-19 US Heatmap',
        font=dict(
            size=24 # Font size for title
            )
        ),
    geo=dict(
        scope='usa',
        projection=go.layout.geo.Projection(type='albers usa'),
        showlakes=False,
        lakecolor='rgb(255, 255, 255)',
        bgcolor='#f8f9fb' # Background color of map
        ),
    hoverlabel=dict(
        bgcolor='#f8f9fb', # Background color of hoverlabel
        font_size=10, # Font size for hoverlabel
        font_family='Rockwell' # Font for hoverlabel
        ),
    coloraxis=dict(
        colorbar=dict(
            thicknessmode='pixels',
            thickness=12
            )
        ),
    font_family='Rockwell', # Font for plot
    paper_bgcolor='#f8f9fb', # Background color of whole thing
)
# Updates the layout of the heatmap

fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 100
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 100
# Adjusts the time in between frames in the animation

fig.layout.sliders[0].currentvalue['prefix'] = 'Date: '
# Reformats the "Date" on the slider

fig.update_traces(hovertemplate='<b>%{hovertext}</b><br>Date: %{customdata[0]}<br>Positive Cases: %{z}<extra></extra>')
for frame in fig.frames:
    frame['data'][0].hovertemplate = '<b>%{hovertext}</b><br>Date: %{customdata[0]}<br>Positive Cases: %{z}<extra></extra>'

fig.layout.updatemenus[0].showactive = True
fig.layout.sliders[0].tickcolor = '#f8f9fb' # Blends ticks in with background
fig.layout.coloraxis.colorbar.title.font.size=15

fig.show()
