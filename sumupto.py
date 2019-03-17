# Thomas Roux
# Solution to Problem 1 - calculates sum of all 
# numbers between one and user entered integer
# Begun: 09/02/2019; 16h00

# Asks user for input, and checks whether input value an integer
while True:
    try:
        i = int(input("\nPlease enter a positive integer above zero: "))
        break
# Continues to prompt user to enter valid integer until correct
    except ValueError:
        print("Please enter digits only. Please try again")

# Checks to see if entered character is an integer amenable to computation
# Program will exit if i equal to 0
if i == 0: 
    print("\nInvalid character - please enter an integer above zero.")
    print("Exiting program...")
    print()
    exit()
# Program will convert negative integer to positive and continue
elif i < 0: 
    i = abs(i)
    print("\nNegative integer changed to positive.")

# Creates variable to store total in through 'for' loop iterations
total = 0

# Calculates sum of user entered integer
for x in range(i + 1):
    total = total + x

# Prints total
print(f"\nThe sum of all numbers between 1 and {i} is: {total}")
print()