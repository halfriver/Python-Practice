# Pythagorean Triples Checker
 # Allows the user to input the sides of any triangle in any order.
 # Return whether the triangle is a Pythagorean Triple or not.
 # Loop the program so the user can use it more than once without having to restart the program.

# Original: 03 Sept 2019
# Edited: 24 November 2020

num = [int(x) for x in input("Enter 3 numbers, dilimited by a space after each. Example: 1, 2, 3 \n").split(" ")]

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
