kSize = 0
nSize = 0

def V(n, k, vTable):
    if((n == 1 and (k == 1 or k == -1)) or (n == 0 and k == 0)):
        return 1
    if((k < -(n * (n + 1) / 2)) or (k > (n * (n + 1) / 2))):
        return 0
    n = n - 1

    kIndex =  k + kSize

    leftValue = 0 if kIndex - n - 1 < 0 or kIndex - n - 1 >= len(vTable[n]) else vTable[n][kIndex - n - 1]
    rightValue = 0 if kIndex + n + 1 < 0 or kIndex + n + 1 >= len(vTable[n]) else vTable[n][kIndex + n + 1]

    return leftValue + rightValue

def calculateVValues():
    vTable = []
    for n in range (nSize):
        tableRow = []
        for T0 in range (kSize * 2 + 1):
            tableRow.append(V(n, T0 - kSize, vTable))
        vTable.append(tableRow)
        print(n)
    print("done calculating V values")
    return vTable

def printVValues(vTable):
    for n in range (-kSize, kSize + 1):
        print ('{0: {width}}'.format(n, width = 10), end = '')
    print()
    for n in range (nSize):
        for T0 in range (kSize * 2 + 1):
            print ('{0: {width}}'.format(vTable[n][T0], width = 10), end = '')
        print()

def createVValuesFile(vTable, vValuesFileName):
    f = open(vValuesFileName, 'w')
    for i in range(nSize):
        for j in range(kSize * 2 + 1):
            f.write('{0: {width}}'.format(vTable[i][j], width = 15))
            f.write("; ")
        f.write("\n")
        if(i%10 == 0): print(i)
    f.close()
    print("File created")

def calculatePValues(vTable):
    pTable = []
    for n in range(nSize):
        tableRow = []
        sumValue = 0
        powerValue = 2**n
        for T0 in range (kSize * 2, kSize-1, -1):
            sumValue += vTable[n][T0]
            p = sumValue / powerValue
            tableRow.insert(0, p)
        pTable.append(tableRow)
        print(n)
    print("done calculating P values")
    return pTable

def printPValues(pTable):
    for n in range (kSize + 1):
        print ('{0: {width}}'.format(n, width = 20), end = '')
    print()

    for n in range (nSize):
        for T0 in range (kSize + 1):
            print ('{0: {width}}'.format(pTable[n][T0], width = 20), end = '')
        print()


def createPValuesFile(pTable, pValuesFileName):
    f = open(pValuesFileName, 'w')
    for i in range(nSize):
        for j in range(kSize + 1):
            f.write(str(pTable[i][j]))
            f.write(";")
        f.write("\n")
        if(i%10 == 0): print(i)
    f.close()
    print("File created")
