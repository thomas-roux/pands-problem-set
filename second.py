# Thomas Roux
# Solution to Problem 9 - takes a txt filename argument from the command line and prints every second line
# Begun: 11/03/2019; 20h00

# Imports sys to allow filename argument from command line - https://stackoverflow.com/questions/7033987/python-get-files-from-command-line
import sys

# Checks to see if only one filename entered
if len(sys.argv) == 2:
    pass
# Exits if none, or more than one, filename entered
else:
    print("\nPlease enter a single filename.\n")
    exit()

# Gives filename to last argument from command line
filename = sys.argv[-1]

# Creates index to track line count
index = 1

# Opens file with 'with' argument to ensure closure - https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# Uses 'try/except' clause in case file missing or path incorrect - https://stackoverflow.com/a/52554112
try:
    with open(filename, 'r') as f:
        # Prints every second line of file
        for line in f:
            if index % 2 == 0:
                print(line)
            index = index + 1
except FileNotFoundError:
    print("\nFile not found. Check filename and path variable.\n")
    exit()
    