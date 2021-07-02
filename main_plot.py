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



interactive_plot(x, y, 0, 1, 0.1)

# plt.show()

