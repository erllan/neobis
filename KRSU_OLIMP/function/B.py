def allSum(a):
    if 1 <= int(a) <= 10 ** 9:
        sum = 0
        revers = []
        res = ''
        for i in a:
            sum += int(i)
            revers.append(i)
        for i in reversed(revers):
            res += i + '+'
        print(f"{res.strip('+')}={sum}")


a = input()
allSum(a)
