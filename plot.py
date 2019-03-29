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
plt.plot(x, x, 'ro', label = "y = x")
plt.plot(x, x * 2, 'g^', label = "y = 2x")
plt.plot(x, x**2, 'bs', label = "y = x**2")
    
# Label graph
plt.xlabel('X value')
plt.ylabel('Y value')
plt.title('Function of x, 2x, x**2', fontsize = 14)
plt.legend(loc = "upper left", fontsize = "small")

# Print graph
print("\nPlot will open in new window.\n")
plt.show()
    