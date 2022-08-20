'''
PROBLEM:
Write a function, flatten_array(), that takes in a 2-dimensional 
array, flattens it into a 1-dimensional array, and returns it. You 
can assume that you will only be given one or two-dimensional arrays.

For example, flatten_array([1, 2, [3, 4, 5], 6, [7, 8], 9]) should 
return [1, 2, 3, 4, 5, 6, 7, 8, 9].
'''
def flatten_array(array):
    if isinstance(array, list):
        temp = []
        for element in array:
            temp.extend(flatten_array(element))
        return temp
    else:
        return [array]

print('Flattened array:', flatten_array([1, 2, [3, 4, 5], 6, [7, 8], 9]))