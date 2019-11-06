# 19 October 2019
# Fibonacci + Factorial

def fibonacci(num):
    if num == 1:
        return(0)
    elif num == 2:
        return(1)
    elif num <= 0:
        return("Go fuck yourself.")
    else:
        return(fibonacci(num-2) + fibonacci(num-1))
        
def factorial(num):
    if num == 0:
        return(1)
    else:
        return(num*factorial(num-1))
