def gcd(a, b, counter):
    if a == 0 or b == 0:
        print("GCD(" + str(b) + ',' + str(a) + ')')
        return max(a, b)
    else:
        if counter != 1:
            print("GCD(" + str(b) + ',' + str(a) + ')')
        counter += 1
        if a > b:
            return gcd(a - b, b, counter)

        else:
            return gcd(a, b - a, counter)


a, b = input().split(' ')
a = int(a)
b = int(b)
if a > 0 and b > 0:
    print("GCD(" + str(a) + ',' + str(b) + ')=' + str(gcd(a, b, 1)))
