'''
Problem 20 - What's My Number?
Between 1 and 1000, there is only 1 number that meets the following criteria:
- The number has two or more digits.
- The number is prime.
- The number does NOT contain a 1 or 7 in it.
- The sum of all of the digits is less than or equal to 10.
- The first two digits add up to be odd.
- The second to last digit is even and greater than 1.
- The last digit is equal to how many digits are in the number.
'''

# Original: 03 Nov 2019
# Edited: 29 November 2020

from math import sqrt, ceil


def isprime(x):
    for i in range(2, ceil(sqrt(x))):
        if x % i == 0:
            return True


def find():
    num_master = []

    # number has two or more digits and does not contain 1 or 7
    for num in range(1000):
        if ("1" not in str(num) and "7" not in str(num) and num > 10):
            num_master.append(str(num))

    remove = []
    for num in num_master:
        add = [int(digit) for digit in num]

        # the sum of all the digits is less than or equal to 10
        if sum(add) > 10:
            remove.append(num)

        # the first two digits add up to be odd
        elif (add[0] + add[1]) % 2 == 0:
            remove.append(num)

        # the second to last digit is even
        elif add[len(add)-2] % 2 != 0 or add[len(add)-2] == 0:
            remove.append(num)

        # the last digit is equal to how many digits are in the number
        elif add[len(add)-1] != len(add):
            remove.append(num)

        # the number is prime
        elif isprime(int(num)):
            remove.append(num)

    for num in remove:
        num_master.remove(num)

    print(num_master)
