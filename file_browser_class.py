
from tkinter import *
from tkinter import filedialog

filename = None 

class file_browser_class(object):
	"""docstring for file_browser_class"""
	def __init__(self, arg):
		super(file_browser_class, self).__init__()
		self.arg = arg
		
	# a file explorer in Tkinter

		# import all components
		# from the tkinter library
	
	

	def file_browser_():
		# import filedialog module
		

		# Function for opening the
		# file explorer window
		def browseFiles():
			global filename
			filename = filedialog.askopenfilename(initialdir = "/",
												title = "Select a File",
												filetypes = (("DPT files",
																"*.DPT*"),
															("all files",
																"*.*")))
			
			# Change label contents
			label_file_explorer.configure(text="File Opened: "+filename)

		def pepe():
			print(filename)
			window.destroy()
			return()


		print(filename)
			# Create the root window
		window = Tk()

		# Set window title
		window.title('File Explorer')

		# Set window size
		window.geometry("700x100")

		#Set window background color
		window.config(background = "white")

		# Create a File Explorer label
		label_file_explorer = Label(window,
									text = "File Explorer using Tkinter",
									width = 100, height = 4,
									fg = "blue")

			
		button_explore = Button(window,
								text = "Browse Files",
								command = browseFiles)


		button_open = Button(window,
								text = "Open graph",
								command = pepe)


		button_exit = Button(window,
							text = "Exit",
							command = exit)

		# Grid method is chosen for placing
		# the widgets at respective positions
		# in a table like structure by
		# specifying rows and columns
		label_file_explorer.grid(column = 1, row = 2, columnspan=1000)

		button_explore.grid(column = 1, row = 1)

		button_open.grid(column = 2, row = 1)

		button_exit.grid(column = 3,row = 1)

		# Let the window wait for any events
		window.mainloop()
		



if __name__ == "__main__":
	file_browser_class.file_browser_()
