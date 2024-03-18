#Task 1w

activity_time={'sleeping':8,'classes':6,'studying':3.5,'TV':2,'Music':1}
print('before adding the "Others" entry,the dictionary is ',activity_time)
#24-8-6-3.5-2-1=3.5
#so "other" occupies 3.5 hours on an average level
activity_time['Others']=3.5
print('after adding the "Others" entry,the dictionary is ',activity_time)

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

print("---")

print("What kind of activity are you interested in when it comes to the average time spent? 'sleeping', 'classes', 'studying', 'TV', 'Music', 'Others' ")
print("PLEASE BE MINDFUL OF YOUR SPELLING!")
userinput=input("I am interested in:")
print(activity_time[userinput],"hours spent on an average level")

#Task 2
UK_cities=[0.56,0.62,0.04,9.7]
China_cities=[0.58,8.4,29.9,22.2]
sorted_UK_cities=sorted(UK_cities)
sorted_China_cities=sorted(China_cities)
print("Sorted values for the populations of cities in the UK and China are ",sorted_UK_cities,"and ",sorted_China_cities,"respectively. ")

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

