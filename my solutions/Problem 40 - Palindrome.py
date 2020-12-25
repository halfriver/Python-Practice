'''
Problem 40 - Palindrome
- Palindrome means anything that reads the same backwards as forwards.
- Write a program to check if a number is a palindrome or not.
'''

# Original: 24 November 2020


def palindrome(num):
    num_inv = ""
    for i in range(len(num)):
        num_inv += num[(len(num)-1)-i]
    if num == num_inv:
        print(num_inv + " is a palindrome of " + num_inv + ".\n")
    else:
        print(num_inv + " is not a palindrome of " + num_inv + ".\n")


num = str(input("Input a number to see if it is a palindrome.\n").replace(" ", "")).lower()

while True:
    palindrome(num)
    num = str(input("If you'd like to check another number, enter it now. If you'd like to exit, enter 'x'.\n").replace(" ", "")).lower()
    if num.lower() == "x":
        break
