num = int(input())
odd_numbers = 0
even_numbers = 0

if 1 <= num <= 10 ** 9:
    for value in (str(num)):
        if int(value) % 2 == 0:
            even_numbers += 1
        elif int(value) % 2 == 1:
            odd_numbers += 1
    print(odd_numbers, even_numbers)
