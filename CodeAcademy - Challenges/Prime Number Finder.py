'''
Create a prime_finder() function that takes in a number, 
n, and returns all the prime numbers from 1 to n (inclusive). 

As a reminder, a prime number is a number that is only divisible 
by 1 and itself.

For example, prime_finder(11) should return [2, 3, 5, 7, 11].
'''

def prime_finder(n):
    primes = []
    for i in range(n + 1):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, (i // 2) + 1):
                if i % j == 0:
                    break
            else:
                primes.append(i)
    return primes

print(prime_finder(11))