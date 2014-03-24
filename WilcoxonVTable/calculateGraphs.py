#TODO fix those methods - probably broke after moving stuff to separate files

def calculateVtableStandardDeviations(vTable):
    halfOfArraySize = int(math.floor(len(vTable[0])/2))
    for n in range (1, len(vTable)):
        tableRow = []
        E = 0
        N = 0
        for V in range(len(vTable[0])):
            if(vTable[n][V] != 0):
                x = vTable[n][V]
                E += ((V - halfOfArraySize) ** 2) * x
                N += x
        E = E / N
        tableRow.append(E)
        print(E)
    print("done calculating V values")

table1 = []
table2 = []
def findWhenGaussianIsEffective(pTable, gaussianPTable):
    table1 = []
    table2 = []
    for i in range(len(pTable)):
        x = 0;
        smallestP = 0
        for j in range(len(pTable[0])):
            if(pTable[i][j] != 0):
                errorPresentage = (abs(gaussianPTable[i][j] - pTable[i][j])/ gaussianPTable[i][j]) * 100
                if(errorPresentage < 50):
                    smallestP = pTable[i][j]
            elif(x == 1):
                table1.append(j - 1)
                table2.append(smallestP)
                x = 0
    return table1, table2

def findHighestApproximationError(pTable, gaussianPTable):
    nTable = []
    for i in range(len(pTable)):
        highestErrorList = []
        lowValue = 0.1
        highestApproximateError = 0
        for j in range(len(pTable[0])):

            p = pTable[i][j]
            if(p < lowValue):
                lowValue = lowValue / 10
                highestErrorList.append(highestApproximateError)
                highestApproximateError = 0
                if(p == 0):
                    break
            pApprox = gaussianPTable[i][j]
            errorPresentage = abs(pApprox - p)/ pApprox * 100
            if(errorPresentage > highestApproximateError):
                #print(p)
                #print(gaussianPTable[i][j])
                #print(errorPresentage)
                highestApproximateError = errorPresentage

        nTable.append(highestErrorList)
        if(i%10==0): print(i)
    return nTable

def printHighestApproxPTable(table, nTable):
    tableSize = len(table) - 1

    for i in range(len(table[tableSize])):
        number = 10 ** (i + 1)
        name = "kuni" + str(1 / (number))
        print(name + " <- c(", end="")
        first = True
        for j in range(len(table)):
            if(not first):
                print(", ", end="")

            if(len(table[j]) > i ):
                print(str(table[j][i]), end="")
            else:
                print("NA", end="")
            first = False
        print(")")

def printPvsPdata(Pexact, Papprox, n):
    print(len(Pexact[n]))
    print("pExact <- c(", end="")
    first = True
    for i in range(len(Pexact[n])):
        if(Pexact[n][i] == 0):
            break
        if(not first):
            print(", ", end="")
        print(Pexact[n][i], end="")
        first = False
    print(")")
    print("pApprox <- c(", end="")
    first = True
    for i in range(len(Papprox[n])):
        if(Pexact[n][i] == 0):
            break
        if(not first):
            print(", ", end="")
        print(Papprox[n][i], end="")
        first = False
    print(")")
