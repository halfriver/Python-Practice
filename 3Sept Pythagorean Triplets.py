# Pythagorean Triples Checker
# 03 Sept 2019

delim = input("Enter 3 numbers, dilimited by a comma and space after each. Example: 1, 2, 3 \n")
num = delim.split(", ")
for x in range(0,len(num)):
    num[x] = int(num[x])

hypo_index = num.index(max(num))
if hypo_index == 1:
    a = num[2]
else:
    a = num[1]
b = num[3 - (num.index(a)) - hypo_index]
c = num[hypo_index]

if (a**2) + (b**2) == (c**2):
    print("Congrats! The set is a Pythagorean Triple.")
elif (a**2) + (b**2) != (c**2):
    print("The set is not a Pythagorean Triple.")
