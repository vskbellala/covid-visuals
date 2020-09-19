import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import us

url = 'https://covidtracking.com/api/v1/states/daily.csv'
data = pd.read_csv(url, parse_dates=['date'], usecols=['date', 'state', 'death'])
df = pd.DataFrame(data)
df = df[::-1]
# Reads data from CSV, outputs to a DataFrame, and reverses order of the rows

df = df.fillna(0)

df['date'] = df['date'].dt.strftime('%B %d, %Y')
df['date'] = df['date'].astype('str')
# Reformats the date to month/day

url2 = 'https://www2.census.gov/programs-surveys/popest/tables/2010-2019/state/totals/nst-est2019-01.xlsx'
population_data = pd.read_excel(url2)
pop_df = pd.DataFrame(population_data)

pop_df = pop_df.iloc[8:59]

for i in range(0, len(df['state'])):
    state = str(us.states.lookup(str(df.iloc[i, 1])))
    for x in range(0, 51):
        st = str(pop_df.iloc[x, 0])
        pop = int(pop_df.iloc[x, 12])
        fullname = st.replace('.', '')
        if state == fullname:
            df.iloc[i, 2] = int((df.iloc[i, 2] / pop) * 1000000)


fig = px.choropleth(df,
                    locationmode='USA-states',
                    locations='state',
                    animation_frame='date',
                    color=np.log10(df['death']),
                    color_continuous_scale=px.colors.sequential.dense,
                    range_color=(0, 4),
                    labels={'death': 'Deaths Cases Per 1 Million People',
                            'date': 'Date',
                            'state': 'State'},
                    template='none',
                    hover_name='state',
                    hover_data={'date': True, 'death': True, 'state': False}
                    )
# Builds and animates a choropleth(heatmap) map with COVID-19 deaths cases over time

fig.update_layout(
    title=dict(
        text='COVID-19 US Deaths Heatmap',
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
                text='Deaths*'
                ),
            tickvals=[0, 1, 2, 3, 4],
            ticktext=[0, 10, 100, 1000, 10000]
            )
        ),
    font_family='Rockwell', # Font for plot
    paper_bgcolor='#ffffff', # Background color of whole thing
    annotations=[dict(
        text='*Per 1 Million People',
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

fig.update_traces(hovertemplate='<b>%{hovertext}</b><br>Date: %{customdata[0]}<br>Deaths*: %{customdata[1]}<extra></extra>')
for frame in fig.frames:
    frame['data'][0].hovertemplate = '<b>%{hovertext}</b><br>Date: %{customdata[0]}<br>Deaths*: %{customdata[1]}<extra></extra>'

fig.layout.updatemenus[0].showactive = True
fig.layout.sliders[0].tickcolor = '#ffffff'  # Blends ticks in with background
fig.layout.coloraxis.colorbar.title.font.size = 15

fig.write_html(file="../docs/plots/deaths_heat.html",auto_play=True,full_html=False,include_plotlyjs='cdn',
  animation_opts=a_opts

) # write figure to html
