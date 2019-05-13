# Cameron Rodriguez
# Date
# This program encrypts and decrypts files.

# These modules generates the GUI for the program
import Tkinter as tk
import tkFileDialog

"""
Data Dictionary

main
crypt
location
"""

# This class generates the GUI for the program and runs the main menu
# tk.Frame: classobj: provides the Tkinter Frame interface as a superclass
class MainMenu(tk.Frame):
    # This function initializes the Tkinter interface and hosts the main menu of the program.
    def __init__(self):
        # Initialize window
        main = tk.Tk()
        tk.Frame.__init__(self, master=main)
        self.main = main

        # Configure window
        self.main.title('Encryption Program')
        self.main.lift()
        self.main.rowconfigure(0, weight=1)
        self.main.columnconfigure(0, weight=1)
        
        # Add text and options
        tk.Label(self.main, text='Welcome to the Encryption program! This program will take a text file that you specify, and '+
                 'then either encrypt or decrypt its data with the provided password. Select an option to the right to get started.',
                 wraplength=240, height=5, justify='left').grid(rowspan=3, row=0, columnspan=2, column=0, padx=(0,5))
        tk.Button(self.main, text='Encrypt data', command=self.encrypt, anchor='center').grid(column=2, row=0, sticky='NSEW')
        tk.Button(self.main, text='Decrypt data', command=self.decrypt, anchor='center').grid(column=2, row=1, sticky='NSEW')
        tk.Button(self.main, text='Quit program', command=main.destroy, anchor='center').grid(column=2, row=2, sticky='NSEW')
    # def __init__

    # This function calls the EncryptMenu class to encrypt data.
    def encrypt(self):
        crypt = CryptMenu(self, 'en')
    # End encrypt

    # This function calls the DecryptMenu class to decrypt data.
    def decrypt(self):
        crypt = CryptMenu(self, 'de')
    # End decrypt
# End MainMenu

# This class loads the encryption or decryption menu to allow the user to encrypt or decrypt a file.
# tk.Toplevel: classobj: provides the Tkinter Toplevel interface as a superclass
class CryptMenu(tk.Toplevel):
    # This function allows the user to select the file to encrypt or decrypt
    # main: instance: an instance of Tk that becomes the parent of the Toplevel class
    # action: str: indicates whether the file will be encrypted or decrypted
    def __init__(self, main, action):
        # Initialize window
        tk.Toplevel.__init__(self, main)
        self.main = main
        self.title('Encrypt Data')
        
        # Add file select menu
        tk.Label(self, text='Please select the location of the file you would like to encrypt.').grid(columnspan=3,
                                                                                                                  column=0, row=0)
        tk.Label(self, text='File location:', anchor='w', borderwidth=1, relief='solid').grid(column=0, row=1, padx=(0,5), sticky='W')
        location = tk.Entry(self, width=60).grid(columnspan=2, column=0, row=1, padx=(70,0), sticky='NSEW')
# End EncryptMenu

a = MainMenu()
a.mainloop()
