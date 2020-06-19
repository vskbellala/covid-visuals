# *******DO NOT RUN THIS PROGRAM**********

from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
import plotly.express as px
import pandas as pd

url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
data = pd.read_csv(url, dtype={"fips": str})
df = pd.DataFrame(data)

fig = px.choropleth(df,
                    animation_frame='date',
                    geojson=counties,
                    locations='fips',
                    color='cases',
                    color_continuous_scale="Viridis",
                    range_color=(0, df['cases'].max()),
                    scope="usa"
                    )

fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()