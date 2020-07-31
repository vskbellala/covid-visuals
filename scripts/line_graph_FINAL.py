import pandas as pd
import plotly.graph_objects as go

url = 'https://covidtracking.com/api/v1/us/daily.csv' # historical COVID 19 data for US
us_cases = pd.read_csv(url,parse_dates=['date'],usecols=['date','positive','death'],converters={'positive':float}) 
# parse_dates formats the date column

df = pd.DataFrame(us_cases) # extract and reverse only 3 specified columns
# df_us['date'] = df_us['date'].dt.strftime('%Y-%m-%d') # reformat date columns
df_us = df[::-1].reset_index(drop=True)


fig1 = go.Figure(
	frames=[go.Frame(
        data=[go.Scatter(
            x=df_us['date'].loc[0:k],
            y=df_us['positive'].loc[0:k],
            ),
            go.Scatter(
            x=df_us['date'].loc[0:k],
            y=df_us['death'].loc[0:k],
            )])

        for k in range(0,len(df_us))] # Use list comprehension to populate each frame in the animation
)
fig1.add_trace(go.Scatter(x=df_us['date'], y=df_us['positive'],name="Positive Cases", line=dict(color='#1abd7c'))) # pos case graph
fig1.add_trace(go.Scatter(x=df_us['date'], y=df_us['death'],name="Deaths", line=dict(color='#3fabe0'))) # death graph
fig1.update_traces(mode="lines") # change markers to a continuous line

# animation configuration parameters
a_opts = {"frame": {"duration": 0, "redraw": False}, "fromcurrent": True, "transition": {"duration": 100, "easing": "cubic-in"}}

fig1.update_layout(hovermode="x unified", # consistent hover
    xaxis=dict(linecolor='#f8f9fb', range=[df_us['date'].min(),df_us['date'].max()], autorange=False), #x axis range
    yaxis=dict(gridcolor='#e8e8e8',linecolor='#f8f9fb', range=[0, df_us['positive'].max()*1.25], autorange=False), # y axis range - use pos max x 1.25 to improve viewability, color of y-axis gridlines
    xaxis_title="Date",
    yaxis_title="Count",
    title="COVID-19 US Cases & Deaths",
    font_family='Rockwell', # Font for plot
    paper_bgcolor='#f8f9fb', # Background color of whole thing
    plot_bgcolor='#f8f9fb', # Background color of plot
    hoverlabel=dict(
        bgcolor='#f8f9fb', # Background color of hoverlabel
        font_size=12, # Font size for hoverlabel
        font_family='Rockwell' # Font for hoverlabel
        ),
    xaxis_showgrid=False,
    updatemenus=[{'type':'buttons',"buttons": [ # note - buttons are in a drop down, don't know how to fix that
            {
                "args": [None, a_opts],
                "label": "Play",
                "method": "animate"
            }, # play button
            {
                "args": [[None], {"frame": {"duration": 0, "redraw": False},
                                  "mode": "immediate",
                                  "transition": {"duration": 0}}],
                "label": "Pause",
                "method": "animate"
            }# pause button
        ]
}])

fig1.write_html(file="../plots/covid_lines.html",auto_play=True,full_html=False,include_plotlyjs='cdn',
    animation_opts=a_opts

) # write figure to html
'''
animation_opts: dict or None (default None)
    dict of custom animation parameters to be passed to the function
    Plotly.animate in Plotly.js. See
    https://github.com/plotly/plotly.js/blob/master/src/plots/animation_attributes.js
    for available options. Has no effect if the figure does not contain
    frames, or auto_play is False.
'''