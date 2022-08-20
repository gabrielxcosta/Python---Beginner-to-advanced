'''
PROBLEM:
Create a fib_finder() function that finds the nth number 
in the Fibonacci sequence. As a reminder, the Fibonacci 
sequence is a mathematical sequence that begins with 0 and
1, with each following term being the sum of the two previous terms.

For example, the first two terms of the sequence are represented by 
fib_finder(1) and fib_finder(2), which return 0 and 1, respectively. 
fib_finder(6) should return 5.
'''
def fib_finder(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n - 1]

print(f'Prime finded: {fib_finder(6)}')