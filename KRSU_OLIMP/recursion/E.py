def sum_digits(num):
    if num > 9:
        return num % 10 + int(sum_digits(num // 10))
    else:
        return num


a = int(input())

revers = []
res = ''
for i in str(a):
    revers.append(i)
for i in reversed(revers):
    res += i + '+'
print(res.strip('+'))
print(sum_digits(a))
