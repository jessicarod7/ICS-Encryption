# Goals

## Requirements

- read from a preset text file
- provide the option to encrypt or decrypt
  - if encrypt, request a password and generate the encryption key
  - [ ] ord() characters and use encryption key to shift letters
  - [ ] save to a new file
  - if decrypt, request a password and generate the encryption key
  - [ ] use encryption key to shift letters and chr() characters
  - [ ] save to a new file

**Additional Goals**

- Use a GUI (probably Tkinter) to [select the input file](https://pythonspot.com/tk-file-dialogs/) (NOTE: tkFileDialog requires Tkinter, but is not part of the module)
- Use another form of encryption OR add onto the shift encryption (use Checkcryption as inspiration)
- NOTE: non-ASCII chars throw a TypeError in ord(), and a ValueError in chr()

## Encryption Method

### Key Generation

- **One to one, password to key**
- Require the password to be all ASCII, min 3 chars
- Split into sets of 3
  - ord() and the 1st/2nd/3rd char in each set has its own numeric equivalent, append to in-progress key
- Divide the sum of the digits by the number of digits (val1), then find the remainder of that number divided by 10 (val2)
- Add val2 after the floor division halfway point of the in-progress key, and finally divide by val1

### Text Encoding

### Text Decoding
