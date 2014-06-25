def calculate(n, verbose = False):
    vTable = []
    nSize = n + 1
    kSize = calculateK(nSize)

    for n in range (nSize):
        tableRow = []
        for T0 in range (kSize * 2 + 1):
            tableRow.append(V(n, T0 - kSize, kSize, vTable))
        vTable.append(tableRow)

        if verbose:
            print(n)

    if verbose:
        print("done calculating V values")

    return vTable

def calculateK(nSize):
    kSize = 0
    for n in range (nSize):
        kSize += n
    return kSize

def V(n, k, kSize, vTable):
    if((n == 1 and (k == 1 or k == -1)) or (n == 0 and k == 0)):
        return 1
    if((k < -(n * (n + 1) / 2)) or (k > (n * (n + 1) / 2))):
        return 0
    n = n - 1

    kIndex =  k + kSize

    leftValue = 0 if kIndex - n - 1 < 0 or kIndex - n - 1 >= len(vTable[n]) else vTable[n][kIndex - n - 1]
    rightValue = 0 if kIndex + n + 1 < 0 or kIndex + n + 1 >= len(vTable[n]) else vTable[n][kIndex + n + 1]

    return leftValue + rightValue
