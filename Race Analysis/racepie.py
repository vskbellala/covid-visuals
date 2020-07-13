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



# For subplots: fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])

#Fill with frames for animation
fig= go.Figure(frames=[go.Frame(
        data=[go.Pie(labels=case_names,values=raceData.get_set(gr,x,case_vars),title=x.strftime('%B %d, %Y'))]) for x,y in gr]
)

# Add cases trace
fig.add_trace(go.Pie(labels=case_names,values=raceData.get_set(gr,rd.df['Date'].max(),case_vars)))
# fig.add_trace(go.Pie(labels=case_names,values=raceData.get_set(gr,rd.df['Date'].max(),death_vars),title=dict(text="Deaths")))
# fig.add_trace(go.Pie(labels=death_names,values=rd.agg[death_vars],title=dict(text="Deaths")))

#Update trace styling
fig.update_traces(hoverinfo='value', textinfo='label+percent', textfont_size=18,
                  marker=dict(line=dict(color='#000000', width=2)),automargin=False

)

#layout styling
fig.update_layout(
    title="US COVID-19 Cases by Race",
    updatemenus=[{'type':'buttons',"buttons": [ # Play Pause Buttons w/ smooth animation
            { # Modify frame and  transition duration/easing to change animation playbck
                "args": [None, {"frame": {"duration": 500, "redraw": True},
                                "fromcurrent": True, "transition": {"duration": 100,
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
fig.update_layout(margin = dict(b=500/2))

#Show Fig
fig.show()






# Create pie chart using plotly express
# Uses current date which was defined earlier in title
# currently set to generate a DEATH graph; change 'death_vars' & 'death_names' to case variables to get case graph
# fig = px.pie(rd.agg, values=rd.agg[case_vars], names=case_names,title='COVID-19 US Deaths by Race as of '+date)

# #update info displayed
# fig.update_traces(textposition='inside', textinfo='percent+label')

# #change hover style
# fig.update_layout(
#     hoverlabel=dict(
#         bgcolor="white", 
#         font_size=16,
#     )
# )
# fig.show()