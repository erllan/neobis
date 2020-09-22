numb = int(input())
allSum = []
if numb >= 0:
    for i in str(numb):
        allSum.append(int(i))
    print(sum(allSum))
