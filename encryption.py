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
selected_file
raw_file
original
password_field
password
key
temp
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
        
        # Add intro and buttons to encrypt/decrypt/quit program
        tk.Label(self.main, text='Welcome to the Encryption program! This program will take a text file that you specify, and '+
                 'then either encrypt or decrypt its data with the provided password. Select an option to the right to get started.',
                 wraplength=240, height=5, justify='left').grid(rowspan=3, row=0, columnspan=2, column=0, padx=(0,5))
        tk.Button(self.main, text='Encrypt data', command=self.encrypt, anchor='center').grid(column=2, row=0, sticky='NSEW')
        tk.Button(self.main, text='Decrypt data', command=self.decrypt, anchor='center').grid(column=2, row=1, sticky='NSEW')
        tk.Button(self.main, text='Quit program', command=main.destroy, anchor='center').grid(column=2, row=2, sticky='NSEW')
    # def __init__

    # This function calls the FileMenu class to encrypt data.
    def encrypt(self):
        crypt = FileMenu(self, 'En')
    # End encrypt

    # This function calls the FileMenu class to decrypt data.
    def decrypt(self):
        crypt = FileMenu(self, 'De')
    # End decrypt
# End MainMenu

# This class loads the encryption or decryption menu to allow the user to encrypt or decrypt a file.
# tk.Toplevel: classobj: provides the Tkinter Toplevel interface as a superclass
class FileMenu(tk.Toplevel):
    # This function allows the user to select the file to encrypt or decrypt.
    # main: instance: an instance of Tkinter Frame that becomes the parent of the Toplevel class
    # action: str: indicates whether the file will be encrypted or decrypted
    def __init__(self, main, action):
        # Initialize window
        tk.Toplevel.__init__(self, main)
        self.lift()
        self.main = main
        self.action = action
        self.title('{}crypt Data'.format(self.action))
        
        # Add intro, text box to enter file address, and buttons to select with GUI and OK
        tk.Label(self, text='Please type or select the location of the file you would like to {}crypt below.'.format(self.action.lower())).grid(columnspan=3,
                                                                                                                  column=0, row=0)
        tk.Label(self, text='File\nlocation:', anchor='w', borderwidth=1, relief='solid').grid(column=0, rowspan=2, row=1, padx=(0,5), sticky='NSW')
        self.location = tk.Text(self, wrap=tk.WORD, height=3, width=36)
        self.location.grid(column=0, rowspan=2, row=1, padx=(50,0))
        tk.Button(self, text='Open file', command=self.file_select, width=8).grid(column=1, row=1, sticky='NSEW')
        tk.Button(self, text='Use this file', command=self.open_file, width=8).grid(column=1, row=2, sticky='NSEW')
    # End __init__
    
    # This function uses tkFileDialog to allow the user to select a specific file.
    def file_select(self):
        # Open GUI to select file
        selected_file = None
        selected_file = tkFileDialog.askopenfilename(initialdir='H:/', title = 'Select File', filetypes=(('Text Documents', '*.txt'), ('Markdown Document', '*.md'),
                                                                                                         ('Rich Text Format', '*.rtf'), ('All Files', '*.*')))
        
        # Replace text box contents with selected file
        self.location.delete('1.0', tk.END)
        self.location.insert(tk.END, selected_file)
        if selected_file is not None:
            self.lift() # Lifts Toplevel window again after file is selected
        # End if selected_file
    # End file_select
    
    # This function loads the selected file into the program and calls the PasswordMenu class to start encryption/decryption.
    def open_file(self):
        # Read the file into a variable
        with open(self.location.get('1.0', 'end-1c'), 'r') as raw_file:
            self.original = raw_file.read()
        
        self.destroy()
        crypt = PasswordMenu(self.main)
    #End open_file
# End FileMenu

# This class requests the password, and calls the encryption/decryption functions
# tk.Toplevel: classobj: provides the Tkinter Toplevel interface as a superclass
class PasswordMenu(tk.Toplevel):
    # This function requests a password from the user.
    # main: instance: an instance of Tkinter Frame that becomes the parent of the Toplevel class
    def __init__(self, main):
        # Initialize window
        tk.Toplevel.__init__(self, main)
        self.main = main
        self.title('Enter Password')
        
        # Add widgets to enter password and describe requirements
        tk.Label(self, text='Please enter a password which meets the following requirement:\n'+
                 '    - Minimum length of 3 characters', justify='left').grid(columnspan=3, column=0, row=0)
        tk.Label(self, text='Password:', anchor='w').grid(column=0, row=1, sticky='W')
        self.password_field = tk.Entry(self)
        self.password_field.grid(columnspan=3, column=0, row=1, padx=(60,27), sticky='NSEW') 
        tk.Button(self, text='OK', command=self.check_password).grid(column=2, row=1, sticky='NSE')
    # End __init__

    # This function ensures that the password given is valid, and runs the encryption/decryption program if so.
    def check_password(self):
        self.password = self.password_field.get()
        
        if len(self.password) >= 3:
            self.destroy()
            key = encryption_key(self.password) # Generate the encryption key
        else:
            temp = tk.Toplevel(self)
            temp.title('Invalid Password')
            tk.Label(temp, text='The password provided contains invalid characters.'+
                     '\nPlease try again with ASCII characters.').grid(column=0, row=0)
            tk.Button(temp, text='OK', command=temp.destroy, width=8).grid(column=0, row=1)

# This function generates the encryption key from the password
# password: string: contains the user's password
# Returns the encryption key
def encryption_key(password):
    pass

a = MainMenu()
a.mainloop()
