def perfect_numbers(number):
    re = []
    number = int(number)
    if 0 < number <= 100000:
        for n in range(1, number):
            if number % n == 0:
                re.append(n)
        if sum(re) == number:
            return 'YES'
        elif sum(re) != number:
            return 'NO'


a = int(input())
perfect_numbers(a)


def perfect_numbers2(number):
    test = [6, 28, 496, 8128]
    number = int(number)
    if 1 <= number <= (10 ** 10):
        if test.count(a) > 0:
            print('YES')
        else:
            print('NO')


a = int(input())
perfect_numbers2(a)
