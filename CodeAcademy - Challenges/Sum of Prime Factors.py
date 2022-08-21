'''
Create a sum_of_prime_factors() function that takes in an integer n 
and returns the sum of all of its prime factors. As a reminder, a prime 
number is a number whose only factors are one and itself. Therefore, a prime 
factor is a factor of a given number that itself is a prime number.

For example, sum_of_prime_factors(91) should return 20 since its prime 
factors are 13 and 7. 
'''
def sum_of_prime_factors(n):
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
    
    print(f'Primes: {primes}')

    primes_factors = []
    for factor in primes:
        if n % factor == 0:
            primes_factors.append(factor)
    
    print(f'{n} primes factors: {primes_factors}')

    return f'Sum: {sum(primes_factors)}'


print(sum_of_prime_factors(91))