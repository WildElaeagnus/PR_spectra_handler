def interactive_plot(x_min=0.0, x_max=1.0, x_stp=0.001):
	from numpy import pi, sin
	import numpy as np
	import matplotlib.pyplot as plt
	from matplotlib.widgets import Slider, Button, RadioButtons

	def signal(amp, freq, phase, offset):
	    return amp * sin(2 * pi * freq * t + phase) + offset

	axis_color = '#fafad2'

	fig = plt.figure()
	ax = fig.add_subplot(111)



	# Adjust the subplots region to leave some space for the sliders and buttons
	fig.subplots_adjust(left=0.25, bottom=0.25)



	t = np.arange(x_min, x_max, x_stp)
	amp_0 = 5
	freq_0 = 3
	phase_0 = 0
	offset_0 = 0



	# Draw the initial plot
	# The 'line' variable is used for modifying the line later
	[line] = ax.plot(t, signal(amp_0, freq_0, phase_0, offset_0), linewidth=2, color='red')
	ax.set_xlim([0, 1])
	ax.set_ylim([-10, 10])



	# Add two sliders for tweaking the parameters


	# Define an axes area and draw a slider in it
	amp_slider_ax  = fig.add_axes([0.25, 0.15, 0.65, 0.03], facecolor = axis_color) #, axisbg=axis_color
	amp_slider = Slider(amp_slider_ax, 'Amp', 0.1, 10.0, valinit=amp_0)



	# Draw another slider
	freq_slider_ax = fig.add_axes([0.25, 0.1, 0.65, 0.03], facecolor = axis_color)
	freq_slider = Slider(freq_slider_ax, 'Freq', 0.1, 30.0, valinit=freq_0)

	#phase slider
	phase_slider_ax = fig.add_axes([0.25, 0.7, 0.65, 0.03], facecolor = axis_color)
	phase_slider = Slider(phase_slider_ax, 'phase', 0.1, 30.0, valinit=phase_0)

	#offset slider
	offset_slider_ax = fig.add_axes([0.25, 0.4, 0.65, 0.03], facecolor = axis_color)
	offset_slider = Slider(offset_slider_ax, 'offset', 0.1, 30.0, valinit=offset_0)

	# Define an action for modifying the line when any slider value changes
	def sliders_on_changed(val):
	    line.set_ydata(signal(amp_slider.val, freq_slider.val, phase_slider.val, offset_slider.val))
	    fig.canvas.draw_idle()
	amp_slider.on_changed(sliders_on_changed)
	freq_slider.on_changed(sliders_on_changed)
	phase_slider.on_changed(sliders_on_changed)
	offset_slider.on_changed(sliders_on_changed)


	# Add a button for resetting the parameters
	reset_button_ax = fig.add_axes([0.8, 0.025, 0.1, 0.04], facecolor = axis_color)
	reset_button = Button(reset_button_ax, 'Reset', color=axis_color, hovercolor='0.975')
	def reset_button_on_clicked(mouse_event):
	    freq_slider.reset()
	    amp_slider.reset()
	    phase_slider.reset()
	    offset_slider.reset()
	reset_button.on_clicked(reset_button_on_clicked)



	# Add a set of radio buttons for changing color
	color_radios_ax = fig.add_axes([0.025, 0.5, 0.15, 0.15], facecolor = axis_color)
	color_radios = RadioButtons(color_radios_ax, ('red', 'blue', 'green'), active=0)
	def color_radios_on_clicked(label):
	    line.set_color(label)
	    fig.canvas.draw_idle()
	color_radios.on_clicked(color_radios_on_clicked)


	# ax[1].plot(-x,y)
	# ax[1].set_ylabel('coherence')
	# plt.show()

if __name__ == "__main__":
	interactive_plot()
	# plt.show()