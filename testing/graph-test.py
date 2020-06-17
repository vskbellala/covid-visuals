# Goal: plot positive corona cases against date using matplotlib, pandas, etc. with data from covidtracking.com

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime

# Libraries imported: used for CSV manipulation and graphing

url = 'https://covidtracking.com/api/v1/states/il/daily.csv'
il_cases = pd.read_csv(url,parse_dates=['date'],usecols=['date','positive']) 
#parse_dates formates the date column, usecols filters it to only the date and positive cases
df_il = pd.DataFrame(il_cases)

# read csv and create dataframe for it

t = list(df_il['date'].dt.strftime('%m/%d'))[::-1]
print(t)
#reformat date from 2020-03-16 to 03/16 for simplicity
# this is where everything breaks lol
x = np.array(t)
y = list(df_il['positive'])[::-1] #reverse list so older data is first
print(x)
print(y)


plt.plot(x,y)
plt.xlabel("date")
plt.ylabel("count of positive cases")
plt.title('IL corona cases')
plt.show()