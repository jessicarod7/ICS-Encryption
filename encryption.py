# Cameron Rodriguez
# Date
# This program encrypts and decrypts files.

# These modules generates the GUI for the program
import Tkinter as tk
import tkFileDialog

"""
Data Dictionary


"""

# This class generates the GUI for the program.
# tk.Frame: CLASS: provides the Tkinter frame to the class
class MenuInterface(tk.Frame):
    # This function initializes the class and its Tkinter frame
    # master: CLASS:  references the root class
    def __init__(self, master=None):
        tk.Frame.__init__(self, master) 
        # Option 1: remove the class as it is and call Toplevel windows as needed (Note: even when called
        # independently, Toplevel windows ALWAYS open 2 instances, so I strongly suggest Option 2)
        # Option 2: maintain the Frame for the entire operation, and open Toplevels for en/decryption
    def load_game(self):
        pass