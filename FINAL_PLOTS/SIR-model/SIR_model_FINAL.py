from diffeqsolver import *
import kfinder as kfi
import os, pandas as pd, numpy as np, plotly.express as px, plotly.graph_objects as go

k = kfi.average() # get k value
b = 0.5 # placeholder value for b
N = 329227746 # Approx. US Population as of 01/28/2020
days = kfi.length*2 # obtain num days from length of cut df column
pts = 1000 # higher = smoother
x0 = [1,1/N,0] #initialize s(0),i(0),r(0) values


t,s,i,r = solve(b,k,x0,days,pts) # generate list of datapoints for a plot

'''
# Run the following 3 commands to get graph based on population instead of fraction of pop.
# Do not forget to modify the trace titles to account for the different equations used.
s *= N
i *= N
r *= N
'''

'''
From diffeqsolver:

params: (b-constant, k-constant, [s(0), i(0), r(0)], # of days, # of datapoints)
return: [t values, s datapoints, i datapoints, r datapoints]
'''
# res = kfi.df_positive[::-1]

# Make Figure
fig1 = go.Figure(
	frames=[go.Frame(
        data=[go.Scatter(
            x=t[0:k],
            y=s[0:k],
            ),
            go.Scatter(
            x=t[0:k],
            y=i[0:k],
            ),
            go.Scatter(
            x=t[0:k],
            y=r[0:k],
            ),
            # go.Scatter(
            # x=list(range(kfi.length))[0:k],
            # y=res[0:k],
            # )
        ])

        for k in range(len(t))] # Use list comprehension to populate each frame in the animation
)
# Add individual plots 
fig1.add_trace(go.Scatter(x=t, y=s,name="s(t)")) # s(t) trace
fig1.add_trace(go.Scatter(x=t, y=i,name="i(t)")) # i(t) trace
fig1.add_trace(go.Scatter(x=t, y=r,name="r(t)")) # r(t) trace

fig1.update_traces(mode="lines") # change markers to a continuous line

# fig1.add_trace(go.Scatter(x=list(range(kfi.length)), y=res,name="Positive Cases",mode='markers')) # pos trace

fig1.update_layout(hovermode="x unified",
    xaxis=dict(linecolor='#f8f9fb'),
    yaxis=dict(gridcolor='#e8e8e8', linecolor='#f8f9fb'),
    xaxis_title="Days",
    yaxis_title="Fraction of US Population",
    title="COVID-19 SIR Model",
    font_family='Rockwell', # Font for plot
    paper_bgcolor='#f8f9fb', # Background color of whole thing
    plot_bgcolor='#f8f9fb', # Background color of plot
    hoverlabel=dict(
        bgcolor='#f8f9fb', # Background color of hoverlabel
        font_size=12, # Font size for hoverlabel
        font_family='Rockwell' # Font for hoverlabel
        ),
    xaxis_showgrid=False,
    updatemenus=[{'type':'buttons',"buttons": [ # Play Pause Buttons w/ smooth animation
            { # Modify frame and  transition duration/easing to change animation playbck
                "args": [None, {"frame": {"duration": 0, "redraw": False},
                                "fromcurrent": True, "transition": {"duration": 0,
                                                                    "easing": "cubic-in"}}],
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

# fig1.update_layout(xaxis_type="log")
fig1.show() # display figure