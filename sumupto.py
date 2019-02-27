# Thomas Roux
# Solution to Problem 1 - calculates sum of all 
# numbers between one and user entered integer
# Begun: 09/02/2019; 16h00

# Asks user for input, and checks whether input value an integer
# Continues to prompt user to enter valid integer until correct
while True:
    try:
        i = int(input("\nPlease enter a positive integer: "))
        break
    except ValueError:
        print("That is not an integer, e.g. 12, 5, 173, etc. Please try again")

# Checks to see if entered character is a integer amenable to computation
if i == 0:
    print("Invalid character - please enter an integer above zero.")
# need to work out how to repeat question or quit programme here
elif i < 0:
    i = abs(i)
    print("\nNegative integer changed to positive.")

# Calculates sum and prints total
total = 0

for x in range(i + 1):
    total = total + x

print("\nThe sum of all numbers between 1 and " + str(i) + " is: " + str(total))
print()