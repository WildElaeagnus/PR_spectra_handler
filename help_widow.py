
from tkinter import *

import tkinter as tk

class help_window_class():
    """docstring for file_browser_class"""
    def __init__(self, ):
        super(help_window_class, self).__init__()

    def all_text(self, text2, arg1, arg2):
        text2.insert(tk.END, arg1, 'label')
        result = arg2
        text2.insert(tk.END, result, 'body')
        return result

    def main_winow(self, ):

        # Create the window window
        window = Tk()

        # Set window title
        window.title('Help')

        # Set window size
        # window.geometry("700x500")

        #Set window background color
        # window.config(background = "white")

        # text1 = tk.Text(window, height=20, width=30)
        # # photo = tk.PhotoImage(file='./William_Shakespeare.gif')
        # text1.insert(tk.END, '\n')
        # # text1.image_create(tk.END, image=photo)

        # text1.pack(side=tk.LEFT)

        text2 = tk.Text(window, height=30, width=70 )
        scroll = tk.Scrollbar(window, command=text2.yview)
        text2.configure(yscrollcommand=scroll.set)
        text2.tag_configure('label', font=('Verdana 16 bold'))
        text2.tag_configure('body', font=('Helvetica 14'), lmargin1=0, lmargin2=65)
        quote = self.all_text(
            text2,
            'Help photoreflection spectra handler\n',
            """
        This program is designed for the processing of photoreflection spectra, specifically for fitting the shape of the interference 
        signal into the spectrum.
        Filtering out the interference signal in the spectrum can help to detect a more complex signal that has been distorted by the 
        interference overlay. 
        """,
        )

        quote = self.all_text(
            text2,
            '\nLeft graph\n',
            """
        This graph is needed to adjust the sinusoidal shape as close 
        as possible to the part of the spectrum that should be 
        responsible for the interference signal. 
        """,
        )

        quote = self.all_text(
            text2,
            '\nRght graph\n',
            """
        This graph is needed to see the result of subtracting the fitted sine wave from the original spectrum. 
        """,
        )

        quote = self.all_text(
            text2,
            '\nCd left and righ sliders\n',
            """
        These sliders represents amount of attenuation by gauss 
        function from right and left side accordingly.
        """,
        )

        quote = self.all_text(
            text2,
            '\nWd left and right sliders\n',
            """
        These sliders represents intensity of attenuation by gauss 
        function from right and left side accordingly.
        """,
        )

        quote = self.all_text(
            text2,
            '\nAmp slider\n',
            """
        This slider represents amplitude of sine signal.
        """,
        )

        quote = self.all_text(
            text2,
            '\nFreq slider\n',
            """
        This slider represents frequency of sine signal.
        """,
        )

        quote = self.all_text(
            text2,
            '\nPhase slider\n',
            """
        This slider represents phase of sine signal from 0 to 2*Pi in 
        rads. 
        """,
        )

        quote = self.all_text(
            text2,
            '\nOffset slider\n',
            """
        This slider represents offset of sine signal along the x-axis. 
        """,
        )

        quote = self.all_text(
            text2,
            '\nReset button\n',
            """
        This button returns all sliders to their default positions witch is marcked red on each sliider.
        """,
        )

        # quote = self.all_text(
        #     text2,
        #     '\nHeader\n',
        #     """
        # som tex 
        # """,
        # )




        text2.pack(side=tk.LEFT)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        tk.mainloop()

		

if __name__ == "__main__":
	hello = help_window_class()
	hello.main_winow()
