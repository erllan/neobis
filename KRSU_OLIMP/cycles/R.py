num = int(input())
res = ''
count = 0
if 1 <= num <= 10 ** 9:
    for i in str(num):
        count += 1
        if count != 1 and count != len(str(num)):
            res += i
    if int(res) == 0:
        print()
    else:
        print(int(res))
