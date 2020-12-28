import pandas as pd
import plotly.graph_objects as go
import us

url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv' # historical COVID 19 data for US
us_cases = pd.read_csv(url, parse_dates=['date'], usecols=['date','county','deaths', 'cases', 'state'], converters={'cases':float}) 
# parse_dates formats the date column

df = pd.DataFrame(us_cases) # extract and reverse only 3 specified columns
df['date'] = df['date'].astype('str')

def abbr(s):
	'''
	Abbreviate the string s to first letter of each word IF it's multiple words
	'''
	if " " in s:
		l = s.split()
		l = list(map(lambda x: x[0],l))
		return "".join(l)
	return s

def plot(city, county, state, cases_color, deaths_color):
	'''
	Plot covid cases and deaths of the specified city county state combination.
	Also has custom cases and deaths line colors.
	'''
	plot_title = '{0}, {1}'.format(city,us.states.lookup(state).abbr)
	c_abbr = abbr(city).lower()
	event_sheet = '{}_sheet'.format(c_abbr)
	plot_file = '{}_lines'.format(c_abbr)
	# if state == 'Illinois':
	# 	plot_title = 'Chicago, IL'
	# 	event_sheet = 'chicago_sheet'
	# 	plot_file = 'chicago_lines'
	# elif state == 'Texas':
	# 	plot_title = 'Houston, TX'
	# 	event_sheet = 'houston_sheet'
	# 	plot_file = 'houston_lines'
	# elif state == 'Florida':
	# 	plot_title = 'Jacksonville, FL'
	# 	event_sheet = 'jacksonville_sheet'
	# 	plot_file = 'jacksonville_lines'
	# elif state == 'California':
	# 	plot_title = 'Los Angeles, CA'
	# 	event_sheet = 'la_sheet'
	# 	plot_file = 'la_lines'
	# elif state == 'New York':
	# 	plot_title = 'New York City, NY'
	# 	event_sheet = 'nyc_sheet'
	# 	plot_file = 'nyc_lines'
	# else:
	# 	plot_title = 'Seattle, WA'
	# 	event_sheet = 'seattle_sheet'
	# 	plot_file = 'seattle_lines'


	df_us = df.loc[(df['county'] == county) & (df['state'] == state)]
	df_us = df_us.reset_index(drop=True)

	fig1 = go.Figure(
	    frames=[go.Frame(
	        data=[go.Scatter(
	            x=df_us['date'].loc[0:k],
	            y=df_us['cases'].loc[0:k],
	            ),

	            go.Scatter(
	            x=df_us['date'].loc[0:k],
	            y=df_us['deaths'].loc[0:k],
	            )])

	        for k in range(len(df_us))] # Use list comprehension to populate each frame in the animation
	)

	fig1.add_trace(go.Scatter(x=df_us['date'], y=df_us['cases'],name="Cases", line=dict(color=cases_color))) # pos case graph
	fig1.add_trace(go.Scatter(x=df_us['date'], y=df_us['deaths'],name="Deaths", line=dict(color=deaths_color))) # death graph
	fig1.update_traces(mode="lines") # change markers to a continuous line


	dateslist = [df_us['date'][0]]
	numlist = [df_us['cases'][0]]
	textlist = []

	link = 'event_lists/' + event_sheet + '.csv'
	temp = pd.read_csv(link, parse_dates=['date'])
	df_events = pd.DataFrame(temp)
	df_events['date'] = df_events['date'].astype('str')

	for date in df_events['date']:
	    dateslist.append(date)
	    numlist.append(df_us.loc[df_us['date'] == date, 'cases'].item())
	    textlist.append(df_events.loc[df_events['date'] == date, 'events'].item())

	#dateslist = [df_us['date'][0], df_us['date'][56], df_us['date'][70], df_us['date'][100]]
	#numlist = [df_us['cases'][0], df_us['cases'][56], df_us['cases'][70], df_us['cases'][100]]
	#textlist = ['number 1', 'number 2', 'number 3']


	# Adds in markers to the plot
	k = 0
	for i in range(len(fig1.frames)):
	    date1 = fig1.frames[i]['data'][0].x[len(fig1.frames[i]['data'][0].x)-1]
	    if i == 0:
	        fig1.frames[i]['data'] += (go.Scatter(
	                x=dateslist[0:1], 
	                y=numlist[0:1], 
	                showlegend=False,
	                mode='none',
	                hoverinfo='skip'),)
	    else:
	        fig1.frames[i]['data'] += (go.Scatter(
	                    x=dateslist[1:k+1], 
	                    y=numlist[1:k+1], 
	                    showlegend=False,
	                    mode='markers+text',
	                    hoverinfo='skip',
	                    text=textlist[0:k],
	                    textposition='top center',
	                    textfont_size=10,
	                    marker=dict(
	                        color='LightSkyBlue', 
	                        size=10,
	                        line=dict(
	                            color=cases_color, 
	                            width=2))),)
	    if i != 0:
	        for date2 in dateslist:
	            if date1 == date2:
	                k += 1

	fig1.add_trace(go.Scatter(
	            x=dateslist, 
	            y=numlist, 
	            showlegend=False,
	            mode='markers+text', 
	            hoverinfo='skip',
	            text=textlist,
	            textposition='top center',
	            textfont_size=10,
	            marker=dict(
	                color='LightSkyBlue', 
	                size=10,
	                line=dict(
	                    color=cases_color, 
	                    width=2))),)


	# animation configuration parameters
	a_opts = {"frame": {"duration": 0, "redraw": False}, "fromcurrent": True, "transition": {"duration": 300, "easing": "cubic-in"}}

	fig1.update_layout(hovermode="x unified", # consistent hover
	    xaxis=dict(linecolor='#e8e8e8', range=[df_us['date'].min(),df_us['date'].max()], autorange=False), #x axis range
	    yaxis=dict(gridcolor='#e8e8e8',linecolor='#ffffff', range=[0, df_us['cases'].max()*1.25], autorange=False), # y axis range - use pos max x 1.25 to improve viewability, color of y-axis gridlines
	    xaxis_title="Date",
	    yaxis_title="Count",
	    title="COVID-19 Cases & Deaths in " + plot_title,
	    font_family='Rockwell', # Font for plot
	    paper_bgcolor='#ffffff', # Background color of whole thing
	    plot_bgcolor='#ffffff', # Background color of plot
	    hoverlabel=dict(
	        bgcolor='#ffffff', # Background color of hoverlabel
	        font_size=12, # Font size for hoverlabel
	        font_family='Rockwell' # Font for hoverlabel
	        ),
	    xaxis_showgrid=False,
	    updatemenus=[{'type':'buttons',"buttons": [ # note - buttons are in a drop down, don't know how to fix that
	            {
	                "args": [None, a_opts],
	                "label": "&#9654;",
	                "method": "animate"
	            }, # play button
	            {
	                "args": [[None], {"frame": {"duration": 0, "redraw": False},
	                                  "mode": "immediate",
	                                  "transition": {"duration": 0}}],
	                "label": "&#9724;",
	                "method": "animate"
	            } # pause button
	        ]
	}])

	fig1.layout.updatemenus[0].pad.r = 15
	fig1.layout.updatemenus[0].pad.b = 15

	fig1.write_html(file="../../docs/plots/" + plot_file + ".html",auto_play=True,full_html=False,include_plotlyjs='cdn',
	    animation_opts=a_opts) # write figure to html

	'''
	animation_opts: dict or None (default None)
	    dict of custom animation parameters to be passed to the function
	    Plotly.animate in Plotly.js. See
	    https://github.com/plotly/plotly.js/blob/master/src/plots/animation_attributes.js
	    for available options. Has no effect if the figure does not contain
	    frames, or auto_play is False.
	'''

plot('Chicago','Cook', 'Illinois', '#ff0d6a', '#b3295e')
plot('Houston','Harris', 'Texas', '#2adbcf', '#218a83')
plot('Jacksonville','Duval', 'Florida', '#fc03a5', '#7b03fc')
plot('Los Angeles', 'Los Angeles', 'California', '#a3cf06', '#5f7022')
plot('New York City', 'New York City', 'New York', '#fc8403', '#cf1706')
plot('Seattle', 'King', 'Washington', '#e61c73', '#8f2196')




