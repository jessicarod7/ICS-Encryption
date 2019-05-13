# Cameron Rodriguez
# Date
# This program encrypts and decrypts files.

# These modules generates the GUI for the program
import Tkinter as tk
import tkFileDialog

"""
Data Dictionary


"""

# This class generates the GUI for the program and runs the main menu
# tk.Frame: classobj: provides the Tkinter Frame interface as a superclass
class MainMenu(tk.Frame):
    # This function initializes the Tkinter interface and hosts the main menu of the program.
    def __init__(self):
        # Initialize window
        main = tk.Tk()
        tk.Frame.__init__(self, master=main)

        # Configure window
        main.title('Encryption Program')
        main.lift()
        main.rowconfigure(0, weight=1)
        main.columnconfigure(0, weight=1)
        
        # Add text and options
        tk.Label(main, text='Welcome to the Encryption program! This program will take a text file that you specify, and '+
                 'then either encrypt or decrypt its data with the provided password. Select an option to the right to get started.',
                 wraplength=240, height=5, justify='left').grid(rowspan=3, row=0, columnspan=2, column=0, padx=(0,5))
        tk.Button(main, text='Encrypt data', command=self.encrypt, anchor='center').grid(column=2, row=0, sticky='NSEW')
        tk.Button(main, text='Decrypt data', command=self.decrypt, anchor='center').grid(column=2, row=1, sticky='NSEW')
        tk.Button(main, text='Quit program', command=main.destroy, anchor='center').grid(column=2, row=2, sticky='NSEW')
    # def __init__

    # This function calls the EncryptMenu class to encrypt data.
    def encrypt():
        encrypt = EncryptMenu()
    # End encrypt

    # This function calls the DecryptMenu class to decrypt data.
    def decrypt():
        decrypt = DecryptMenu()
    # End decrypt
# End MainMenu

# This class loads the encryption menu to allow the user to encrypt a file.
# tk.Toplevel: classobj: provides the Tkinter Toplevel interface as a superclass
class EncryptMenu(tk.Toplevel):
    pass
# End EncryptMenu

# This class loads the decryption menu to allow the user to decrypt a file.
# tk.Toplevel: classobj: provides the Tkinter Toplevel interface as a superclass
class DecryptMenu(tk.Toplevel):
    pass
# End DecryptMenu

a = MainMenu()
a.mainloop()