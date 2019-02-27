# Thomas Roux
# Solution to Problem 7 - determines the square root of floating number to two decimal spaces
# Begun: 27/02/2019; 17h15

# Import the Python mathematics module
import math

# Asks user for input, and checks whether input value a number
# Continues to prompt user to enter valid number until correct
while True:
    try:
        i = float(input("\nPlease enter a positive number: "))
        break
    except ValueError:
        print("That is not a number. Please try again")

# Checks to see if entered character is a number amenable to computation
# Program will exit if i equal to zero
# Program will convert negative integer to positive and continue
if i == 0: 
    print("\nThat is not a positive number - please try again.")
    print()
    exit()
elif i < 0: 
    i = abs(i)
    print("\nNegative number changed to positive.")

# Calculates the square root of the entered value using the math module, and rounds to one decimal space
sr = round(math.sqrt(i), 1)

# Prints the result
print("\nThe square root of", i, "is approximately " + str(sr) + ".")
print()