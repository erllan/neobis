def taskD(a, b):
    test = [a, b]
    if test.count(1) == 1:
        return 1
    else:
        return 0


num = int(input())
count = 0
wrong = []
while count < num:
    a, b = input().split()
    wrong.append(taskD(int(a), int(b)))
    count += 1

for i in wrong:
    print(int(i))
