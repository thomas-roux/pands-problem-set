# Thomas Roux
# Solution to Problem 9 - takes a txt filename argument from the command line and prints every second line
# Begun: 11/03/2019; 20h00

# Imports sys to allow filename argument from command line - https://stackoverflow.com/questions/7033987/python-get-files-from-command-line
import sys

# Gives filename to last argument from command line. It is assumed file is within same directory python is executed in.
# This will only read the last argument - if there is more than one file name, only the last will be executed
filename = sys.argv[-1]

# Creates index to track line count
index = 1

# Reads each line and prints every second line of text
# Opens file with 'with' argument to ensure closure - https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
with open(filename, 'r') as f:
    for line in f:
        if index % 2 == 0:
            print(line)
        index = index + 1
    