# Problem 31: Chickens and Rabbits
 # We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

# Original: 09 December 2020

print("We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many chickens and how many rabbits do we have?\n")

# build the lists of all possible solutions, based off of legs
p_c = [2*(x+1) for x in range(35)]
p_r = [4*(x+1) for x in range(35)]

# iterate through to find the answer
for c in p_c:
    for r in p_r:
        if c+r == 94 and p_c.index(c)+p_r.index(r)+2 == 35:
            print("There are " + str(p_c.index(c)+1) + " chickens and " + str(p_r.index(r)+1) + " rabbits.")



