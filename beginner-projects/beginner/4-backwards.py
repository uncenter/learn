input = input("Enter a string: ")
output = ''
for i in range(1, len(input)+1):
    output += input[-(i)]
print(output)
