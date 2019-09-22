# Change Calculator
# 8 Sept 2019

total = input("What's the dollar amount? \n")
amount = [int(x) for x in total.split(".")]

dollars = [20, 10, 5, 1]
bills = [0, 0, 0, 0]
cents = [25, 10, 5, 1]
coins = [0, 0, 0, 0]

for x in range(0,4):
    while True:
        if amount[0] - dollars[x] >= 0:
            bills[x] += 1
            amount[0] -= dollars[x]
        else:
            break

for x in range(0,4):
    while True:
        if amount[1] - cents[x] >= 0:
            coins[x] += 1
            amount[1] -= cents[x]
        else:
            break

print(str(bills[0]) + " $20 bills \n" + str(bills[1]) + " $10 bills \n" + str(bills[2]) + " $5 bills \n" + str(bills[3]) + " $1 bills")  
print(str(coins[0]) + " quarters \n" + str(coins[1]) + " dimes \n" + str(coins[2]) + " nickels \n" + str(coins[3]) + " pennies \n")
