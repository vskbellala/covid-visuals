# Small script for writing latest COVID-19 Statistics in the US to the website
import pandas as pd

url = 'https://api.covidtracking.com/v1/us/current.csv'
data = pd.read_csv(url, usecols=['positive', 'death', 'totalTestResults'])
df = pd.DataFrame(data)

for col in df:
	df[col] = df.apply(lambda x: "{:,}".format(x[col]), axis=1)
	print('Opening {0}.md'.format(col))
	f = open("../docs/content/stats/{0}.md".format(col), "w")
	print('Writing latest statistic: {0}'.format(df[col][0]))
	f.write('{0}'.format(df[col][0]))
	print('Moving to next statistic')
	f.close()