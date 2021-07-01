from collections import namedtuple


def interactive_plot(arg_x, arg_y, x_min=0.0, x_max=1.0, x_stp=1):
	from numpy import pi, sin
	import numpy as np
	import matplotlib.pyplot as plt
	from matplotlib.widgets import Slider, Button, RadioButtons
	# from numpy import pi, sin
	# import numpy as np
	# import matplotlib.pyplot as plt
	# from matplotlib.widgets import Slider, Button, RadioButtons

	#call main_plot(x, y) and grag all plots to interactive_graph

	fig, ax = plt.subplots(nrows=1, ncols=2,)
	# ax[0].plot(arg_x, arg_y)
	line, = ax[0].plot(arg_x, arg_y)
	line, = ax[1].plot(arg_x, arg_y)

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

	# ax[1].plot(-x,y)
	#show window maimazed
	# ax[1].plot(interactive_plot.t, interactive_plot.s)

	
	# def signal(amp, freq, phase, offset):
	# 	cd = 10
	# 	wd = 0.5
	# 	def gauss_func():
	# 		return (1 / ((np.exp( (-t - cd) / wd)) + (np.exp( (t - cd) / wd)) + 1))
	# 	return gauss_func()

	def signal(amp, freq, phase, offset, cd, wd):
		def gauss_func():
			return (1 / ((np.exp( np.float64(-t%1 - cd + offset)/wd )) + (np.exp( np.float64(t%1 - cd - offset)/wd)) + 1))
		return ((amp * sin(2 * pi * freq * t + phase))  * gauss_func()) 

	axis_color = '#fafad2'


	# fig = plt.figure()
	# ax[1] = fig.add_subplot(122)

	# Adjust the subplots region to leave some space for the sliders and buttons
	fig.subplots_adjust(left=0.2, bottom=0.5)

	t = np.arange(min(arg_x), max(arg_x), (max(arg_x) - min(arg_x))/1000)

	values = namedtuple('values', 'min max default')
	amp_0 = values(0.01, 10, 1)
	freq_0 = values(0.00001, 0.001, 0.0001)
	if __name__ == "__main__":
		freq_0 = values(0.01, 10, 1)
	phase_0 = values(0, 2*np.pi, np.pi)
	offset_0 = values(-10, 10, 0)
	cd_0 = values(0, 1, 1)
	wd_0 = values(0, 1, 0)

	# amp_0 = 5
	# freq_0 = 3
	# phase_0 = 0
	# offset_0 = 0
	# cd_0 = 1
	# wd_0 = 1

	# interactive_plot.t = t
	# interactive_plot.s = signal(amp_0, freq_0, phase_0, offset_0)

	# Draw the initial plot
	# The 'line' variable is used for modifying the line later [line] = 
	line,  = ax[1].plot(t, signal(amp_0.default, 
								  freq_0.default, 
								  phase_0.default, 
								  offset_0.default, 
								  cd_0.default, 
								  wd_0.default), 
								  linewidth=2, 
								  color='red')
	ax[1].set_xlim([min(arg_x), max(arg_x)])
	ax[1].set_ylim([min(arg_y), max(arg_y)])
	# line,  = ax[0].plot(t, signal(amp_0, freq_0, phase_0, offset_0, cd_0, wd_0), linewidth=2, color='red')
	


	# Add two sliders for tweaking the parameters

# region
	# Define an axes area and draw a slider in it
	amp_slider_ax  = fig.add_axes([0.25, 0.15, 0.65, 0.03], facecolor = axis_color) #, axisbg=axis_color
	amp_slider = Slider(amp_slider_ax, 
						'Amp', 
						amp_0.min, 
						amp_0.max, 
						valinit=amp_0.default)



	# Draw another slider
	freq_slider_ax = fig.add_axes([0.25, 0.1, 0.65, 0.03], facecolor = axis_color)
	freq_slider = Slider(freq_slider_ax, 
						 'Freq', 
						 freq_0.min, 
						 freq_0.max, 
						 valinit=freq_0.default)

	#phase slider
	phase_slider_ax = fig.add_axes([0.25, 0.05, 0.65, 0.03], facecolor = axis_color)
	phase_slider = Slider(phase_slider_ax, 
						  'phase',
						  phase_0.min, 
						  phase_0.max, 
						  valinit=phase_0.default)

	#offset slider
	offset_slider_ax = fig.add_axes([0.25, 0.0, 0.65, 0.03], facecolor = axis_color)
	offset_slider = Slider(offset_slider_ax, 
						   'offset', 
						   offset_0.min, 
						   offset_0.max, 
						   valinit=offset_0.default)

	#offset slider
	cd_slider_ax = fig.add_axes([0.25, 0.2, 0.65, 0.03], facecolor = axis_color)
	cd_slider = Slider(cd_slider_ax, 
					   'cd', 
					   cd_0.min, 
					   cd_0.max, 
					   valinit=cd_0.default)

	#offset slider
	wd_slider_ax = fig.add_axes([0.25, 0.25, 0.65, 0.03], facecolor = axis_color)
	wd_slider = Slider(wd_slider_ax, 
					   'wd', 
					   wd_0.min, 
					   wd_0.max, 
					   valinit=wd_0.default)

	# Define an action for modifying the line when any slider value changes
	def sliders_on_changed(val):
	    line.set_ydata(signal(amp_slider.val, freq_slider.val, phase_slider.val, offset_slider.val, cd_slider.val, wd_slider.val))
	    fig.canvas.draw_idle()
	amp_slider.on_changed(sliders_on_changed)
	freq_slider.on_changed(sliders_on_changed)
	phase_slider.on_changed(sliders_on_changed)
	offset_slider.on_changed(sliders_on_changed)
	cd_slider.on_changed(sliders_on_changed)
	wd_slider.on_changed(sliders_on_changed)

	# Add a button for resetting the parameters
	reset_button_ax = fig.add_axes([0.8, 0.3, 0.1, 0.04], facecolor = axis_color)
	reset_button = Button(reset_button_ax, 'Reset', color=axis_color, hovercolor='0.975')
	def reset_button_on_clicked(mouse_event):
	    freq_slider.reset()
	    amp_slider.reset()
	    phase_slider.reset()
	    offset_slider.reset()
	    cd_slider.reset()
	    wd_slider.reset()
	
	reset_button.on_clicked(reset_button_on_clicked)

	# interactive_plot.line = [line]

	# # Add a set of radio buttons for changing color
	# # color_radios_ax = fig_1.add_axes([0.025, 0.5, 0.15, 0.15], facecolor = axis_color)
	# # color_radios = RadioButtons(color_radios_ax, ('red', 'blue', 'green'), active=0)
	# # def color_radios_on_clicked(label):
	# #     line.set_color(label)
	# #     fig_1.canvas.draw_idle()
	# # color_radios.on_clicked(color_radios_on_clicked)


	# ax[1][1].plot(-x,y)
	# # ax[1][1].set_ylabel('coherence')
	
# endregion

	# ax[1].plot([1, 2, 3], [1, 2, 3])
	ax[1].set_ylabel('coherence')


	figManager = plt.get_current_fig_manager()
	figManager.window.showMaximized()
	plt.show()

if __name__ == "__main__":
	interactive_plot([-1, 0, 1], [-10, 2, 10])
	# print(interactive_plot.t)
	# plt.show()
	