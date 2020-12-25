'''
Problem 2 - Armstrong Number
- Define a function that allows the user to check whether or not a given number
is an Armstrong Number (also known as a Narcissistic Number).
- Hint: To do this, first determine the number of digits of the given number.
Call that n. Then take every digit in the number and raise it to the nth power.
Sum them, and if your answer is equal to the original number then it is an
Armstrong Number.
- Tip: All single digit numbers are Armstrong numbers.
'''

# Original: 24 November 2020


def armstrong(n):
    n_sq = [int(x)**len(n) for x in n]
    if sum(n_sq) == int(n):
        print(str(n) + " is an Armstrong number.\n")
    else:
        print(str(n) + " is not an Armstrong number.\n")


# user inputs a number
n = input("Input a number to check if it is an Armstrong number.\n")
while True:
    while True:
        # check that input is a number; if not, retry
        try:
            int(n)
            break
        except ValueError:
            n = input("Not an integer, try again.\n")
    armstrong(n)

    # exit program or rerun
    n = input("Enter 'x' to quit. Enter another number to evaluate it.\n")
    if n == "x":
        break
