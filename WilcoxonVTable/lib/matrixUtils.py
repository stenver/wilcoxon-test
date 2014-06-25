def read_V_table(fileName):
    table = []
    f = open("wilxdata/" + fileName)
    i = 0
    for line in f:
        tableRow = []
        splittedString = line.split(";")
        for s in splittedString:
            readyToConvert = s.replace("\n", "").replace(" ", "")
            if(readyToConvert != ""):
                tableRow.append(int(readyToConvert))
        table.append(tableRow)
        i += 1
    return table

def read_P_table(fileName):
    table = []
    f = open("wilxdata/" + fileName)
    i = 0
    for line in f:
        tableRow = []
        splittedString = line.split(";")
        for s in splittedString:
            readyToConvert = s.replace("\n", "").replace(" ", "")
            if(readyToConvert != ""):
                tableRow.append(float(readyToConvert))
        table.append(tableRow)
        i += 1
    return table

def write_V_table(table, vValuesFileName, verbose = False):
    with open("wilxdata/" + vValuesFileName, 'w') as f:
        nSize = len(table)
        kSize = len(table[0])
        for i in range(nSize):
            for j in range(kSize):
                f.write(str(table[i][j]))
                f.write("; ")
            f.write("\n")
            if(i%10 == 0 and verbose): print(i)
        if verbose:
            print("File created")


def write_P_table(table, fileName, verbose = False):
    with open("wilxdata/" + fileName, 'w') as f:
        nSize = len(table)
        kSize = len(table[0])
        for i in range(nSize):
            for j in range(kSize):
                f.write(str(table[i][j]))
                f.write(";")
            f.write("\n")
            if(i%10 == 0 and verbose): print(i)
        if verbose:
            print("File created")

def show(table, width = 10):
    nSize = len(table)
    kSize = (int)(len(table[0]) / 2)
    for n in range (-kSize, kSize + 1):
        print ('{0: {width}}'.format(n, width = width), end = '')
    print()
    for n in range (nSize):
        for T0 in range (kSize * 2 + 1):
            print ('{0: {width}}'.format(table[n][T0], width = width), end = '')
        print()
