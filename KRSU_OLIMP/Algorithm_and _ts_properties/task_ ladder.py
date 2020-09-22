listWord = input().split(' ')
if len(listWord) <= 100:
    space = 0
    for key, value in enumerate(listWord):
        if key == 0:
            space = len(value)
            print(value)
        else:
            result = ' ' * space + value
            space = len(result)
            print(result)
