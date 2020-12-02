import pandas as pd,numpy as np

class raceData():
	"""
	docstring for raceData
	
	All Data sourced from https://covidtracking.org

	Races covered:
	White
	Black
	Latinx
	Asian
	NHPI = native hawaiian and pacific islander
	AIAN = American Indian and Alaska Natives

	self.url: race dataset url
	self.cols: columns we are using (date, cases & deaths by race); note: ethnicity is not collected here
	self.data: reads CSV at url and filters cols with pandas
	self.df: generate pandas DataFrame for self.data
	- also has command to fix the data error for 'Cases_White'

	group_data: returns groupby object by 'Date'

	@staticmethod get_set: returns pandas Series with agg. values for specific columns cols on specific date date
	@staticmethod cr_key: simple replace string method to generate race labels
	
	"""
	def __init__(self):
		self.url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vS8SzaERcKJOD_EzrtCDK1dX1zkoMochlA9iHoHg_RSw3V8bkpfk1mpw4pfL5RdtSOyx_oScsUtyXyk/pub?gid=43720681&single=true&output=csv'
		self.cols =  ['Date','Cases_White', 'Cases_Black', 'Cases_LatinX', 'Cases_Asian', 'Cases_AIAN', 'Cases_NHPI', 'Cases_Multiracial', 'Cases_Other', 'Cases_Unknown', 'Deaths_White', 'Deaths_Black', 'Deaths_LatinX', 'Deaths_Asian', 'Deaths_AIAN', 'Deaths_NHPI', 'Deaths_Multiracial', 'Deaths_Other', 'Deaths_Unknown']
		self.data = pd.read_csv(self.url, usecols=self.cols,parse_dates=['Date'])
		self.df = pd.DataFrame(self.data)
		self.df['Cases_White'] = pd.to_numeric(self.df['Cases_White'].str.replace(',',''))
		# self.df['Cases_White'] = pd.to_numeric(self.df['Cases_White'])
	def group_data(self):
		self.group = self.df.groupby('Date')
		return self.group
	@staticmethod
	def get_set(gr_obj,date,cols):
		gr_new = gr_obj.get_group(date)[cols].agg(np.sum)
		return gr_new
	@staticmethod 
	def cr_key(fstring,flist):
		return [each.replace(fstring,'') for each in flist]