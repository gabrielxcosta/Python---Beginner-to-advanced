'''
PROBLEM:
You have a bag containing tiles with numbers [1, 2, 3, …, n] 
written on them. Each number appears exactly once, so there 
are n tiles and n numbers. Now, without looking, k number 
tiles are randomly picked out of the bag and discarded. Create 
a missing_nos() function that takes in a list and k, and returns
the missing numbers in ascending order (from smallest to greatest).

For example, missing_nos([1, 2, 4, 5, 6, 7, 8, 10], 2) should 
return [3, 9].
'''
def missing_nos(array, k):
    aux = set(i + 1 for i in range(array[-1]))
    missing_values = []
    for value in aux:
        if value not in array:
            missing_values.append(value)
    return missing_values

print('Missing values in the list:', missing_nos([1, 2, 4, 5, 6, 7, 8, 10], 2))