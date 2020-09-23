def GCD(a, b):
    x = a
    y = b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a

    gcd = a + b
    return f'GCD({x},{y})={gcd}'


a, b = input().split()

print(GCD(int(a), int(b)))
