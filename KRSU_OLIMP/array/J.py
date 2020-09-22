n = input()
res = n.strip('0')
test = int(res[0]) % 2
test2 = int(res[-1]) % 2

if 0 <= len(n) <= 30000 and 0 <= int(res) <= 10 ** len(res):
    if test == 0 and test2 == 0 and int(res[0]) // 2 == int(res[-1]) // 2 and len(res) % 2 == 0:
        print('lucky')
    else:
        print('unlucky')
