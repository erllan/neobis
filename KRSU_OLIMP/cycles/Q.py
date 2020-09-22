num = int(input())
res = ''
if 1 <= num <= 10 ** 9:
    for i in str(num):
        if int(i) % 2 == 1:
            res += i
    print(res)
