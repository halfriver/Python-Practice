# Problem 12: Fibonacci Sequence + Factorial
 # Define a function that allows the user to find the value of the nth term in the sequence.
 # To make sure you've written your function correctly, test the first 10 numbers of the sequence.
 # You can assume either that the first two terms are 0 and 1 or that they are both 1.
 # There are two methods you can employ to solve the problem. One way is to solve it using a loop and the other way is to use recursion.
 # Try implementing a solution using both methods.

# Original: 19 October 2019
# Edited: 26 November 2020

n = input("Give a number and we'll find that nth term in the Fibonacci sequence.").replace(" ", "")
# input must be a whole number and cannot be negative

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
