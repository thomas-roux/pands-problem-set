# Thomas Roux
# Solution to Problem 10 - displays a plot of the functions x, x**2, and 2x for range 0 to 4 (whole integer steps)
# Begun: 25/03/2019; 21h30

# Import the necessary modules to allow working with plots
import numpy as np
import matplotlib.pyplot as plt

# Create an array to include 0 to 4
x = np.arange(5)

# Calculate plot placements according to function specified above and individualise function graphics - 
# https://matplotlib.org/users/pyplot_tutorial.html
plt.plot(x, x, 'r--', x, x**2, 'bs', x, x * 2, 'g^')
    
# Label graph
plt.xlabel('X value')
plt.ylabel('Y value')
plt.title('Function of x, x**2, 2x', fontsize = 14)

plt.legend(loc = 'upper left')
plt.show()
    