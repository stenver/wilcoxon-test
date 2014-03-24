import math
import pAccurateTable
import calculateGraphs
import calculateApproximateTable

__author__ = 'stenver'


pTable = []
gaussianPTable = []
nSize = 500
kSize = 0
for n in range (nSize):
    kSize += n
vValuesFileName = 'vTable' + str(nSize) + '.txt'
pValuesFileName = 'pTable' + str(nSize) + '.txt'
gaussianPValuesFileName = 'gaussianPvalues' + str(nSize) + '.txt'


def readFile(name):
    table = []
    #print("started to read " + str(name))
    f = open(name, 'r')
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
        #if(i%10==0): print(i)
    #print("finished reading " + str(name))


#Calculate the v and p tables. Create files
'''
pAccurateTable.kSize = kSize
pAccurateTable.nSize = nSize
vTable = pAccurateTable.calculateVValues()
#pAccurateTable.printVValues(vTable)
#pAccurateTable.createVValuesFile(vValuesFileName, vTable)

#vTable = readFile(vValuesFileName)
pTable = pAccurateTable.calculatePValues(vTable)
#pAccurateTable.printPValues(pTable)
#pAccurateTable.createPValuesFile(pTable, pValuesFileName)
'''

#Read the already calculated files in
gaussianPtable = readFile(gaussianPValuesFileName)
pTable = readFile(pValuesFileName)

#Do various calculations or graphs on the tables
'''
(table1, table2) = findWhenGaussianIsEffective(pTable, gaussianPtable)
table = findHighestApproximationError(pTable, gaussianPtable)
printHighestApproxPTable(table)

printPvsPdata(pTable, gaussianPTable, 50)
printPvsPdata(pTable, gaussianPTable, 25)

readFile(vValuesFileName, vTable)
calculateVtableStandardDeviations(vTable)
'''

#printKRelativeValues(499, pTable, gaussianPTable)

approximateTable = calculateApproximateTable.calculateApproximateTable(pTable, gaussianPtable)
calculateApproximateTable.writeApproximateTableFile(approximateTable, nSize)
