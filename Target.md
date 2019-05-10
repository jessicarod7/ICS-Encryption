# Goals

## ASCII values

~~0-31 are invalid~~  
32-255 = **224 valid chars**

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

- Use a GUI (probably Tkinter) to [select the input and output file](https://pythonspot.com/tk-file-dialogs/) (NOTE: tkFileDialog requires Tkinter, but is not part of the module)
- Use another form of encryption OR add onto the shift encryption (use Checkcryption as inspiration)
- NOTE: non-ASCII chars throw a TypeError in ord(), and a ValueError in chr()

## Encryption Method

### Key Generation

- **One to one, password to key**
- Require the password to be all ASCII, min 3 chars
- Split into sets of 3
  - ord() and the 1st/2nd/3rd char in each set has its own numeric equivalent, append to in-progress key
- Divide the sum of the digits by the number of digits (val1), then find the remainder of that number divided by 10 (val2)
- Add val2 after the floor division halfway point of the in-progress key, and finally divide by val1 (gives key), appending val2 again repeatedly if key length is less than 3

### Text Encoding

- ord() every character into a list
- Modulo divide key[-3:] by 224 and right shift by that number, looping as necessary
- Add 3*key[0] to every key[1]^th space in the original, looping as necessary
- Add digits of key repeatedly until the number is single digit, and then **insert** random.randint(0,223)+32 to every ^th position (this may not run, that's ok)
- chr() back to a string and save

### Text Decoding

- ord() every character into a list
- Add digits of key repeatedly until the number is single digit, then run something similar to the following code (tested and verified):

```python
a=[1,1,2,1,1,2,1,1,2,1]

for i in range(n): # n = number of times it can possible occur (division math req.)
    del a[2*(i+1)] # 2 = the single digit number from the key
```

- Subtract 3*key[0] from every key[1]^th space in the original, reverse looping as necessary
- Modulo divide key[-3:] by 224 and left shift by that number, looping as necessary
- chr() back to a string and save

[https://pythonprogramming.net/object-oriented-programming-crash-course-tkinter/](https://pythonprogramming.net/object-oriented-programming-crash-course-tkinter/)
