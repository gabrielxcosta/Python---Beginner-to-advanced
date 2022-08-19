'''
PROBLEM:
Create a stats_finder() function that takes in a list of numbers and returns
a list containing the mean and mode, in that order. As a reminder, the mean 
is the average of the values and the mode is the most occurring value. If 
there are multiple modes, return the mode with the lowest value. Make sure
that you write your functions and find these answers from scratch – don’t 
use imported tools!

For example, stats_finder([500, 400, 400, 375, 300, 350, 325, 300]) should 
return [368.75, 300].
'''
def stats_finder(array):
    mean = sum(array) / len(array)
    largestCount = 0
    modes = []
    for value in array:
        if value in modes:
            continue
        count = array.count(value)
        if count > largestCount:
            del modes[:]
            modes.append(value)
            largestCount = count
        elif count == largestCount:
            modes.append(value)
    return [mean, min(modes)]

print(stats_finder([500, 400, 400, 375, 300, 350, 325, 300]))