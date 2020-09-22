A, B = input().split()
numbers = []
for i in range(int(A), int(B) + 1):
    numbers.append(int(i))
    print(f'{i}*{i}={i * i}')
