num = int(input())
wrong = ''
for i in str(num):
    if str(num).count(i) > 1:
        wrong = 'YES'
        break
    else:
        wrong = 'NO'
print(wrong)
