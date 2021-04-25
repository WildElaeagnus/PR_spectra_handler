# Import pandas
from mpmath import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import file_browser
from file_browser import file_browser_
from interactive_plot import *

DEBUG = True 

if (DEBUG):
	df = pd.read_csv("test_file.DPT",  delimiter='\t', header=None, names=None, index_col=None )
else:
	#get filename from file explorer
	file_browser_()

	# check if file path is choosen
	if file_browser.filename == None:
		exit()
	# reading csv file 
	df = pd.read_csv(file_browser.filename,  delimiter='\t', header=None, names=None, index_col=None )

# parsing file
x = df.iloc[:, 0]
y = df.iloc[:, 1]

#call main_plot(x, y) and grag all plots to interactive_graph

fig, ax = plt.subplots(nrows=1, ncols=2,)

ax[0].plot(x, y)
# ax.invert_xaxis() 
ax[0].set(xlabel='k, 1/cm', ylabel='I r. u.',
       title="Python_program_to_create.filename")
ax[0].grid()

def k2eV(arg):
	return 1.23984*arg/10000 

def eV2k(arg):
	return 1.23984*arg/10000 

secax = ax[0].secondary_xaxis('top', functions = (k2eV,  eV2k))
secax.set_xlabel('E, eV')

#plot 2

ax[1].plot(-x,y)
ax[1].set_ylabel('coherence')

#show window maimazed
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()

# interactive_plot()
plt.show()

