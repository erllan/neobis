num = int(input())
delNum = int(input())
res = ''
if 1 <= num <= 10 ** 9:
    for i in str(num):
        if delNum != int(i):
            res += i
    print(res)
