array = []
count = int(input())
if 1 <= count <= 100000:
    for _ in range(count):
        number = int(input())
        array.append(number)
    a = sorted(array)
    for i in a:
        print(i)

