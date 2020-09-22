n = input()
array = []
a = input().split(' ')
if len(a) == int(n):
    for i in a:
        array.append(int(i))
    print(max(array), array.count(max(array)))


