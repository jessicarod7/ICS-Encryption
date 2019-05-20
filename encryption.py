# Cameron Rodriguez
# Date
# This program encrypts and decrypts files.

# These modules generates the GUI for the program
import Tkinter as tk
import tkFileDialog

import math # This module is used to split the password into sets of three

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
crypted_text
invalid
key_trio
key_val
key_half
ascii_list
key_shift
triple_key
single_key
single_key_sum
l
b
final_file
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
        # End with open
        self.destroy()
        crypt = PasswordMenu(self.main, self.action, self.original, self.location)
    #End open_file
# End FileMenu

# This class requests the password, and calls the encryption/decryption functions.
# tk.Toplevel: classobj: provides the Tkinter Toplevel interface as a superclass
class PasswordMenu(tk.Toplevel):
    # This function requests a password from the user.
    # main: instance: an instance of Tkinter Frame that becomes the parent of the Toplevel class
    # action: str: indicates whether the file will be encrypted or decrypted
    # original: str: the file to be encrypted or decrypted
    # location: str: the location of the original file
    def __init__(self, main, action, original, location):
        # Initialize window
        tk.Toplevel.__init__(self, main)
        self.main = main
        self.action = action
        self.original = original
        self.location = location
        self.title('Enter Password')
        
        # Add widgets to enter password and describe requirements
        tk.Label(self, text='Please enter a password which meets the following requirement:\n'+
                 '    - Minimum length of 3 characters', justify='left').grid(columnspan=3, column=0, row=0)
        tk.Label(self, text='Password:', anchor='w').grid(column=0, row=1, sticky='W')
        self.password_field = tk.Entry(self)
        self.password_field.grid(columnspan=3, column=0, row=1, padx=(60,97), sticky='NSEW')
        tk.Button(self, text='{}crypt my data'.format(self.action), command=self.check_password).grid(column=2, row=1, sticky='NSE')
    # End __init__

    # This function ensures that the password given is valid, and runs the encryption/decryption program if so.
    def check_password(self):
        self.password = self.password_field.get()
        
        if len(self.password) >= 3:
            self.destroy()
            key = encryption_key(self.password) # Generate the encryption key
            crypted_text = crypt(key, self.action, self.original)
            result = FinalMenu(self.main, self.action, self.location, crypted_text)
        else:
            invalid = tk.Toplevel(self)
            invalid.title('Invalid Password')
            tk.Label(invalid, text='The password provided contains invalid characters.'+
                     '\nPlease try again with ASCII characters.').grid(column=0, row=0)
            tk.Button(invalid, text='OK', command=invalid.destroy, width=8).grid(column=0, row=1)
        # End if len(self.password)
    # End check_password
# End PasswordMenu

# This class lets the user select where to save the completed file.
# tk.Toplevel: classobj: provides the Tkinter Toplevel interface as a superclass
class FinalMenu(tk.Toplevel):
    # This function introduces the user to the filesave menu.
    # main: instance: an instance of Tkinter Frame that becomes the parent of the Toplevel class
    # action: str: indicates whether the file will be encrypted or decrypted
    # original: str: the file to be encrypted or decrypted
    # location: str: the location of the original file
    # crypted_text: str: the encrypted/decrypted text
    def __init__(self, main, action, location, crypted_text):
        # Initialize window
        tk.Toplevel.__init__(self, main)
        self.main = main
        self.action = action
        self.location = location
        self.crypted_text = crypted_text
        self.title('Text {}crypted'.format(self.action))

        # Describe result
        self.l = tk.Label(self, text='Your file has been successfully {}crypted. On the next screen, you will select '+
                 'where to save the file.'.format(action.lower())).grid(column=0, row=0)
        self.b = tk.Button(self, text='OK').grid(column=0, row=1, command=self.save)
    # End __init__

    # This function lets the user choose where to save the file and does so
    def save(self):
        selected_file = None
        self.location = self.location[:len(self.location)-(self.location[::-1].index('/'))] # Sets location to parent folder of original file

        selected_file = tkFileDialog.asksaveasfilename(initialdir=self.location, title = 'Save File', filetypes=(('Text Documents', '*.txt'), ('Markdown Document', '*.md'),
                                                                                                         ('Rich Text Format', '*.rtf'), ('All Files', '*.*')))
        if selected_file is not None:
            # Save file
            with open(selected_file, 'w+') as final_file:
                final_file.write(self.crypted_text)
            # End with open

            # Show confirmation window
            self.l.destroy()
            self.b.destroy()
            
            self.title('File Saved')
            tk.Label(self, text='Your file has been saved').grid(column=0, row=0)
            tk.Button(self, text='OK').grid(column=0, row=0)
        # End if selected_file
    # End save

# This function generates the encryption key from the password
# password: string: contains the user's password
# Returns the encryption key
def encryption_key(password):
    key_val=0
    key=[]
    key_int=0
    
    # Generate first part of encryption key by splitting password into groups of three or less
    for i in range(int(math.ceil(len(password)/3.0))): 
        key_trio = [0, 0, 0]
        
        # Generate first character in key trio
        key_trio[0] = str(ord(password[i*3]))
        while int(key_trio[0]) >= 10: # Add digits to get a single digit result, repeating if necessary
            if int(key_trio[0]) >= 100:
                key_trio[0] = str(int(key_trio[0][-3]) + int(key_trio[0][-2]) + int(key_trio[0][-1]))
            else:
                key_trio[0] = str(int(key_trio[0][-2]) + int(key_trio[0][-1]))
            # End while key_trio[0]
        # End while key_trio[0]
        
        try:
            # Generate second character in key trio
            key_trio[1] = str(ord(password[(i*3)+1]))
            for j in range(9, 0, -1): # Get single digit result from largest single digit factor
                if int(key_trio[1]) % j == 0:
                    key_trio[1] = str(j)
                    break
                # End if key_trio[1]
            # End for j
            
            # Generate third character in key trio
            key_trio[2] = str(ord(password[(i*3)+2]))
            key_trio[2] = key_trio[2][-1] # Uses last digit of character value for single digit result
        except IndexError: # End of password reached
            pass
        # End try/except
        
        for j in key_trio:
            if type(j) is str:
                key.append(j)
            # End if type(j)
        # End for j
    # End for i
    
    key = ''.join(key)
    
    # Generate and add extra character in middle of key
    key_val = str((int(key) / len(key)) % 10)
    key_half = len(key) / 2
    key = key[:key_half] + key_val + key[key_half:]
    
    return key

# This function encrypts or decrypts the file depending on the option given.
# key: str: the encryption key
# action: str: indicates whether the file will be encrypted or decrypted
# original: str: the file to be encrypted or decrypted
# Returns the encrypted/decrypted file
def crypt(key, action, original):
    # Convert every char in original to its ASCII value
    ascii_list = [ord(i) for i in original]
    key_shift = int(key[-3:]) % 224 # Within the range of visible ASCII chars, 32-255
    triple_key = 3 * int(key[0])
    single_key = key

    while len(single_key) > 1: # Add key digits until a single digit is reached
        single_key_sum = 0
        for i in range(len(single_key)):
            single_key_sum += single_key[i]
        # End for i
        single_key = str(single_key_sum)
    # End while len(single_key)
    single_key += 100  # For printability

    if action == 'En': # Encrypt file
        # Shift to right by key_shift spaces, looping if necessary
        for i in range(len(ascii_list)):
            ascii_list[i] += key_shift
            if ascii_list[i] > 255:
                ascii_list[i] -= 224
            # End if ascii_list[i]
        # End for i

        # Adds triple_key at interval, looping if necessary
        if int(key[1]) == 0:
            pass
        else:
            for i in range(1, (len(ascii_list)/int(key[1]))+1):
                ascii_list[(i*int(key[1])) - 1] += triple_key
                if ascii_list[i] > 255:
                    ascii_list[i] -= 224
                # End if ascii_list[i]
            # End for i
        # End if int(key[1])

        # Inserts single_key in reverse order at interval
        if int(key[2]) == 0:
            pass
        else:
            for i in range((len(ascii_list)/int(key[2])), 0, -1):
                ascii_list = ascii_list[:(i*int(key[2]))] + [single_key] + ascii_list[(i*int(key[2])):]
            # End for i
        # End if int(key[2])
    else: # Decrypt file
        # Removes single_key in reverse order at interval
        if int(key[2]) == 0:
            pass
        else:
            for i in range((len(ascii_list) / (1 + int(key[2]))), 0, -1): # Adjust interval to account for extra characters
                del ascii_list[(i*int(key[2]))]
            # End for i
        # End if int(key[2])

        # Subtracts triple_key at interval, looping if necessary
        if int(key[1]) == 0:
            pass
        else:
            for i in range(1, (len(ascii_list)/int(key[1]))+1):
                ascii_list[(i*int(key[1])) - 1] += triple_key
                if ascii_list[i] < 32:
                    ascii_list[i] += 224
                # End if ascii_list[i]
            # End for i
        # End if int(key[1])

        # Shift to left by key_shift spaces, looping if necessary
        for i in range(len(ascii_list)):
            ascii_list[i] -= key_shift
            if ascii_list[i] < 32:
                ascii_list[i] += 224
            # End if ascii_list[i]
        # End for i
    # End if action

    # Convert to text and merge to string
    ascii_list = [chr(i) for i in ascii_list]
    crypted_text = ''.join(ascii_list)

    return crypted_text
    
# Start the program
program = MainMenu()
program.mainloop()