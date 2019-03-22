# Thomas Roux
# Solution to Problem 6 - takes a user input string and outputs every second word
# Begun: 06/03/2019; 18h00

# Import string module to enable working with punctuation - https://www.tutorialspoint.com/How-to-strip-down-all-the-punctuation-from-a-string-in-Python
import string

# Asks user to input string
i = input("Please enter a sentence: ")

# Splits string into seperate words based on white space and stores in a list
word = i.split()

# Creates a counter to keep track of every second word. If every odd word is preferred (i.e. word 1 + 3 + ...) change 'index = 0'
index = 1

# Loops through individual words in list 'word' and outputs every second word next to each other
for wrd in word:
    # excludes characters that are not words, e.g. !, :, ;, &, etc. Full list here - https://www.dotnetperls.com/punctuation-python
    if wrd in string.punctuation:
        continue
    # determines every second word
    if index % 2 == 0:
        print(wrd, end=" ")
    # loops counter for next iteration
    index = index + 1

# Prints an empty line
print()

