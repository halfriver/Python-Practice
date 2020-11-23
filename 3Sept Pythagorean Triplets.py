# Pythagorean Triples Checker
# 03 Sept 2019

num = [int(x) for x in input("Enter 3 numbers, dilimited by a comma and space after each. Example: 1, 2, 3 \n").split(", ")]

# set the three values to a, b, and c such that c equals the largest number
c_index = num.index(max(num))
if c_index == 1:
    a = num[2]
else:
    a = num[1]
b = num[3 - (num.index(a)) - c_index]
c = num[c_index]

# test and print result
if (a**2) + (b**2) == (c**2):
    print("The set is a Pythagorean Triple.")
elif (a**2) + (b**2) != (c**2):
    print("The set is not a Pythagorean Triple.")
