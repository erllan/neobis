num = int(input())
res = 0
if len(str(num)) % 2 == 0:
    lenNum = len(str(num)) // 2
else:
    lenNum = len(str(num))
if 1 <= num <= 10 ** 9:
    for i in range(lenNum):
        res += int(str(num)[i])
    print(res)
