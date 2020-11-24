# Problem 6: Coin Estimator by Weight
 # Allow the user to input the total weight of each type of coin they have (pennies, nickels, dimes, and quarters).
 # Print out how many of each type of coin wrapper they would need, how many coins they have, and the estimated total value of all of their money.
 # Subgoals: Round all numbers printed out to the nearest whole number and allow the user to select whether they want to submit the weight in either grams or pounds.

# Original: 05 Sept 2019
# Edited: 24 November 2020

# given per-coin weight (g), wrapper capacity, value, and name of each coin type
coins = [(2.5, 50, 0.01, "Penny      "), (5.0, 40, 0.05, "Nickel     "), (2.268, 50, 0.10, "Dime       "), (5.670, 40, 0.25, "Quarter    "), (11.34, 20, 0.50, "Half-Dollar"), (8.1, 25, 1.00, "Dollar Coin")]

# choose grams or pounds
grams = False
pounds = False
while grams == False and pounds == False:
    g_lb = input("Will you be submitting the weights in grams or pounds? Please type 'pounds' or 'lbs' for imperial, 'grams' or 'g' for metric. \n")
    if g_lb == "pounds" or g_lb == "lbs":
        pounds = True
    elif g_lb == "grams" or g_lb == "g":
        grams = True

while True:
    weights = [int(x) for x in input("Please enter the total weight of each coin type, separated by commas in the order as follows: \n" + "Penny, Nickel, Dime, Quarter, Half-Dollar, Dollar \n").replace(" ", "").split(",")]
    if len(weights) == 6:
        break

wrappers = []
value = []

print("")
for x in range(len(weights)):
    # convert to grams if not already
    if pounds:
        weights[x] = weights[x]*453.592

    # recalcuate weights to determine number of coins per category
    weights[x] = weights[x]//coins[x][0]

    # populate wrappers and value lists
    wrappers.append(weights[x]//coins[x][1])
    value.append(weights[x]*coins[x][2])

    # cast as strings
    weights[x] = str(int(weights[x]))
    wrappers[x] = str(int(wrappers[x]))

    # print output
    if weights[x] != 0:
        print(coins[x][3] + ": " + weights[x] + " coins fills a total of " + wrappers[x] + " wrappers")
        
print("The total value of your coins is $" + str(sum(value)) + ".\n")


