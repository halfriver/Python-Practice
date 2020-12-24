'''
Problem 8 - Change Calculator
- Create a program that allows them to input a certain amount of change, and
then print how many quarters, dimes, nickels, and pennies are needed to make up
the amount needed.
- Example: If they input “1.47”, the program will say that he needs 5
quarters, 2 dimes, 0 nickels, and 2 pennies.
- In addition, to save your friend from needing to calculate the change, allow
them to enter the amount given to them and the purchase amount so that you can
calculate the change yourself.
- Make sure that you handle pluralization correctly.
- Allow your friend to either enter another dollar amount or quit.
- Strip out “$” characters and gracefully notify the user of any errors with
their input (i.e. handle inputs like “$0.37”, “1>78”, or “fish”)
'''

# Original: 8 Sept 2019
# Edited: 25 November 2020

# check that input is an int
value = input("What's the dollar amount?\n").replace(" ", "").replace("$", "")
while True:
    try:
        value = [int(x) for x in value.split(".")]
        # make sure decimal converts correctly to cents
        if len(value) == 2:
            if value[1] < 10:
                value[1] *= 10
        break
    except ValueError:
        value = input("Please input an integer.\n").replace(" ", "").replace("$", "")

# denomination
dollars = [(20, "$20 bills"), (10, "$10 bills"), (5, "$5 bills"), (1, "$1 bills")]
cents = [(25, "quarters"), (10, "dimes"), (5, "nickels"), (1, "pennies")]
# bill and coin amounts
bills = [0, 0, 0, 0]
coins = [0, 0, 0, 0]

# bill amounts
for x in range(len(bills)):
    while True:
        if value[0] - dollars[x][0] >= 0:
            bills[x] += 1
            value[0] -= dollars[x][0]
        else:
            bills[x] = str(bills[x])
            break
    print(bills[x] + " " + dollars[x][1])

# coin amounts
if len(value) == 2:
    for x in range(len(coins)):
        while True:
            if value[1] - cents[x][0] >= 0:
                coins[x] += 1
                value[1] -= cents[x][0]
            else:
                coins[x] = str(coins[x])
                break
        print(coins[x] + " " + cents[x][1])
