# Problem 12: Fibonacci Sequence + Factorial
 # Define a function that allows the user to find the value of the nth term in the sequence.
 # To make sure you've written your function correctly, test the first 10 numbers of the sequence.
 # You can assume either that the first two terms are 0 and 1 or that they are both 1.

# Original: 19 October 2019
# Edited: 26 November 2020

def fibonacci(num):
    if num == 1:
        return(0)
    elif num == 2:
        return(1)
    else:
        return(fibonacci(num-2) + fibonacci(num-1))

# just an unrelated factorial function to practice recursion
def factorial(num):
    if num == 0:
        return(1)
    else:
        return(num*factorial(num-1))

# input must be a whole number and cannot be negative
while True:
    try:
        n = int(input("Give a number and we'll find that nth term in the Fibonacci sequence.\n").replace(" ", ""))
        if n < 1:
            print("Please give a positive number.")
            continue
        break
    except:
        print("This is not a valid number, please try again.")

print("The " + str(n) + "th term of the Fibonacci sequence is " + str(fibonacci(n)) + ".")
