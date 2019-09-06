# 05 Sept 2019
# Coin Estimator by Weight

import math

grams = False
pounds = False
while grams == False and pounds == False:
    g_lb = input("Will you be submitting the weights in grams or pounds? Please type 'pounds' or 'lbs' for imperial, 'grams' or 'g' for metric. \n")
    if g_lb == "pounds" or g_lb == "lbs":
        pounds = True
    elif g_lb == "grams" or g_lb == "g":
        grams = True

cont = False
while cont == False:
    weight_input = input("Please enter how much each type of coin weighs, separated by spaces and commas in the order as follows: \n" + "Penny, Nickel, Dime, Quarter, Half-Dollar, Dollar \n")
    weights = weight_input.split(", ")  
    if len(weights) == 6:
        cont = True

for x in range(0, 6):
    weights[x] = float(weights[x])
    if pounds:
        weights[x] = (weights[x])*453.592

coins = [
         math.floor((weights[0])/2.5),
         math.floor((weights[1])/5.0),
         math.floor((weights[2])/2.268),
         math.floor((weights[3])/5.670),
         math.floor((weights[4])/11.34),
         math.floor((weights[5])/8.1)
         ]

wrappers = [
            math.floor((coins[0])/50),
            math.floor((coins[1])/40),
            math.floor((coins[2])/50),
            math.floor((coins[3])/40),
            math.floor((coins[4])/20),
            math.floor((coins[5])/25)
            ]

for x in range(0, 6):
    coins[x] = str(coins[x])
    wrappers[x] = str(wrappers[x])

print("You have " + coins[0] + " pennies, " + coins[1] + " nickels, " + coins[2] + " dimes, " + coins[3] + " quarters, " + coins[4] + " half-dollars, and " + coins[5] + " dollar coins in total.\n" +
      "These will fill " + wrappers[0] + " penny wrappers, " +  wrappers[1] + " nickel wrappers, " + wrappers[2] + " dime wrappers, " + wrappers[3] + " quarter wrappers, " + wrappers[4] + " half-dollar wrappers, and " + wrappers[5] + " dollar wrappers.")
