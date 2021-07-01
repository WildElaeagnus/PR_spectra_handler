# fft test
from mpmath import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import file_browser
from file_browser import file_browser_
from interactive_plot import *
import math
import scipy
from scipy.fft import fft, ifft

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

y_fft = pd.Series(fft(y.to_numpy()))

y_fft_ = pd.Series(np.real(y_fft.truncate(0, y_fft.size/2)))
# pog_pd_ = pog_pd.to_numpy()
_y_fft_ = y_fft_[::-1].reset_index(drop = True)

x_fft = x.truncate(0, x.size/2)

fig, ax = plt.subplots(nrows=1, ncols=3,)

ax[0].plot(x, y)

ax[0].set(title = "PR_signal")

ax[1].plot(x_fft, _y_fft_)
# ax[1].axis([0, 681, -15, 15]) not working
ax[1].set(title = "Interferogram")

ax[2].plot([1, 2, 3], [1, 2, 3])

ax[2].set(title = "PR signal with no noise")

fig.subplots_adjust(left=0.15, bottom=0.5)

figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()
plt.show()
# print(x, y)

