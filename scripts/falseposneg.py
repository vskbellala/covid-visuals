import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd


url = 'https://api.covidtracking.com/v1/states/current.csv' # current COVID 19 data for US states

state_cases = pd.read_csv(url,parse_dates=['date'], usecols=['date','state','totalTestsPeopleViral','negative','positiveCasesViral','positive'])

