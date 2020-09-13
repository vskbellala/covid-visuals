import os
import sys
import datetime

'''
Messy script for automagically updating each plot
'''

pathA = 'scripts'
graphs = {'region_bar':"bar_graph_FINAL.py",
'bubble_chart':'bubble_chart_FINAL.py',
'bubble_map':'bubble_map_FINAL.py',
'deaths_heat':'heatmap_percapita_FINAL.py',
'covid_lines':'line_graph_FINAL.py',
'Statistics':'stats.py'
}

# loop for running python scripts without special dependencies
print('Navigating to working directory.')
sys.stdout.flush()
os.chdir('scripts/')

for graph in graphs:
	print("Running {0} python script".format(graph))
	sys.stdout.flush()
	os.system('py {0}'.format(graphs[graph]))
	print('Completed successfully. Moving to next script.')


# commands for special scripts :0
specg = {'race_pie_chart':'pie_chart_FINAL.py','SIR_model':'SIR_model_FINAL.py'}

for spec in specg:
	# Get to correct directory
	print('Navigating to directory {0}.'.format(spec))
	sys.stdout.flush()
	os.chdir('{0}/'.format(spec))

	#Run Script
	print('Running {0}'.format(specg[spec]))
	sys.stdout.flush()
	os.system('py {0}'.format(specg[spec]))

	#Reset directory for next loop
	print('Resetting directory.')
	sys.stdout.flush()
	os.chdir('../')

# Commands for city charts!

cityg = ['chicago','houston','jacksonville','LA','nyc','seattle']
citydir = 'individual_cities'

# Get to correct directory
print('Navigating to directory {0}.'.format(citydir))
sys.stdout.flush()
os.chdir('{0}/'.format(citydir))

for city in cityg:
	print("Running '{0}' python script".format(city))
	sys.stdout.flush()
	os.system('py {0}.py'.format(city))
	print('Completed successfully. Moving to next script.')


print('updating last_update.md') # used for automagically updating the date of last update (aka when this script is ran)
os.chdir('../../')
date = datetime.datetime.now()
f = open("docs/content/last_update.md", "w")
f.write('**Last updated [{0}](https://github.com/vskbellala/covid-visuals/commits/master).**'.format(date.strftime('%m/%d/%Y')))
f.close()

print('All scripts ran.')

