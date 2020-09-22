N = int(input())
array = input().split()
C = input()
if len(array) == N:
    if array.count(C) >= 1:
        print("YES")
    else:
        print('NO')
