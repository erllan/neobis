n = int(input())
array = input().split()
if len(array) == n and n >= 2 and len(array) <= 2000000000:
    minNumber = min(array)
    re = []
    for i in array:
        if int(i) != int(min(array)):
            re.append(int(i))
    minNumber2 = min(re)
    print(minNumber, minNumber2)

