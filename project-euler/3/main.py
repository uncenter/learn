# ----- Problem ----- #
# Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

# ----- Result ----- #
# Answer: 6857 [71, 839, 1471, 6857]
# Time: 69.58125ms
# Tries: many

# ----- Code ----- #

def main(num):
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
    factors_prime = []
    factors = list_factors(num)
    for factor in factors:
        if check_prime(factor) and factor != 1:
            factors_prime.append(int(factor))
    print(factors_prime)

main(600851475143)