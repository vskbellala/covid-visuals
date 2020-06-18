import numpy as np
import pandas as pd
import plotly.express as px

url = "https://covidtracking.com/api/v1/states/current.csv"
all_data = pd.read_csv(url, usecols=['state', 'positive'])
df_data = pd.DataFrame(all_data)

states = np.array(df_data['state'])
cases = np.array(df_data['positive'])
scaled = []

old_min = np.min(cases)
old_max = np.max(cases)
new_min = 1
new_max = 3

for n in cases:
    new_value = ((n - old_min) / (old_max - old_min)) * (new_max - new_min) + new_min
    scaled.append(new_value)

fig = px.choropleth(locations=states, locationmode="USA-states", color=scaled, scope="usa")


fig.update_layout(title_text='COVID Heatmap')

fig.show()