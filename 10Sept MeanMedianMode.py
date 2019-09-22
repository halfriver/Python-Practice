# 10 Sept 2019
# Mean, Median, Mode

import math

num_list = input("Provide a list of numbers separated by commas and spaces. \n")
num = [int(x) for x in num_list.split(", ")]


def mean(num):
    mean = 0
    for x in range(0, len(num)):
        mean += num[x]
    mean /= len(num)
    return float(mean)

def median(num):
    median = 0
    if len(num) % 2 == 0:
        x = math.ceil(len(num)/2)
        y = x - 1
        median = float((num[x] + num[y])/2)
        return median
    else:
        median = num[math.floor(len(num)/2)]
        return median

def mode(num):
    mode_count = 1
    mode = []
    for x in range(0, len(num)):
        if num.count(num[x]) > mode_count:
            mode_count = num.count(num[x])
            mode = [num[x]]
        elif num.count(num[x]) == mode_count and num[x] not in mode:
            mode.append(num[x])
    return (mode, mode_count)

print("Mean: " + str(round(mean(num), 2)) + "\nMedian: " + str(median(num)) + "\nMode: " + str(mode(num)[0]) + " which occur(s) " + str(mode(num)[1]) + " times")
