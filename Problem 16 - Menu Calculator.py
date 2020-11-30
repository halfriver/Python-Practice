# Menu Calculator
# 12 November 2019

print("Welcome to the Food Place! Please buy our food!\nHere's our menu:")
menu = ["Plain Naan", "Garlic Naan", "Vegetable Korma", "Palak Paneer", "Chana Masala", "Chicken Korma", "Chicken Saag", "Goat Curry", "Lamb Biryani", "Mango Lassi"]
prices = [2.99, 2.99, 7.99, 7.99, 8.50, 8.99, 8.99, 9.99, 10.99, 2.50]
order = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in range(len(menu)):
   print(str(x) + ": " + str(menu[x]) + " $" + str(round(prices[x],2)))

# keep an order open until the customer is ready to check out
while True:
    # take order and parse through each part
    add = str(input("Add to your order using the numbers of the above menu items.\n"))
    for x in range(len(order)):
        order[x] = order[x] + add.count(str(x))

    while True:
        text = "Your order consists of:"
        for x in range(len(order)):
            if order[x] > 0:
                text = text + "\n    " + str(order[x]) + "  " + menu[x]
        print(text)
        done = input("Is this correct? Type 'r' to remove, 'a' to add to the order. If ready to check out, type 'c'.\n").lower()
        if done != "a" and done != "r" and done != "c":
            print("Try again:")
        elif done == "r":
            remove = input("What items would you like to remove?\n")
            for x in range(10):
                if order[x] > 0:
                    order[x] = order[x] - remove.count(str(x))
                #if order[x] < 0:
                 #   order[x] = 0
        else:
            break
    if done == "c":
        break

# total cost calculation, print receipt
subtotal = 0
for x in range(len(order)):
    if order[x] > 0:
        print(str(order[x]) + " " + str(menu[x]) + " @ $" + str(round(prices[x],2)) + " each \n        $" + str(round(order[x]*prices[x],2)))
        subtotal += order[x]*prices[x]
tax = round(round(subtotal,2)*0.08,2)
total = round(subtotal,2) + tax
print("Subtotal: $" + str(round(subtotal,2)) + "\nTax: $" + str(tax) + "\nTotal: $" + str(round(total,2)) + "\n\nThanks for your order!")


