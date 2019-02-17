# Thomas Roux
# Solution to Problem 1 - calculates sum of all 
# numbers between one and user entered integer
# Begun: 09/02/2019; 16h00

# Asks user to enter an integer
i = int(input("\nPlease enter a positive integer: "))

# Checks to see if entered characters a valid integer
if i == 0:
    print("Invalid character - please enter an integer above zero.")
    # need to work out how to exit programme here or loop back to line 7
elif i < 0:
    i = abs(i)
    print("\nNegative integer changed to positive.")

# Calculates sum and prints total
total = 0

for x in range(i + 1):
    total = total + x

print("\nThe sum of all numbers between 1 and " + str(i) + " is: " + str(total))
print()