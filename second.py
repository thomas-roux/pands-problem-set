# Thomas Roux
# Solution to Problem 9 - takes a txt filename argument from the command line and prints every second line
# Begun: 11/03/2019; 20h00

# Imports sys to allow filename argument from command line - https://stackoverflow.com/questions/7033987/python-get-files-from-command-line
import sys

# Checks to see if only one filename entered
if len(sys.argv) == 2:
    print()
# Exits if none, or more than one, filename entered
else:
    print()
    print("Please enter a single filename.")
    print()
    exit()

# Gives filename to last argument from command line. It is assumed file is within same directory python is executed in.
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
    