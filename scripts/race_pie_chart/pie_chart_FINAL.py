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
names = raceData.cr_key('Cases_',case_vars)  # create array of race names

# initialize array of death count variables - IGNORES Unknown & Other
death_vars = ['Deaths_White', 'Deaths_Black', 'Deaths_LatinX', 'Deaths_Asian', 'Deaths_AIAN', 'Deaths_NHPI', 'Deaths_Multiracial']

# animation config params
a_opts = {"frame": {"duration": 500, "redraw": True},
                                "fromcurrent": True, "transition": {"duration": 100,
                                                                    "easing": "cubic-in"}}

def make_race_pie(stat_vars, n):
    '''Generates a pie chart based on the statistics indicated by stat_lst'''
    n = n.lower()
    title = n.capitalize()

    #Fill with frames for animation
    fig= go.Figure(frames=[go.Frame(
            data=[go.Pie(labels=names, sort=False, values=raceData.get_set(gr,x,stat_vars),title=x.strftime('%B %d, %Y'))]) for x,y in gr]
    )

    # Add stat trace
    fig.add_trace(go.Pie(labels=names,values=raceData.get_set(gr,rd.df['Date'].max(),stat_vars)))

    #Update trace styling
    fig.update_traces(hovertemplate=title+' : %{value}<extra></extra>', textinfo='label+percent', textfont_size=18,
                      marker=dict(line=dict(color='#000000')),automargin=False, sort=False, title=dict(font=dict(size=17)))

    #layout styling
    fig.update_layout(
        title="US COVID-19 {0} by Race".format(title),
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

    fig.write_html(file="../../docs/plots/{}_pie.html".format(n),auto_play=True,full_html=False,include_plotlyjs='cdn',
        animation_opts=a_opts) # write figure to html

# generate cases and deaths animated pie charts by race
make_race_pie(case_vars,"cases")
make_race_pie(death_vars,"deaths")