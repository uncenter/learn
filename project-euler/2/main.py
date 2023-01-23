# ----- Problem ----- #
# Even Fibonacci numbers

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# ----- Result ----- #
# Answer: 4613732
# Time: 0.060892ms
# Tries: 1

# ----- Code ----- #
def even_fibonacci_nums(limit):
    sum = 0
    a, b = 0, 1
    while b < limit:
        a, b = b, a + b
        if b % 2 == 0:
            sum += b
    return sum


print(even_fibonacci_nums(4000000))