# Thomas Roux
# Solution to Problem 1 - calculates sum of all 
# numbers between one and user entered integer
# Begun: 09/02/2019; 16h00

# Asks user to enter an integer
i = int(input("Please enter a positive integer: "))

# Calculates sum and prints answer
ans = 1
total = 0
while ans <= i:
    total = total + ans
    ans = ans + 1
print(total)