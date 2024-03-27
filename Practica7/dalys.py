import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/Users/32771/Desktop/IBI/practical/Practical7")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

specific_value=dalys_data.iloc[0:101:10,3]
print(specific_value)

Discriminate_Afghanistan=dalys_data.iloc[:,0]=="Afghanistan"
Afghanistan_data=dalys_data.loc[Discriminate_Afghanistan,"DALYs"]
print(Afghanistan_data)

Discriminate_China=dalys_data.iloc[:,0]=="China"
China_data=dalys_data.loc[Discriminate_China,["DALYs","Year"]]
print(China_data)
China_DALYs_data=China_data.loc[:,"DALYs"]
China_Year_data=China_data.loc[:,"Year"]
China_DALYs_mean=np.mean(China_DALYs_data)
print("The mean DALYs in China over time is",China_DALYs_mean)

#Comparation:the DALY in 2019,China is 22270.51, so it is less than the mean

plt.figure()
plt.plot(China_Year_data,China_DALYs_data,'b+')
plt.xticks(China_Year_data,rotation=-90)
plt.show()
plt.clf()

#question solutions

Discriminate_2019=dalys_data[dalys_data.iloc[:,2] == 2019 ]
data_set_2019=Discriminate_2019.loc[:,"DALYs"]
#Discriminate_2019=dalys_data.iloc[:,2]=="2019"
#data_set_2019=dalys_data.loc[Discriminate_2019,"DALYs"]
print(data_set_2019)

plt.figure()
data_set_2019.plot(kind="box",title="DALYs in 2019 across countries",figsize=(10,8))
plt.show()
plt.clf()
