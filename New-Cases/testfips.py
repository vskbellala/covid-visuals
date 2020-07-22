import pandas as pd, numpy as np, us

fdf = (pd.read_json('https://raw.githubusercontent.com/josh-byster/fips_lat_long/master/fips_map_minify.json')).transpose()
counties = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')
df = pd.DataFrame(counties)

'''
def get_lat(county,state,fips):
	if fips in fdf.index:
		return fdf.loc[fips,'lat']
	else:
		for tupl in fdf.itertuples():
			x = tupl[3]
			if x.rsplit(' ',1)[1] == "County":
				x = x.rsplit(' ',1)[0]
			if x.lower() == county.lower() and state == us.states.lookup(tupl[4]).name:
				return tupl[4]
	return np.nan
df['lat'] = list(map(get_lat, df['county'],df['state'],df['fips']))
'''
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


print(df)