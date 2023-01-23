# ----- Problem ----- #
# Multiples of 3 or 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# ----- Result ----- #
# Answer: 233168
# Time: 0.212976ms
# Tries: 2
# ->  First Answer: 266333
#     - Forgot to break out of the inner loop, multiples of both 3 and 5 were being added twice.
# ->  Second Answer: 233168
#     - Added break statement to inner loop (l.22),

# ----- Result ----- #
def sum_of_multiples(limit, *multiples):
    sum = 0
    for i in range(limit):
        for n in multiples:
            if i % n == 0:
                sum += i
                break
    return sum

print(sum_of_multiples(1000, 3, 5))