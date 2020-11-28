# Problem 13: Base Jumper
 # Create a program that converts an integer to the specified base.
 # The program should ask for 3 inputs. The number to convert. The base the number is in. And the base to convert the number to.
 # The program should accept a base that is in the range of 2 to 16 inclusive.
 # Display the result to the user and ask if they want to exit or convert another number.

# Original: 26 November 2020

from math import log

def base_norm(num, base_i):
    if base_i == 10:
        return int(num)
    # convert to base 10 so that I can wrap my head around it
    temp = [digits.index(n.upper()) for n in reversed(num)]
    for i in range(len(temp)):
        temp[i] *= (base_i**i)
    return sum(temp)

def base_jump(num, base_f):
    if base_f == 10:
        return num
    conversion = [0]
    while num/base_f > base_f:
        conversion.append(num % base_f)
        num /= base_f
        print(conversion)
        print(num)
    print(conversion)
        

##def base_jump(num, base_f):
##    if base_f == 10:
##        return num
##    # assumes base 10, based off of previous function
##    conversion = [0]
##    while num/base_f**(len(conversion)-1) > base_f:
##        conversion.append(0)
##    for i in range(len(conversion)):
##        conversion[i] = num//base_f**(len(conversion)-1-i)
##        num -= base_f**(len(conversion)-1-i)
##        print(num)
##    print(conversion)

    
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "G", "F"]
q = ["What base is your number currently in?\n",
     "What number would you like to convert?\n",
     "What base would you like to convert this number to?\n"]
inputs = [0, "", 0]

####### get rid of this continue boolean >:0000
cont = True

for i in range(len(q)):
    while True:
        try:
            # inputs 1 and 3 must be ints
            if i != 1: 
                inputs[i] = int(input(q[i]).replace(" ", ""))
                # must be between 2 and 16 (inclusive)
                if (inputs[i] < 2 or inputs[i] > 16):
                    print("The base must be between 2 and 16.\n")
                    continue
                # if initial base and base to convert to are the same, prompt again 
                if i == 2 and inputs[0] == inputs[2]:
                    print("Your number is already in this base.\n")
                    continue
            # input 2 may contain A-F in addition to numerals, and it must be valid for the base entered
            elif i == 1:
                inputs[1] = input(q[1]).replace(" ", "")
                for digit in digits[inputs[0]:]:
                    if digit.lower() not in inputs[1].lower():
                        cont = True
                        continue
                    else:
                        print("This value does not exist in the base you specified. Try again.\n")
                        cont = False
                        break
                if cont == False:
                    continue
            break
        except ValueError: 
            print("That's not a valid number. Try again.\n")
        
base_jump(base_norm(inputs[1], inputs[0]), inputs[2])

