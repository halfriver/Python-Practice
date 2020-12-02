# Problem 21: Factors of a Number
 # Define a function that creates a list of all the numbers that are factors of the user's number.
 # The numbers in your list should be sorted from least to greatest, and 1 and the original number should be included.
 # Remember to consider negative numbers as well as 0.

# Original: 4 Nov 2019

def factor(x):
    factors = []
    for num in range(1,x+1):
        if x % num == 0:
            factors.append(num)
    return factors

# repeatability
while True:
    # input handling: must be a number
    while True:
        try:
            x = int(input("Type a number.\n"))
            break
        except:
            print("Please enter a valid number.")

    # input might be zero, negative, or positive
    if x == 0:
        print("Every number is a factor of 0.\n")
    else:
        factors = factor(abs(x))
        # if negative, every positive factor has a negative counterpart
        if x < 0:
            neg_factors = []
            for i in factors:
                neg_factors.append(i*-1)
            factors.extend(neg_factors)
            factors = sorted(factors)

        # print results
        if len(factors) == 2:
            print("The factors of " + str(x) + " are 1 and " + str(x) + ". It is a prime number.\n")
        else:
            print_factors = ""
            for i in range(len(factors)):
                if i < len(factors)-1:
                    print_factors += str(factors[i]) + ", "
                else:
                    print_factors += "and " + str(factors[i])
            print("The factors of " + str(x) + " are " + print_factors + ".\n")

    # user can choose to go again or quit
    if input("Please enter 'x' to quit. If you would like to continue to find the factors of another number enter any other key.\n").lower().strip() == 'x':
        break
