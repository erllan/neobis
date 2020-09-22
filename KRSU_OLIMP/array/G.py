n = input()
array = ''
a = input().split(' ')
if len(a) == int(n):
    for i in range(len(a) - 1, -1, -1):
        array += a[i]+' '
    print(array.strip())
