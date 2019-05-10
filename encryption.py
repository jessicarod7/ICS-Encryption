# Cameron Rodriguez
# Date
# This program encrypts and decrypts files.

# These modules generates the GUI for the program
import Tkinter as tk
import tkFileDialog

"""
Data Dictionary


"""

# This class generates the GUI for the program and handles major navigation.
# tk.Tk: CLASS: provides the Tkinter interface to the class
class MenuInterface(tk.Tk):
    # This function initializes the class and its Tkinter frame
    def __init__(self):
        # Initialize window
        tk.Tk.__init__(self)
        tk.Frame.__init__(self)
        self.main_menu()
    # End __init__
        
    def main_menu(self):
        main = tk.Frame(self)
        main.title('Encryption Program')
        main.lift()
        
        # Add text and options
        tk.Label(main, text='Welcome to the Encryption program! This program will take a text file that you specify, and'+
                 'then either encrypt or decrypt its data with the provided password. Select an option to the right to get started.', justify='center',
                 wraplength=70, height=2).grid(rowspan=3, row=0, column=0)
        tk.Button(main, text='Encrypt data', command=self.encrypt, anchor='center').grid(column=1, row=0, sticky='NSEW')
        tk.Button(main, text='Decrypt data', command=self.decrypt, anchor='center').grid(column=1, row=1, sticky='NSEW')
        tk.Button(main, text='Quit program', command=self.quit, anchor='center').grid(column=1, row=2, sticky='NSEW')

a=MenuInterface()
a.mainloop()
