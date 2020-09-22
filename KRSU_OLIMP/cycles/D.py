def fib(n):
    if n == 0:
        return 0
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b


end = int(input())
if end < 0:
    print("ERROR")
else:
    count = 0
    sum = 0
    while fib(count) < end:
        sum += fib(count)
        count += 1
    print(sum)
