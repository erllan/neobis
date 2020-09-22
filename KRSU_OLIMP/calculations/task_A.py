a, b, c = str(input()).split(' ')
arithmetical = (int(a) + int(b) + int(c)) / 3
print(str(f"{a}+{b}+{c}={int(a) + int(b) + int(c)}"))
print(str(f"{a}*{b}*{c}={(int(a) * int(b)) * int(c)}"))
if str(arithmetical)[2] == '0':
    arithmetical = int(arithmetical)
    print(f'({a}+{b}+{c})/3=' + str(arithmetical))
else:
    print(f'({a}+{b}+{c})/3=' + str(float('%.6f' % arithmetical)))
