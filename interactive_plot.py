from collections import namedtuple
# from numpy import right_shift
from help_widow import *

from timeit import default_timer as timer
import numpy as np
from numpy import pi, sin
from numpy.core.fromnumeric import size
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

from numba import njit


def interactive_plot(arg_x, arg_y, x_min=0.0, x_max=1.0, x_stp=0.01, y_amp=1):
	# som vars 
	button_color = '#fafad0'
	left_curve_color = '#00ff5f'
	right_curve_color = '#ff3f00'
	
	# TIMEIT = True
	TIMEIT = False

	# allocate space in fig for 2 graphs
	# with plt.ion():
	fig, ax = plt.subplots(nrows=1, ncols=2,)
	
	# left graph with raw specrta
	# with plt.ion():
	line, = ax[0].plot(arg_x, arg_y,)

	ax[0].set(xlabel='k, 1/cm', ylabel='I r. u.',
	        	title="Raw spectra and sine")
	ax[0].grid()

	# right graph with rew spectra
	line_, = ax[1].plot(arg_x, arg_y,)

	ax[1].set(xlabel='k, 1/cm', ylabel='I r. u.',
	        	title="Raw spectra and substracted spectra")
	# ax[1].set_ylabel("pepe",)
	# ax[1].toggle(all=True)

	# ax[1].tick_params(right=True)
	ax[1].grid()

	# secondary axes

	def k2eV(arg):
		return 1.23984*arg/10000 

	def eV2k(arg):
		return 1.23984*arg/10000 

	secax = ax[0].secondary_xaxis('top', functions = (k2eV,  eV2k))
	secax.set_xlabel('E, eV')

	secax = ax[1].secondary_xaxis('top', functions = (k2eV,  eV2k))
	secax.set_xlabel('E, eV')

	#sine generator
	# def map_(x, out_min, out_max):
	# 	return (x - min(x)) * (out_max - out_min) / (max(x) - min(x)) + out_min
	@njit
	def signal(amp, freq, phase, offset, cd_left, wd_left, cd_right, wd_right):
	
		# x = t but transformed for calculating big exponents
		x = map_(t, 0, 1)
		def gauss_func():
			return (1 / ((np.exp((-x - cd_left + offset)/wd_left )) + (np.exp((x - cd_right - offset)/wd_right)) + 1))
		gauss = gauss_func()

		return ((amp * sin(2 * pi * freq * t + phase))  * gauss) 

	# Adjust the subplots region to leave some space for the sliders and buttons
	fig.subplots_adjust(top=0.89,
						bottom=0.46,
						left=0.065,
						right=0.99,
						hspace=0.19,
						wspace=0.15 )

	# t = np.arange(min(arg_x), max(arg_x), (max(arg_x) - min(arg_x))/1000)
	t = np.arange(x_min, x_max, x_stp)
	print("size of t: "+str(size(t)))


	values = namedtuple('values', 'min max default')
	amp_0 = values(0.01, 0.5, y_amp)
	freq_0 = values(0.00001, 0.01, 0.0001)
	if __name__ == "__main__":
		freq_0 = values(0.01, 10, 0.1)
	phase_0 = values(0, 2*np.pi, np.pi)
	offset_0 = values(-1, 1, 0)
	cd_R = values(0, 1, 1)
	wd_R = values(0, 1, 0.1)
	cd_L = values(0, 1, 1)
	wd_L = values(0, 1, 0.1)
# amp, freq, phase, offset, cd_left, wd_left, cd_right, wd_right placed in tuple
	default_sine_config = {'amp': amp_0.default, 
							'freq': freq_0.default, 
							'phase': phase_0.default, 
							'offset': offset_0.default, 
							'wd_left': wd_L.default,
							'cd_left': cd_L.default, 
							'cd_right': cd_R.default,
							'wd_right': wd_R.default}

	# Draw the initial plot
	# The 'line' variable is used for modifying the line later
	line,  = ax[0].plot(t, signal(**default_sine_config), 
								  				linewidth=2, 
								  				color=right_curve_color)
	ax[0].set_xlim([min(arg_x), max(arg_x)])
	ax[0].set_ylim([min(arg_y), max(arg_y)])
	
	line_, = ax[1].plot(arg_x, arg_y - signal(**default_sine_config), 
												color=left_curve_color)



# region
	# Add sliders for tweaking the parameters
	# constrain slider precision in regart to performance
	# slider_step = 100
	# that is not helping anyway

	# Define an axes area and draw a slider in it
	amp_slider_ax  = fig.add_axes([0.25, 0.15, 0.6, 0.03], facecolor = button_color) #, axisbg=button_color
	amp_slider = Slider(amp_slider_ax, 
						'Amp', 
						amp_0.min, 
						amp_0.max, 
						valinit=amp_0.default)



	# Draw frequency slider
	freq_slider_ax = fig.add_axes([0.25, 0.1, 0.6, 0.03], facecolor = button_color)
	freq_slider = Slider(freq_slider_ax, 
						 'Freq', 
						 freq_0.min, 
						 freq_0.max, 
						 valinit=freq_0.default)

	#phase slider
	phase_slider_ax = fig.add_axes([0.25, 0.05, 0.6, 0.03], facecolor = button_color)
	phase_slider = Slider(phase_slider_ax, 
						  'Phase',
						  phase_0.min, 
						  phase_0.max, 
						  valinit=phase_0.default)

	#offset slider
	offset_slider_ax = fig.add_axes([0.25, 0.0, 0.6, 0.03], facecolor = button_color)
	offset_slider = Slider(offset_slider_ax, 
						   'Offset', 
						   offset_0.min, 
						   offset_0.max, 
						   valinit=offset_0.default)

	# amount of attenuation by gauss function from left side
	cd_slider_ax_L = fig.add_axes([0.25, 0.25, 0.6, 0.03], facecolor = button_color)
	cd_slider_L = Slider(cd_slider_ax_L, 
					   'Cd left', 
					   cd_L.min, 
					   cd_L.max, 
					   valinit=cd_L.default)

	# amount of attenuation by gauss function from right side
	cd_slider_ax_R = fig.add_axes([0.25, 0.35, 0.6, 0.03], facecolor = button_color)
	cd_slider_R = Slider(cd_slider_ax_R, 
					   'Cd right', 
					   cd_R.min, 
					   cd_R.max, 
					   valinit=cd_R.default)

	# intensity of attenuation by gauss function from left side
	wd_slider_ax_L = fig.add_axes([0.25, 0.2, 0.6, 0.03], facecolor = button_color)
	wd_slider_L = Slider(wd_slider_ax_L, 
					   'Wd left', 
					   wd_L.min, 
					   wd_L.max, 
					   valinit=wd_L.default,
					   )
					#    valstep= (wd_L.max - wd_L.min)/slider_step

	# intensity of attenuation by gauss function from right side
	wd_slider_ax_R = fig.add_axes([0.25, 0.3, 0.6, 0.03], facecolor = button_color)
	wd_slider_R = Slider(wd_slider_ax_R, 
					   'Wd right', 
					   wd_R.min, 
					   wd_R.max, 
					   valinit=wd_R.default)

	# Define an action for modifying the line when any slider value changes
	def sliders_on_changed(val):
		if(TIMEIT): start = timer()
		val_sine_config = {'amp': amp_slider.val, 
							'freq': freq_slider.val, 
							'phase': phase_slider.val, 
							'offset': offset_slider.val, 
							'cd_left': cd_slider_L.val, 
							'wd_left': wd_slider_L.val,
							'cd_right': cd_slider_R.val,
							'wd_right': wd_slider_R.val}
		line.set_ydata(signal(**val_sine_config))
		line_.set_ydata(arg_y - signal(**val_sine_config))

		fig.canvas.draw_idle()
		if(TIMEIT): print("time: "+str(timer() - start)+" sec")
	
	amp_slider.on_changed(sliders_on_changed)
	freq_slider.on_changed(sliders_on_changed)
	phase_slider.on_changed(sliders_on_changed)
	offset_slider.on_changed(sliders_on_changed)
	cd_slider_L.on_changed(sliders_on_changed)
	wd_slider_L.on_changed(sliders_on_changed)
	cd_slider_R.on_changed(sliders_on_changed)
	wd_slider_R.on_changed(sliders_on_changed)

	# Add a button for resetting the parameters
	reset_button_ax = fig.add_axes([0.05, 0.05, 0.1, 0.04], facecolor = button_color)
	reset_button = Button(reset_button_ax, 'Reset', color=button_color, hovercolor='0.975')
	def reset_button_on_clicked(mouse_event):
	    freq_slider.reset()
	    amp_slider.reset()
	    phase_slider.reset()
	    offset_slider.reset()
	    cd_slider_R.reset()
	    wd_slider_R.reset()
	    cd_slider_L.reset()
	    wd_slider_L.reset()
	reset_button.on_clicked(reset_button_on_clicked)

	# add a help button with breath info about how to use this app
	help_button_ax = fig.add_axes([0.05, 0.1, 0.1, 0.04], facecolor = button_color)
	help_button = Button(help_button_ax, 'Help', color=button_color, hovercolor='0.975')
	def help_button_on_clicked(mouse_event):
		hlp = help_window_class()
		hlp.main_winow()
		# wd_slider_R.set_min(wd_R.min+1)
		# wd_slider_R.set_val(0.5)
		# wd_slider_R.set_max(10)
	help_button.on_clicked(help_button_on_clicked)

	# add buttons to save and load slider values
	#md get max and min values of sliders automatically? but am not sure about that

# endregion

	figManager = plt.get_current_fig_manager()
	try:
		figManager.window.showMaximized()
	except: pass
	fig.canvas.manager.set_window_title('PR spectra handler')

	# print(plt.ion())
	plt.show()
@njit
def map_(x, out_min, out_max):
	return (x - min(x)) * (out_max - out_min) / (max(x) - min(x)) + out_min

if __name__ == "__main__":
	import numpy as np
	# interactive_plot([-1, 0, 100], [-10, 2, 10], -1, 100)
	interactive_plot(np.arange(-1, 100, .1), map_(np.arange(-1, 100, 0.1),0,1), -1, 100, 0.1)

	