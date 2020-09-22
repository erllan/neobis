import random

a, b = input().split()
randomArray = []
indexArray = 0
b = int(b)
a = int(a) + 1
if 0 <= int(a):
    for _ in range(int(a) - 1):
        i = random.randrange(1, int(a))
        randomArray.append(i)
    print(*randomArray)
    for i in randomArray:
        if i == b:
            print(int(indexArray))
        indexArray += 1
