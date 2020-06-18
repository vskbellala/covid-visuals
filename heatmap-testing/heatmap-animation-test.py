import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

url = 'https://covidtracking.com/api/v1/states/daily.csv'
data = pd.read_csv(url, usecols=['date', 'state', 'positive'])
df = pd.DataFrame(data)
df = df[::-1]

fig = px.choropleth(df,
                    animation_frame='date',
                    locationmode='USA-states',
                    locations='state',
                    color='positive',
                    color_continuous_scale='Emrld',
                    range_color=(0, df['positive'].max()),
                    hover_name='state'
                    )


fig.update_layout(
    title_text='COVID-19 Heatmap',
    geo=dict(
        scope='usa',
        projection=go.layout.geo.Projection(type='albers usa'),
        showlakes=True,
        lakecolor='rgb(255, 255, 255)')
)

fig.show()
