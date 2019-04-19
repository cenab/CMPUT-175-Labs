def readList():
    numberlist = []
    n = input("Enter a set of numbers (separated by space): ")
    if n.isdigit() == True:
        numberlist.append(int(n))
    if n.isdigit() == False:
        numberlist = n.split()
        for i in range(len(numberlist)):
            numberlist[i] = float(numberlist[i])
        numberlist = sorted(numberlist)
    return numberlist

def calculateMean(numberlist):
    sumnumbers = 0
    if len(numberlist) > 1:
        for i in range(len(numberlist)):
            sumnumbers += numberlist[i]
    if len(numberlist) == 1:
        sumnumbers = numberlist[0]
    mean = float(sumnumbers) / len(numberlist)
    return mean

def calculateStandarDev(numberlist):
    sumnumbers = 0
    numberlist1 = []
    for i in range(len(numberlist)):
        sumnumbers = numberlist[i] + sumnumbers
    mean = float(sumnumbers) / len(numberlist)
    if len(numberlist) == 1:
        sumnumbers = numberlist[0]
        variance = float(sumnumbers) / (1)
    if len(numberlist) > 1:
        for i in range(len(numberlist)):
            numberlist1.append((numberlist[i] - mean)**2)
        sumnumbers = sum(numberlist1)
        variance = float(sumnumbers) / (len(numberlist) - 1)
    standartDev = variance ** 0.5
    return standartDev

numberlist = readList()
print(numberlist)
mean = calculateMean(numberlist)
standartDev = calculateStandarDev(numberlist)
print(mean)
print(standartDev)
