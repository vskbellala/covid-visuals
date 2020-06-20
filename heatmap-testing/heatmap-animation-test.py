import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

url = 'https://covidtracking.com/api/v1/states/daily.csv'
data = pd.read_csv(url, parse_dates=['date'], usecols=['date', 'state', 'positive'])
df = pd.DataFrame(data)
df = df[::-1]
# Reads data from CSV, outputs to DataFrame, and reverses order of the rows

df['date'] = df['date'].dt.strftime('%m/%d')
df['date'] = df['date'].astype('str')
# Reformats the date to month/day

fig = px.choropleth(df,
                    locationmode='USA-states',
                    locations='state',
                    animation_frame='date',
                    color='positive',
                    color_continuous_scale='Emrld',
                    range_color=(0, df['positive'].max()),
                    labels={'positive': 'Positive Cases',
                            'date': 'Date',
                            'state': 'State'}
                    )
# Builds and animates a choropleth(heatmap) map with COVID-19 positive cases overtime

fig.update_layout(
    title_text='COVID-19 Heatmap',
    geo=dict(
        scope='usa',
        projection=go.layout.geo.Projection(type='albers usa'),
        showlakes=True,
        lakecolor='rgb(255, 255, 255)')
)
# Updates the layout of the map to focus on the USA

fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 100
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 100
# Adjusts the time in between frames in the animation

fig.layout.sliders[0].currentvalue['prefix'] = 'Date: '
# Reformats the "Date" on the slider

fig.show()
# Opens the heatmap in a new tab
