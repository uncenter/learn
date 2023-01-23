# ----- Problem ----- #
# Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# ----- Result ----- #
# Answer: 
# Time: __ms
# Tries: 

# ----- Code ----- #
from math import sqrt

def list_factors(n):
    if n % 2 == 0:
        step = 2
    else:
        step = 1
    factors = []
    for i in range(1, int(sqrt(n))+1, step):
        if n % i == 0:
            factors.append(i)
            factors.append(n//i)
    return factors

def check_prime(num):
    factors = list_factors(num)
    if len(factors) > 2:
        return False
    else:
        return True

def largest_prime_factor(num):
    prime_factors = []
    factors = list_factors(num)
    while True:
        prime_factors.append(factors[1])
        x = factors[-1]/factors[1]
        factors = list_factors(x)
        if check_prime(x):
            prime_factors.append(int(x))
            break
    return prime_factors

print(list_factors(13195))
print(largest_prime_factor(13195))