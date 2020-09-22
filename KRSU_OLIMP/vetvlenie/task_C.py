numb = input().split(' ')
if numb.count(numb[0]) >= 2:
    print(numb.count(numb[0]))
elif numb.count(numb[1]) >= 2:
    print(numb.count(numb[1]))
elif numb.count(numb[2]) >= 2:
    print(numb.count(numb[2]))
else:
    print(1)
