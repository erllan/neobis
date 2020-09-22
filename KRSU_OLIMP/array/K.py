array = input().split()
sumArray = 0
if len(array) <= 1000:
    for i in array:
        sumArray += int(i)
print(sumArray)
