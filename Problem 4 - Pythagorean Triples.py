# Problem 4: Pythagorean Triples Checker
 # Allows the user to input the sides of any triangle in any order.
 # Return whether the triangle is a Pythagorean Triple or not.
 # Loop the program so the user can use it more than once without having to restart the program.

# Original: 03 Sept 2019
# Edited: 24 November 2020

def triple(ab, c):
    if (ab[0]**2) + (ab[1]**2) == (c**2):
        print("The set is a Pythagorean Triple.")
    else:
        print("The set is not a Pythagorean Triple.")

''' ORIGINAL
# set the three values to a, b, and c such that c equals the largest number
c_index = num.index(max(num))
if c_index == 1:
    a = num[2]
else:
    a = num[1]
b = num[3 - (num.index(a)) - c_index]
c = num[c_index]
'''

while True:
    num = [x for x in input("Enter 3 numbers, delimited by a comma after each. Example: 1, 2, 3 \n").replace(" ", "").split(",")]
    while True:
        # error testing
        while True:
            try:
                num = [int(x) for x in num]
                break
            except ValueError:
                num = [x for x in input("Make sure you are entering numbers. Please try again. \n").replace(" ", "").split(",")]
        if len(num) == 3:
            break
        else:
            num = [x for x in input("There need to be three numbers. Please try again. \n").replace(" ", "").split(",")]
        
    # c is the largest number, a and b are the remaining items in the list
    c = max(num)
    num.remove(c)

    triple(num, c)

    num = input("If you would like to exit, please enter 'x'. Else, enter another set of numbers to check. \n")
    if num.lower() == "x":
        break


