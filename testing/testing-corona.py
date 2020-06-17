import COVID19Py
import requests
import csv
import pandas as pd
# x = COVID19Py.COVID19()

# latest = x.getLocationByCountryCode("US")
# print(latest)


url = 'https://covidtracking.com/api/v1/states/il/daily.csv'
data = pd.read_csv(url,parse_dates=['date'],usecols=['date','positive','death'])
df = pd.DataFrame(data)
# print(df['date'])
# print(df.loc[1])
# print(df)
# for col in df:
# 	print(col)

def get_row(dframe, row):
	return dframe.loc[row]

def get_point(dframe,row,point):
	s = get_row(dframe,row)
	return s[point]

def find_point(dframe, date):
	for row in dframe.itertuples():
   		list_date = str(row[1])[:10]
   		if date == list_date:
   			tup_row = list(row)
   			print(type(tup_row[1]))
   			tup_row[1] = date
   			return tup_row

# print(get_row(df,1))
# print(type(str(get_point(df,1,'date'))))
list_check = find_point(df,input('date: '))
print(list_check)
print((type(list_check)))


