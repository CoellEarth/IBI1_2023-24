#initial cell density=5
#the starting day=0
#when the density hasn't reached 90, implement the steps below everytime
#   doubles the density
#   ad1 to the day number
#at last output the day
celldensity=5
day=0
while celldensity<=90:
    celldensity=celldensity*2
    day=day+1
print("On day",day,"the cell density goes over 90%, which means you have",day-1,"free days to enjoy your holiday")
   
    

