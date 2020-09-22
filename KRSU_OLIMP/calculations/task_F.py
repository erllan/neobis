import math

x1, y1, x2, y2, x3, y3 = input().split(' ')
A = ((float(x2) - float(x1)) ** 2 + (float(y2) - float(y1)) ** 2) ** 0.5
B = ((float(x3) - float(x1)) ** 2 + (float(y3) - float(y1)) ** 2) ** 0.5
C = ((float(x2) - float(x3)) ** 2 + (float(y2) - float(y3)) ** 2) ** 0.5
P = (A + B + C) / 2
Perimeter = float('%.6f' % (A + B + C))
S = float('%.6f' % math.sqrt(P * (P - A) * (P - B) * (P - C)))
print(Perimeter,  S)
