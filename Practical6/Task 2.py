#Task 2

# Define the populations of cities in the UK and China
# Sort the populations of cities in the UK and China
# Print the sorted values for the populations of cities in the UK and China

UK_cities=[0.56,0.62,0.04,9.7]
China_cities=[0.58,8.4,29.9,22.2]
sorted_UK_cities=sorted(UK_cities)
sorted_China_cities=sorted(China_cities)
print("Sorted values for the populations of cities in the UK and China are ",sorted_UK_cities,"and ",sorted_China_cities,"respectively. ")

# Import required libraries
# Define data for plotting
# Create a new figure
# Plot the bar chart
# Labeling the axes and title
# Set the x-axis ticks and labels
# Show the plot
# Clear the current figure

import numpy as np
import matplotlib.pyplot as plt

N = 4
populations_UK = [0.56,0.62,0.04,9.7]
cityname_UK=["Edinburgh","Glasgow","Stirling","London"]
ind = range(4)
width = 0.7

plt.figure()
plt.bar(ind, populations_UK, width) 
plt.ylabel("populations (millions)")
plt.title("poplation by regions in the UK")
plt.xticks(ind,cityname_UK)
plt.show()
plt.clf()

#same as above
N = 4
populations_China = [0.58,8.4,29.9,22.2]
cityname_China=["Haining","Hangzhou","Shanghai","Beijing"]
ind = range(4)
width = 0.7

plt.figure()
plt.bar(ind, populations_China, width) 
plt.ylabel("populations (millions)")
plt.title("poplation by regions in China")
plt.xticks(ind,cityname_China)
plt.show()
plt.clf()

