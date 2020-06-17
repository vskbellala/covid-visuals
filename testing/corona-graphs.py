import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import gmaps
import gmaps.datasets


url = 'https://covidtracking.com/api/v1/us/daily.csv'
all_data = pd.read_csv(url, parse_dates=['date'], usecols=['date', 'death'])
df_data = pd.DataFrame(all_data)

dates = np.array(df_data['date'].dt.strftime('%m/%d'))[::-1]
deaths = np.array(df_data['death'])[::-1]

plt.plot(dates, deaths)
plt.xlabel('Time')
plt.ylabel('Deaths')


