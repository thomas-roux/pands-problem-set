# Thomas Roux
# Solution to Problem 5 - requests user positive integer input and returns whether integer is a prime number or not
# Begun: 27/02/2019; 16h30

# Asks user for input, and checks whether input value an integer
while True:
    try:
        i = int(input("\nPlease enter a positive integer: "))
        break
# Continues to prompt user to enter valid integer until correct
    except ValueError:
        print("\nPlease enter digits only. Please try again")

# Checks to see if entered character is a integer amenable to computation
# Program will exit if i equal to zero or 1 (1 is not a prime number as only divisible by itself)
if i == 0: 
    print("\nThat is not a positive integer - please try again.")
    print("Exiting program...\n")
    exit()
elif i == 1:
    print("\nThat is not a prime.\n")
    exit()
# Program will convert negative integer to positive and continue
elif i < 0: 
    i = abs(i)
    if i == 1:
        print("\nThat is not a prime.\n")
        exit()
    else:
        print("\nNegative integer changed to positive.")

# Create empty list to store values that i is divisible by
l = []

# Determines whether integer is divisible by more than itself and one. Runs through loop up to, but not including, i
for pp in range(1,i):
    if i % pp == 0:
        l.append(pp)
    else:
        continue

# Determines whether i is prime number by counting number of values in list l - if more than 1 (i.e. i divisible by 1 and 
# some other values), then not prime.
# Prints result
if len(l) > 1:
    print("\nThat is not a prime.\n")
else: 
    print("\nThat is a prime.\n")
    