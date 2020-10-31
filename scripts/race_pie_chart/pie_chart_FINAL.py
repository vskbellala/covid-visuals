from racedata import raceData
import pandas as pd, plotly.graph_objects as go
from plotly.subplots import make_subplots

rd = raceData() # initialize data object
gr = rd.group_data() # generate agg. data



'''
Races covered:
White
Black
Latinx
Asian
NHPI = native hawaiian and pacific islander
AIAN = American Indian and Alaska Natives
'''
# initialize array of case count variables - IGNORES Unknown & Other
case_vars = ['Cases_White', 'Cases_Black', 'Cases_LatinX', 'Cases_Asian', 'Cases_AIAN', 'Cases_NHPI', 'Cases_Multiracial']
case_names = raceData.cr_key('Cases_',case_vars)  # create array of race names

# initialize array of death count variables - IGNORES Unknown & Other
death_vars = ['Deaths_White', 'Deaths_Black', 'Deaths_LatinX', 'Deaths_Asian', 'Deaths_AIAN', 'Deaths_NHPI', 'Deaths_Multiracial']
death_names = raceData.cr_key('Deaths_',death_vars) # create array of race names



# For subplots: fig = make_subpl

#Fill with frames for animation
fig= go.Figure(frames=[go.Frame(
        data=[go.Pie(labels=case_names, sort=False, values=raceData.get_set(gr,x,case_vars),title=x.strftime('%B %d, %Y'))]) for x,y in gr]
)

# Add cases trace
fig.add_trace(go.Pie(labels=case_names,values=raceData.get_set(gr,rd.df['Date'].max(),case_vars)))
# fig.add_trace(go.Pie(labels=case_names,values=raceData.get_set(gr,rd.df['Date'].max(),death_vars),title=dict(text="Deaths")))
# fig.add_trace(go.Pie(labels=death_names,values=rd.agg[death_vars],title=dict(text="Deaths")))

#Update trace styling
fig.update_traces(hovertemplate='Cases: %{value}<extra></extra>', textinfo='label+percent', textfont_size=18,
                  marker=dict(line=dict(color='#000000')),automargin=False, sort=False, title=dict(font=dict(size=17)))


# animation config params
a_opts = {"frame": {"duration": 500, "redraw": True},
                                "fromcurrent": True, "transition": {"duration": 100,
                                                                    "easing": "cubic-in"}}

#layout styling
fig.update_layout(
    title="US COVID-19 Cases by Race",
    updatemenus=[{'type':'buttons',"buttons": [ # Play Pause Buttons w/ smooth animation
            { # Modify frame and  transition duration/easing to change animation playbck
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
}],
    font_family='Rockwell', # Font for plot
    paper_bgcolor='#ffffff', # Background color of whole thing
    plot_bgcolor='#ffffff', # Background color of plot
    hoverlabel=dict(
        bgcolor='#ffffff', # Background color of hoverlabel
        font_size=12, # Font size for hoverlabel
        font_family='Rockwell' # Font for hoverlabel
        ))


fig.update_layout(margin = dict(b=500/2))

fig.update_traces(hole=0.4, marker=dict(line=dict(width=1.5)))
for frame in fig.frames:
    frame['data'][0].hole = 0.4
    frame['data'][0].marker.line.width = 1.5
    frame['data'][0].sort = False
    frame['data'][0].title.font.size = 17

#Show Fig
#fig.write_html(file="testing.html",auto_play=False,include_plotlyjs='cdn')

fig.layout.updatemenus[0].pad.r = 15
fig.layout.updatemenus[0].pad.b = 15

fig.write_html(file="../../docs/plots/cases_pie.html",auto_play=True,full_html=False,include_plotlyjs='cdn',
    animation_opts=a_opts

) # write figure to html