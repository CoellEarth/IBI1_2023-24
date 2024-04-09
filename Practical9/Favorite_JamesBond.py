str_born=input("You were born in year:")
born=int(str_born)
def your_fav_JamesBond(born):
    if born+18<=1986 and born+18>=1973:
        return "Roger Moore"
    elif born+18<=1994 and born+18>=1987:
        return "Timothy Dalton"
    elif born+18<=2005 and born+18>=1995:
        return "Pierce Brosnan"
    elif born+18<=2021 and born+18>=2006:
        return "Daniel Craig"
    else:
        return"no one, because James Bond does not exist in your era"
    
print("Your fav James Bond might be",your_fav_JamesBond(born))

#example
print("I was born in 2005, so my fav JB actor is",your_fav_JamesBond(2005),"according to the theory.")
#the output shows "I was born in 2005, so my fav JB actor is no one, because James Bond does not exist in your era according to the theory."
