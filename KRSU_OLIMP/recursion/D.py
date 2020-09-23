def calculate(number, stp, res='', sum=0):
    if sum == (number ** stp):
        return res + str(number) + '*1' + '\n' + str(sum)
    else:
        res += str(number) + '*'
        if sum != 0:
            sum = sum * number
        else:
            sum = number * number
        return calculate(number, stp, res, sum)


a, b = input().split(' ')
print(calculate(int(a), int(b)))
