def re(numbs):
    numbs = str(numbs)
    res = ''
    if 1 <= int(numbs) <= 10 ** 9:
        for i in range(len(numbs) - 1, -1, -1):
            res += numbs[i]
        print(int(res))


a = input()
re(a)
