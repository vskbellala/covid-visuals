'''
Really broken don't use please

'''






from racedata import raceData
import pandas as pd, plotly.graph_objects as go

rd = raceData()
df_agg = rd.sum_up()
df_agg = df_agg.drop(labels='Date')
date = rd.get_date()
print(df_agg)

df = px.data.tips()
print(df)

# initialize array of case count variables - IGNORES Unknown & Other
case_vars = ['Cases_White', 'Cases_Black', 'Cases_LatinX', 'Cases_Asian', 'Cases_AIAN', 'Cases_NHPI', 'Cases_Multiracial']
case_names = raceData.cr_key('Cases_',case_vars)  # create array of race names

# initialize array of death count variables - IGNORES Unknown & Other
death_vars = ['Deaths_White', 'Deaths_Black', 'Deaths_LatinX', 'Deaths_Asian', 'Deaths_AIAN', 'Deaths_NHPI', 'Deaths_Multiracial']
death_names = raceData.cr_key('Deaths_',death_vars) # create array of race names

# Pop values retrieved from US Census: https://www.census.gov/quickfacts/fact/table/US/PST045219
N = 328239523
us_percent = dict(zip(case_names,[0.601,0.134,0.185,0.059,0.013,0.002,0.028]))
us_pop = dict(zip(case_names,[N*i for i in us_percent.values()]))

# df_dict = {'Race':case_names,'Population':us_pop,'Cases':df_agg[case_vars].values,'Deaths':df_agg[death_vars].values}
# df_temp = pd.DataFrame(df_dict,index=case_names)
# print(df_temp)
# print(df_temp.loc['White','Cases'])

# rep_race = []
# rep_var = []
# rep_val = []
# varval = ["Population",'Cases','Deaths']
# for name in case_names:
# 	for i in range(len(varval)):
# 		rep_race.append(name)
# 	for varv in varval:
# 		rep_var.append(varv)
# 		if varv == "Population":
# 			rep_val.append(df_temp.loc[name,varv]-(df_temp.loc[name,'Cases']+df_temp.loc[name,'Deaths']))
# 		else:
# 			rep_val.append(df_temp.loc[name,varv])

# print(len(rep_var)==len(rep_race)==len(rep_val))



# data = {'Race':rep_race,'Points':rep_var,'Values':rep_val}
# df_us = pd.DataFrame.from_dict(data)

# print(df_us)

# fig = px.sunburst(df_us, path=['Race', 'Points'], values='Values', branchvalues="total")
# fig.show()
print(type(df_agg['Deaths_AIAN']))
'''
ids = []
labels=[]
parents=[]
values=[]
varval = ['Cases','Deaths']
for name in case_names:
	ids.append(name)
	labels.append(name)
	parents.append('')
	values.append(us_pop[name])
	for varv in varval:
		ids.append(name+' - '+varv)
		labels.append(varv)
		if varv == 'Deaths':
			parents.append(name+' - '+'Cases')
			values.append(df_agg['Deaths_'+name])
		elif varv == 'Cases':
			parents.append(name)
			values.append(df_agg['Cases_'+name])


fig =go.Figure(go.Sunburst(ids=ids,labels=labels,parents=parents,values=values, branchvalues= "total"))
fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
fig.show()
'''
ids = []
labels=[]
parents=[]
values=[]
varval = ['Deaths']
for name in case_names:
	ids.append(name)
	labels.append(name)
	parents.append('')
	values.append(df_agg['Cases_'+name])
	for varv in varval:
		ids.append(name+' - '+varv)
		labels.append(varv)
		parents.append(name)
		values.append(df_agg['Deaths_'+name])

fig =go.Figure(go.Sunburst(ids=ids,labels=labels,parents=parents,values=values, branchvalues= "total"))
fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
fig.show()