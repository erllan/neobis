num = int(input())
res = 0

if 1 <= num <= 10 ** 9:
    for key, value in enumerate(str(num)):
        if key % 2 == 1:
            res += int(value)
    print(res)
