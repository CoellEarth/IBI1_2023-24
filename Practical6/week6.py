#Task 1w

# Define the initial dictionary of activity times
# Print the initial dictionary
# Calculate the time for "Others"
# Add the "Others" entry to the dictionary
# Print the updated dictionary

#a variable of the requested activity that can be modified
sleep=8
class_=6
study_=3.5
TV_=2
Music_=1
activity_time={'sleeping':sleep,'classes':class_,'studying':study_,'TV':TV_,'Music':Music_}
print('before adding the "Others" entry,the dictionary is ',activity_time)
#24-8-6-3.5-2-1=3.5
#so "other" occupies 3.5 hours on an average level
others_=3.5
activity_time['Others']=others_
print('after adding the "Others" entry,the dictionary is ',activity_time)

# Import the necessary library
# Define the data for the pie chart
# Create a new figure for the plot
# Plot the pie chart
# Display the plot
# Clear the current figure to prepare for a new plot

import matplotlib.pyplot as plt
activity_lables = ["sleeping", "classes", "studying", "TV", "Music", "Others"]
time_average = [8, 6, 3.5, 2, 1, 3.5]
studying_explode = [0, 0, 0.3, 0, 0, 0]
plt.figure()
plt.pie(time_average, labels =
activity_lables, 
startangle = 90, explode =
studying_explode)
plt.show()
plt.clf()

#print something to separate two parts
print("---")

# Print the prompt asking the user about their interest
# Get user input
# Define the dictionary of activity times
# Check if the user input matches any key in the dictionary
# Print the average time spent on the selected activity
# Print a message if the input doesn't match any key
print("What kind of activity are you interested in when it comes to the average time spent? 'sleeping', 'classes', 'studying', 'TV', 'Music', 'Others' ")
print("PLEASE BE MINDFUL OF YOUR SPELLING!")
userinput=input("I am interested in:")
if user_input in activity_time:
    print(activity_time[user_input], "hours spent on an average level")
else:
    print("Invalid activity name. Please enter a valid activity.")

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

