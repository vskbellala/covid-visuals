# set of functions i use when i make my dataframes
import pandas as pd

def check_var(var):
	print(var)
	print(type(var))
	# for debugging variables
def reset_my_index(df):
  res = df[::-1].reset_index(drop=True)
  return(res)
  	# for resetting index after reversing a dataset
def df_filter (data, cols = [],reset_index = False):
	df = pd.DataFrame(data)
	df_new = df[cols]
	if reset_index:
		return reset_my_index(df_new)
	else:
		return df_new
	# returns dataframe with specified columns
	# no need to use 'usecols' in read_csv()