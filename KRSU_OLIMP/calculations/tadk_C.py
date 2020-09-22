numbers = str(input())
result = ''
for number in numbers:
    result += number + ', '

result = result.strip(", ")
print(result)
