def taskD(x, y, z):
    test = [x, y, z]
    if test.count(0) > 1:
        return 0
    else:
        return 1


num = int(input())
count = 0
wrong = []
while count < num:
    a, b, c = input().split()
    wrong.append(taskD(int(a), int(b), int(c)))
    count += 1

for i in wrong:
    print(int(i))
