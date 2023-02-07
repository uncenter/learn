import string
letters = string.ascii_lowercase

freq = {}
for char in input("Enter a string: ").lower():
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(freq)
