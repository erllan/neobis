N = int(input())
array = input().split()
C = input()
indexCount = 0
if len(array) == N:
    for i in array:
        indexCount += 1
        if i == C:
            print(indexCount)
