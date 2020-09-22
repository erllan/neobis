from math import sqrt

X1, Y1 = input().split(' ')
X2, Y2 = input().split(' ')
answer = sqrt((float(X1) - float(X2)) ** 2 + (float(Y1) - float(Y2)) ** 2)
print(float("{:.3f}".format(answer)))
