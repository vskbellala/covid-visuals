import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import us


url = 'https://covidtracking.com/api/v1/states/daily.csv'
data = pd.read_csv(url, parse_dates=['date'],usecols=['date', 'state', 'positiveIncrease'])
df = pd.DataFrame(data)

# df = df[::-1].reset_index(drop=True)
df['date'] = df['date'].dt.strftime('%m/%d')
df['date'] = df['date'].astype('str')
# Reformats the date to month/day

cencsv = pd.read_csv('https://raw.githubusercontent.com/cphalpert/census-regions/master/us%20census%20bureau%20regions%20and%20divisions.csv',usecols=["State Code",'Region'])
cen = pd.DataFrame(cencsv)
regions = cen['Region'].unique().tolist() # list of us regions
regions.append("Other")

def get_region(abbr): # map function for getting region name for a state
	for tupl in cen.itertuples():
		if abbr == tupl[1]:
			return tupl[2]
	return "Other"


df['region'] = list(map(get_region,df['state'])) # populate 'region' col
df['state'] = [us.states.lookup(x).name for x in df['state']] # convert 2 letter values to full names



# doesn't work when played forwards
fig = px.bar(df, x='region', y="positiveIncrease", color="region",
  animation_frame="date", animation_group="state", range_y=[0,df['positiveIncrease'].max()*1.25],hover_name ='state')
fig.show()

# gr = df.group_by('date')
# fig = go.Figure(
# 	frames=[
# 	go.Bar(x=get_group)

# 	]
# )