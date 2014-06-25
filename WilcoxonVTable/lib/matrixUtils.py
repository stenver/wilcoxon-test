def read(fileName):
    table = []
    f = open("wilxdata/" + fileName, 'r')
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

def write(table, fileName):
    f = open(fileName, 'w')
    nSize = len(table)
    kSize = len(table[0])
    for i in range(nSize):
        for j in range(kSize + 1):
            f.write(str(table[i][j]))
            f.write(";")
        f.write("\n")
        if(i%10 == 0): print(i)
    f.close()
    print("File created")

def show(table, width = 10):
    nSize = len(table)
    kSize = len(table[0])
    for n in range (-kSize, kSize + 1):
        print ('{0: {width}}'.format(n, width = width), end = '')
    print()
    for n in range (nSize):
        for T0 in range (kSize * 2 + 1):
            print ('{0: {width}}'.format(table[n][T0], width = width), end = '')
        print()
