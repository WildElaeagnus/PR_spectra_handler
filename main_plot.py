# PR specta handler v1.0.0
# Import some libs
from mpmath import *
# import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt

# import code from other files
from file_browser_class import *
from interactive_plot import *

# DEBUG = True 
DEBUG = False

if (DEBUG):
	df = pd.read_csv("test_file.DPT",  delimiter='\t', header=None, names=None, index_col=None )
else:
	#get filename from file explorer
	flb = file_browser_class_()
	flb.file_browser_()
	# check if file path is choosen
	if flb.filename is None:
		exit()
	# reading csv file 
	df = pd.read_csv(flb.filename,  delimiter='\t', header=None, names=None, index_col=None )

# parsing file
x = df.iloc[:, 0]
x = x.to_numpy()
# y = df.iloc[::-1, 1].reset_index(drop=True)
y = df.iloc[:, 1]
y = y.to_numpy()

if (DEBUG):
	print(size(y))
	print(size(x))
	# print((max(x)-min(x)+1/size(x)))
	print("min x: "+str(min(x)))
	print("max x: "+str(max(x)))
	print("min y: "+str(min(y)))
	print("max y: "+str(max(y)))

print((max(y)-min(y))/2)
step = (max(x) - min(x))/size(x)
amplitude = (max(y)-min(y))/2
# plot the graph
interactive_plot(x[::-1], y, min(x), max(x), step, amplitude)

