def calculate(vTable, verbose = False):
    pTable = []
    nSize = len(vTable)
    kSize = (int)(len(vTable[0]) / 2)

    for n in range(nSize):
        tableRow = []
        sumValue = 0
        powerValue = 2 ** n
        for T0 in range (kSize * 2, kSize - 1, -1):
            sumValue += vTable[n][T0]
            p = sumValue / powerValue
            tableRow.insert(0, p)
        pTable.append(tableRow)

        if verbose:
            print(n)

    if verbose:
        print("done calculating V values")

    return pTable
