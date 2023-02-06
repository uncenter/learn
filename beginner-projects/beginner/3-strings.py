import string
vowels = 'aeiou'
input = input("Enter a string: ")
vowel = 0
consonant = 0
for char in input:
    if char in string.ascii_letters:
        if char.lower() in vowels:
            vowel += 1
        else:
            consonant += 1
    else:
        break
print(f"In the given string, there are {vowel} vowels and {consonant} consonants.")