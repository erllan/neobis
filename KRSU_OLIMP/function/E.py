def Mutually_simple(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    gcd = a + b
    if gcd == 1:
        return 'YES'
    else:
        return 'NO'


a, b = input().split(' ')

Mutually_simple(int(a), int(b))
