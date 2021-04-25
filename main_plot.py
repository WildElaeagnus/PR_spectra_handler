# Import pandas
from mpmath import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import file_browser
from file_browser import file_browser_

DEBUG = False

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

# plotting file
t = df.iloc[:, 0]
s = df.iloc[:, 1]

fig, ax = plt.subplots()

ax.plot(t, s)
ax.invert_xaxis() 
ax.set(xlabel='k, 1/cm', ylabel='I r. u.',
       title="Python_program_to_create.filename")
ax.grid()

def k2eV(arg):
	return 1.23984*arg/10000 

def eV2k(arg):
	return 1.23984*arg/10000 

secax = ax.secondary_xaxis('top', functions = (k2eV,  eV2k))
secax.set_xlabel('E, eV')

plt.show()

