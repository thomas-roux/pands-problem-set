# Thomas Roux
# Solution to Problem 3 - prints all values between 1,000 and
# 10,000 that are divisble by 6, but not 12
# Begun: 20/02/2019; 21h30

# Create an empty list to store divisible numbers
l = []

# Extract numbers divisible by six from specified range and return to list 'l'
for i in range(1000, 10001):
    if i % 6 == 0:
        l.append(i)

# Remove numbers in list 'l' divisible by 12
for i in l:
    if i % 12 == 0:
        l.remove(i)

# Print result - numbers in range divisible by 6 but not by 12
for i in l:
    print(i)
    
       




