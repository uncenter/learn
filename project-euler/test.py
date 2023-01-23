from math import sqrt

def list_factors_b(n):
    step = 2 if n%2 else 1
    factors_list = []
    for i in range(1, int(sqrt(n))+1, step):
        if n % i == 0:
            factors_list.append(i)
            factors_list.append(n//i)
    return factors_list

print(list_factors_b(600851475143))