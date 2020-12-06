# Problem 16: Menu Calculator
 # To quickly take orders, your program should allow the user to type in a string of numbers and then it should calculate the cost of the order.
 # For example, if one large drink, two small drinks, two hamburgers, one hotdog, and a salad are ordered, the user should type in 5993348, and the program should say that it costs $19.50.
 # Also, make sure that the program loops so the user can take multiple orders without having to restart the program each time.
 # If you decide to, print out the items and prices every time before the user types in an order.
 # Once the user has entered an order, print out how many of each item have been ordered, as well as the total price.
 # If an item was not ordered at all, then it should not show up.

# Original: 12 November 2019
# Edited: 6 December 2020

register = 0

# take multiple orders without restarting program
while True:
   print("Welcome to the Food Place! Please buy our food!\nHere's our menu:")
   menu = ["Chicken Strips", "French Fries", "Hamburger", "Hotdog", "Large Drink", "Medium Drink", "Small Drink", "Milk Shake", "Salad"]
   prices = [3.50, 2.50, 4.00, 3.50, 1.75, 1.50, 1.25, 2.25, 3.75]
   order = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
   for x in range(len(menu)):
      print(str(x+1) + ": " + str(menu[x]) + " $" + str(prices[x]))
   
   # take initial order
   add = str(input("Add to your order using the numbers of the above menu items.\n"))
   for x in range(len(order)):
      order[x] += add.count(str(x+1))

   # keep an order open until the customer is ready to check out
   while True:
      # print current order
      text = "Your order consists of:"
      for x in range(len(order)):
         if order[x] > 0:
            text += "\n    " + str(order[x]) + "  " + menu[x]
      print(text)

      # options to edit order
      done = input("Is this correct? Type 'r' to remove, 'a' to add to the order. If ready to check out, type 'c'.\n").lower()
      if done not in ["a", "r", "c"]:
         print("Input not accepted. Try again.")
      elif done == "r":
         remove = input("What items would you like to remove?\n")
         for x in range(len(menu)):
            if order[x] > 0:
               order[x] -= remove.count(str(x+1))
      elif done == "a":
         add = input("What would you like to add to your order?\n")
         for x in range(len(menu)):
            order[x] += add.count(str(x+1))
      else:
         break

   # total cost calculation, print receipt
   subtotal = 0
   for x in range(len(order)):
       if order[x] > 0:
           print(str(order[x]) + " " + str(menu[x]) + " @ $" + str(round(prices[x], 2)) + " each \n        $" + str(round(order[x]*prices[x], 2)))
           subtotal += order[x]*prices[x]
   tax = round(round(subtotal, 2)*0.08, 2)
   total = round(subtotal, 2) + tax
   register += total
   print("Subtotal: $" + str(round(subtotal, 2)) + "\nTax: $" + str(tax) + "\nTotal: $" + str(round(total, 2)) + "\n\nThanks for your order!\n")

   # prompt cashier to close or continue
   if input("Enter 'x' to close out of register, or any other character to continue to next order.\n").lower() == 'x':
      break

print("Closing out. Your sales for this session totaled $" + str(round(register, 2)) + ".")


