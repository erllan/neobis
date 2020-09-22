num = int(input())
wrong = ''
res = 0
for i in str(num):
    if i == res:
        wrong = 'YES'
        break
    else:
        wrong = 'NO'
    res = i
print(wrong)
