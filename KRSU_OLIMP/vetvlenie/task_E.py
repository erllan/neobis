numb = input().split(' ')
minA = min(numb)
if numb.count(minA) > 1:
    print("NO")
elif int(minA) == 0:
    print("NO")

else:
    print("YES")
