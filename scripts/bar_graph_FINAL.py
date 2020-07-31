import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
DC_STATEHOOD=1
import us


url = 'https://covidtracking.com/api/v1/states/daily.csv'
data = pd.read_csv(url, parse_dates=['date'], usecols=[
                   'date', 'state', 'positiveIncrease'])
df = pd.DataFrame(data)

last = df.loc[len(df)-1,'date']
sta = ['NY','AS','TX','MI'] # Force all bars to show with this dummy data
for st in sta:
	sdata = {'date': last,
	'state': st,
	'positiveIncrease': 0}
	df = df.append(sdata, ignore_index=True)



df = df[::-1].reset_index(drop=True)
df['date'] = df['date'].dt.strftime('%B %d, %Y')
df['date'] = df['date'].astype('str')
# Reformats the date to month/day

cencsv = pd.read_csv(
    'https://raw.githubusercontent.com/cphalpert/census-regions/master/us%20census%20bureau%20regions%20and%20divisions.csv', usecols=["State Code", 'Region'])
cen = pd.DataFrame(cencsv)
regions = cen['Region'].unique().tolist()  # list of us regions
regions.append("Other")


def get_region(abbr):  # map function for getting region name for a state
    for tupl in cen.itertuples():
        if abbr == tupl[1]:
            return tupl[2]
    return "Other"


df['region'] = list(map(get_region, df['state']))  # populate 'region' col
# convert 2 letter values to full names
df['state'] = [us.states.lookup(x).name for x in df['state']]


fig = px.bar(df,
        x='region',
        y="positiveIncrease",
        color="region",
        animation_frame="date",
        animation_group="state",
        hover_name='state',
        log_y=False,
        range_y=[0,50000],#This needs to be better than just hardcoded
        hover_data={
            'date': True,
            'positiveIncrease': True,
            'region': False
            }
        )

fig.update_layout(
    xaxis=dict(
        linecolor='#e8e8e8',
        autorange=False
        ),
    yaxis=dict(
        showline=False,
        gridcolor='#e8e8e8',
        autorange=False
        ),
    xaxis_showgrid=False,
    xaxis_title="Region",
    yaxis_title="New Cases",
    title="COVID-19 US Daily New Cases",
    font_family='Rockwell', # Font for plot
    paper_bgcolor='#f8f9fb', # Background color of whole thing
    plot_bgcolor='#f8f9fb', # Background color of plot
    hoverlabel=dict(
        bgcolor='#f8f9fb', # Background color of hoverlabel
        font_size=12, # Font size for hoverlabel
        font_family='Rockwell' # Font for hoverlabel
        ),
    )

fig.layout.update(showlegend=False)

#fig.update_traces(showlegend=False)

for frame in fig.frames:
    for data in frame['data']:
        data.marker.line.color = '#000000'
        data.marker.line.width = 1.2
        data.marker.opacity = 1
        data.hovertemplate = '<b>%{hovertext}</b><br>Date: %{customdata[0]}<br>New Cases: %{customdata[1]}<extra></extra>'



fig.layout.sliders[0].currentvalue['prefix'] = 'Date: '
# Reformats the "Date" on the slider

fig.layout.updatemenus[0].showactive = True
fig.layout.sliders[0].tickcolor = '#f8f9fb'  # Blends ticks in with background

fig.write_html(file="../plots/region_bar.html",auto_play=True,full_html=False,include_plotlyjs='cdn')
# write figure to html
