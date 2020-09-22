a, b = input().split()
s = 0
count = 0
if int(a) == 0 and int(b) < 0:
    print(f'{a}*({b})=0')
elif int(a) == 0 and int(b) > 0:
    print(f'{a}*{b}=0')
else:
    while count < abs(int(b)):
        count += 1
        s += int(a)
    if int(b) < 0 and int(a) < 0:
        s = abs(s)
        print(f'{a}*({b}) ={s}')
    elif (int(b) < 0) and (int(a) > 0) or (int(a) < 0) and (int(b) > 0):
        if s < 0:
            print(f'{a}*({b})={s}')
        else:
            s = 0 - s
            print(f'{a}*({b})={s}')
    else:
        print(f'{a}*{b}={s}')
