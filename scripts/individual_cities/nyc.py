import pandas as pd
import plotly.graph_objects as go


url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv' # historical COVID 19 data for US
us_cases = pd.read_csv(url, parse_dates=['date'], usecols=['date','county','deaths', 'cases', 'state'], converters={'cases':float}) 
# parse_dates formats the date column

df = pd.DataFrame(us_cases) # extract and reverse only 3 specified columns
#df['date'] = df['date'].dt.strftime('%B %d, %Y')
#df['date'] = df['date'].astype('str')

df_us = df.loc[(df['county'] == 'New York City') & (df['state'] == 'New York')]
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

        for k in range(0,len(df_us))] # Use list comprehension to populate each frame in the animation
)
fig1.add_trace(go.Scatter(x=df_us['date'], y=df_us['cases'],name="Cases", line=dict(color='#fc8403'))) # pos case graph
fig1.add_trace(go.Scatter(x=df_us['date'], y=df_us['deaths'],name="Deaths", line=dict(color='#cf1706'))) # death graph
fig1.update_traces(mode="lines") # change markers to a continuous line

'''
dateslist = []
numlist = []
textlist = []

link = ''
temp = pd.read_csv(link)
df_KOW = pd.DataFrame(temp)

for date in df_KOW['date']:
    dateslist.append(date)
    numlist.append(df_us.loc[df_us['date'] == date, 'cases'].item())
    textlist.append(df_KOW.loc[df_KOW['date'] == date, 'events'].item())
'''

dateslist = [df_us['date'][0], df_us['date'][56], df_us['date'][70], df_us['date'][100]]
numlist = [df_us['cases'][0], df_us['cases'][56], df_us['cases'][70], df_us['cases'][100]]
textlist = ['number 1', 'number 2', 'number 3']


# Adds in markers to the plot
k = 0
for i in range(0, len(fig1.frames)):
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
                    textposition='top left',
                    textfont_size=10,
                    marker=dict(
                        color='LightSkyBlue', 
                        size=14,
                        line=dict(
                            color='#fc8403', 
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
            textposition='top left',
            textfont_size=10,
            marker=dict(
                color='LightSkyBlue', 
                size=14,
                line=dict(
                    color='#fc8403', 
                    width=2))),)

# animation configuration parameters
a_opts = {"frame": {"duration": 0, "redraw": False}, "fromcurrent": True, "transition": {"duration": 300, "easing": "cubic-in"}}

fig1.update_layout(hovermode="x unified", # consistent hover
    xaxis=dict(linecolor='#e8e8e8', range=[df_us['date'].min(),df_us['date'].max()], autorange=False), #x axis range
    yaxis=dict(gridcolor='#e8e8e8',linecolor='#ffffff', range=[0, df_us['cases'].max()*1.25], autorange=False), # y axis range - use pos max x 1.25 to improve viewability, color of y-axis gridlines
    xaxis_title="Date",
    yaxis_title="Count",
    title="COVID-19 Cases & Deaths in New York City, NY",
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
            }# pause button
        ]
}])

fig1.layout.updatemenus[0].pad.r = 15
fig1.layout.updatemenus[0].pad.b = 15

fig1.write_html(file="../../docs/plots/nyc_lines.html",auto_play=True,full_html=False,include_plotlyjs='cdn',
    animation_opts=a_opts) # write figure to html



'''
animation_opts: dict or None (default None)
    dict of custom animation parameters to be passed to the function
    Plotly.animate in Plotly.js. See
    https://github.com/plotly/plotly.js/blob/master/src/plots/animation_attributes.js
    for available options. Has no effect if the figure does not contain
    frames, or auto_play is False.
'''