numb = input().split(' ')
a = int(numb[0])
b = int(numb[1])
c = int(numb[2])
MaxNumb = max(numb)
countMin = {a: "Anton", b: 'Boris', c: 'Victor'}
if int(MaxNumb) == a and numb.count(MaxNumb) < 2:
    print('Anton')
elif int(MaxNumb) == b and numb.count(MaxNumb) < 2:
    print('Boris')
elif int(MaxNumb) == c and numb.count(MaxNumb) < 2:
    print('Victor')
elif numb.count(MaxNumb) == 2:
    print(countMin[min(countMin)])
else:
    print('Same age')
