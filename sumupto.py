# Thomas Roux
# Solution to Problem 1 - calculates sum of all 
# numbers between one and user entered integer
# Begun: 09/02/2019; 16h00

# Asks user for input, and checks whether input value an integer
# Continues to prompt user to enter valid integer until correct
while True:
    try:
        i = int(input("\nPlease enter a positive integer above zero: "))
        break
    except ValueError:
        print("That is not an integer. Please try again")

# Checks to see if entered character is a integer amenable to computation
# Program will exit if i equal to 0
# Program will convert negative integer to positive and continue
if i == 0: 
    print("\nInvalid character - please enter an integer above zero.")
    print()
    exit()
elif i < 0: 
    i = abs(i)
    print("\nNegative integer changed to positive.")

# Calculates sum and prints total
total = 0

for x in range(i + 1):
    total = total + x

print("\nThe sum of all numbers between 1 and " + str(i) + " is: " + str(total))
print()