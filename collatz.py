# Thomas Roux
# Solution to Problem 4 - user input positive integer subjected to following calculation:
# at each step, next value determined by taking current value, if even, dividing by two; 
# if odd, multiply by 3 and add one.
# Programme ends when value = 1
# Begun: 20/02/2019; 22h00

# Asks user for input, and checks whether input value an integer
# Continues to prompt user to enter valid integer until correct
while True:
    try:
        i = int(input("\nPlease enter a positive integer above zero: "))
        break
    except ValueError:
        print("Please enter digits only. Please try again")

# Check to see if entered characters a valid integer
if i == 0:
    print("Invalid character - please enter an integer above zero.")
    print("Exiting program...")
elif i < 0:
    i = abs(i)
    print("\nNegative integer changed to positive.\n")

# Displays user chosen integer on same line as results
print(i, end = " ")

# Performs calculation and displays result of each step until value = 1
while i > 1:
    if i % 2 == 0:
        i = i / 2
    else:
        i = (i * 3) + 1 
    print(int(i), end = " ")

# Prints empty line 
print()