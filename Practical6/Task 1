#Task 1

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

