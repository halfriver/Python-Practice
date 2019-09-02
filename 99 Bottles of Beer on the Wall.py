# Python Problem 1
# 1 Sept 2019

bottlenmbr = 99
def plural(bottlenmbr):
    if bottlenmbr != 1:
        return(str(bottlenmbr) + " bottles ")
    else:
        return(str(bottlenmbr) + " bottle ")
while bottlenmbr > 0:
    print(plural(bottlenmbr) + "of beer on the wall, " + plural(bottlenmbr) + "of beer. Take one down and pass it around. " + plural(bottlenmbr - 1) + "of beer on the wall. \n")
    bottlenmbr -= 1
print("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.")
    
 
