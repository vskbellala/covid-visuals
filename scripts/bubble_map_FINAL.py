import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import us

url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
data = pd.read_csv(url, parse_dates=['date'], usecols=['date', 'county', 'state', 'fips', 'cases'])
df = pd.DataFrame(data)
# Reads data from CSV, outputs to a DataFrame, and reverses order of the rows

df['date'] = df['date'].dt.strftime('%B %d, %Y')
df['date'] = df['date'].astype('str')
# Reformats the date to month/day


#NYC: 40.712776, -74.005974
#Kansas City: 39.099728, -94.578568
#Joplin: 37.084229, -94.513283


fdf = (pd.read_json('https://raw.githubusercontent.com/josh-byster/fips_lat_long/master/fips_map_minify.json')).transpose()

def get_lat(fips):
	try:
		return fdf.loc[fips,'lat']
	except:
		return np.nan
def get_long(fips):
	try:
		return fdf.loc[fips,'long']
	except:
		return np.nan


df['lat'] = list(map(get_lat, df['fips']))
df['long'] = list(map(get_long, df['fips']))

states = []
for state in df['state']:
	abb = str(us.states.lookup(str(state)).abbr)
	states.append(abb)
df['state_abbr'] = list(states)



for i in range(0, len(df['fips'])):
	if np.isnan(df['fips'].loc[i]):
		if df['county'].loc[i] == 'New York City':
			df['lat'].loc[i] = 40.712776
			df['long'].loc[i] = -74.005974
		elif df['county'].loc[i] == 'Kansas City':
			df['lat'].loc[i] = 39.099728
			df['long'].loc[i] = -94.578568
		elif df['county'].loc[i] == 'Joplin':
			df['lat'].loc[i] = 37.084229
			df['long'].loc[i] = -94.513283


df = df.fillna(0)
# Fills in NaN with 0


fig = px.scatter_geo(df,
					locationmode='USA-states',
					lat='lat',
					lon='long',
					animation_frame='date',
					color='cases',
					color_continuous_scale=px.colors.sequential.thermal,
					range_color=(0, df['cases'].max()),
					projection='albers usa',
					size='cases',
					size_max=60,
					labels={'county': 'County',
                            'date': 'Date',
                            'state_abbr': 'State',
                            'cases': 'Positive Cases'},
                    template='none',
                    hover_data={'county': True, 
                    		'state_abbr': True, 
                    		'cases': True, 
                    		'date': True,
                    		'lat': False,
                    		'long': False}
					)

fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 10
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 10
# Adjusts the time in between frames in the animation

# animation configuration parameters
a_opts = {"frame": {"duration": 10}, "transition": {"duration": 10}}

fig.update_layout(
    title=dict(
        text='COVID-19 Cases US Bubble Map by County',
        font=dict(
            size=24 # Font size for title
            )
        ),
    geo=dict(
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

fig.layout.sliders[0].currentvalue['prefix'] = 'Date: '
# Reformats the "Date" on the slider

fig.layout.updatemenus[0].showactive = True
fig.layout.sliders[0].tickcolor = '#f8f9fb' # Blends ticks in with background
fig.layout.coloraxis.colorbar.title.font.size=15


fig.update_traces(hovertemplate='<b>%{customdata[0]} County, %{customdata[1]}</b><br>Date: %{customdata[3]}<br>Cases: %{marker.color}<extra></extra>')
for frame in fig.frames:
    frame['data'][0].hovertemplate = '<b>%{customdata[0]} County, %{customdata[1]}</b><br>Date: %{customdata[3]}<br>Cases: %{marker.color}<extra></extra>'

fig.write_html(file="../plots/bubble_map.html",auto_play=True,full_html=False,include_plotlyjs='cdn',
    animation_opts=a_opts

) # write figure to html