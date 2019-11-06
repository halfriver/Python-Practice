# Factors of a Number
# 4 Nov 2019

def factor(x):
    factors = []
    for num in range(1,x+1):
        if x % num == 0:
            factors.append(num)
    return factors

x = int(input("Type a number.\n"))

factors = factor(x)

if len(factors) == 2:
    print("The factors of " + str(x) + " are " + str(factors) + ". It is a prime number.")
else:
    print("The factors of " + str(x) + " are " + str(factors))
