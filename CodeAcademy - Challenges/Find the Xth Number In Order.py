'''
Write a function, getX, that given an integer x and a list 
nums returns the Xth number if the list was in sorted order. 
In other words, the Xth smallest number.

Function Name: getX

Input: An integer, x, and an unsorted list of integers nums that aren’t 
necessarily distinct.

Output: The integer corresponding to the Xth number in the sorted list

Note that this assumes the first number is position 1, not 0. 
If the input x is greater than the length of the list, or nums 
is empty, return 0.

Attempt a solution as close to linear O(n) (where n is the length of nums) 
time as possible.
'''
def getX(x, nums):
    if x > len(nums) or nums == []:
        return 0
    nums.sort(reverse=False)
    for index, value in enumerate(nums):
        if (index + 1) == x:
            return value

print(getX(2, [6, 3, -1, 5]))