
from tkinter import *

import tkinter as tk

class help_window_class():
    """docstring for file_browser_class"""
    def __init__(self, ):
        super(help_window_class, self).__init__()


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
        text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
        text2.tag_configure('label', font=('Verdana 16 bold'))
        text2.tag_configure('body', font=('Helvetica 14'), lmargin1=0, lmargin2=40)
        quote = self.all_text(
            text2,
            '\nПервый пнункт\n',
            """
        русский тестк
        To be, or not to be that is the question:
        Whether 'tis Nobler in the mind to suffer
        The Slings and Arrows of outrageous Fortune,
        Or to take Arms against a Sea of troubles,
        Aliquam nonummy adipiscing augue. Lorem ipsum dolor sit amet,
        consectetuer adipiscing elit. Maecenas porttitor congue massa.
        Fusce posuere, magna sed pulvinar ultricies, purus lectus malesuada 
        libero, sit amet commodo magna eros quis urna. Nunc viverra imperdiet 
        enim. Fusce est. Vivamus a tellus. Pellentesque habitant morbi tristique 
        senectus et netus et malesuada fames ac turpis egestas. Proin pharetrasenectus et netus et malesuada fames ac turpis egestas. Proin pharetra 
        nonummy pede. 
        """,
        )

        quote = self.all_text(
            text2,
            '\nSecond пнункт\n',
            """
        русский тестк
        To be, or not to be that is the question:
        Whether 'tis Nobler in the mind to suffer
        The Slings and Arrows of outrageous Fortune,
        Or to take Arms against a Sea of troubles,
        Aliquam nonummy adipiscing augue. Lorem ipsum dolor sit amet,
        consectetuer adipiscing elit. Maecenas porttitor congue massa.
        Fusce posuere, magna sed pulvinar ultricies, purus lectus malesuada 
        libero, sit amet commodo magna eros quis urna. Nunc viverra imperdiet 
        enim. Fusce est. Vivamus a tellus. Pellentesque habitant morbi tristique 
        senectus et netus et malesuada fames ac turpis egestas. Proin pharetra 
        nonummy pede. 
        """,
        )

        quote = self.all_text(
            text2,
            '\nThird пнункт\n',
            """
        русский тестк
        To be, or not to be that is the question:
        Whether 'tis Nobler in the mind to suffer
        The Slings and Arrows of outrageous Fortune,
        Or to take Arms against a Sea of troubles,
        Aliquam nonummy adipiscing augue. Lorem ipsum dolor sit amet,
        consectetuer adipiscing elit. Maecenas porttitor congue massa.
        Fusce posuere, magna sed pulvinar ultricies, purus lectus malesuada 
        libero, sit amet commodo magna eros quis urna. Nunc viverra imperdiet 
        enim. Fusce est. Vivamus a tellus. Pellentesque habitant morbi tristique 
        senectus et netus et malesuada fames ac turpis egestas. Proin pharetrasenectus et netus et malesuada fames ac turpis egestas. Proin pharetra 
        nonummy pede. 
        """,
        )
        quote = self.all_text(
            text2,
            '\nForth пнункт\n',
            """
        русский тестк
        To be, or not to be that is the question:
        Whether 'tis Nobler in the mind to suffer
        The Slings and Arrows of outrageous Fortune,
        Or to take Arms against a Sea of troubles,
        Aliquam nonummy adipiscing augue. Lorem ipsum dolor sit amet,
        consectetuer adipiscing elit. Maecenas porttitor congue massa.
        Fusce posuere, magna sed pulvinar ultricies, purus lectus malesuada 
        libero, sit amet commodo magna eros quis urna. Nunc viverra imperdiet 
        enim. Fusce est. Vivamus a tellus. Pellentesque habitant morbi tristique 
        senectus et netus et malesuada fames ac turpis egestas. Proin pharetrasenectus et netus et malesuada fames ac turpis egestas. Proin pharetra 
        nonummy pede. 
        """,
        )



        text2.pack(side=tk.LEFT)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        tk.mainloop()

    def all_text(self, text2, arg1, arg2):
        text2.insert(tk.END, arg1, 'label')
        result = arg2
        text2.insert(tk.END, result, 'body')
        return result
		

if __name__ == "__main__":
	hello = help_window_class()
	hello.main_winow()
