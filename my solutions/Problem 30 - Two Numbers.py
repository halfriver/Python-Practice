# Problem 30: Two Numbers
 # Given an array of integers, return indices of the two numbers such that they add up to a specific target.
 # You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Original: 10 December 2020

# test values
'''
int_array = [2, 3, 7, 16]
target = 9
'''

# input int array
while True:
    try:
        int_array = [int(x) for x in input("Please enter a list of numbers separated by commas.\n").replace(" ","").split(",")]
        if len(int_array) < 2:
            raise IndexError
        break
    except ValueError:
        print("This was not in the correct format. Please try again.\n")
    except ValueError:
        print("There must be at least 2 numbers in the list in order for this to work.\n")

# input target
while True:
    try:
        target = int(input("What is the target value that you would like two numbers from the array to sum to?\n").replace(" ",""))
        break
    except:
        print("Something wasn't right. Please enter a number.\n")

# iterate to compare and add
def two_num(array, target):
    for x in range(len(array)):
        for y in range(len(array)):
            if x != y and array[x]+array[y] == target:
                return print(str(array[x]) + " (index " + str(array.index(array[x])+1) + ") and " + str(array[y]) + " (index " + str(array.index(array[y])+1) + ") add up to equal " + str(target) + ".")
        else:
            return print("There is no pair of values in the array " + str(array) + " that you provided that equals " + str(target) + ".\n")
    
two_num(int_array, target)
