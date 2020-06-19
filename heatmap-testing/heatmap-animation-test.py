import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

url = 'https://covidtracking.com/api/v1/states/daily.csv'
data = pd.read_csv(url, parse_dates=['date'], usecols=['date', 'state', 'positive'])
df = pd.DataFrame(data)
df = df[::-1]
df['date'] = df['date'].dt.strftime('%m/%d')
df['date'] = df['date'].astype('str')

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

fig.update_layout(
    title_text='COVID-19 Heatmap',
    geo=dict(
        scope='usa',
        projection=go.layout.geo.Projection(type='albers usa'),
        showlakes=True,
        lakecolor='rgb(255, 255, 255)')
)

fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 100
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 100

# Update layout and stuff with print(fig.layout)

# fig.data[0].update(hovertemplate='State: %{location}<br>Positive Cases: %{z}<br>Date: 01/22<extra></extra>')

fig.show()
