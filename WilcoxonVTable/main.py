import math
import sys
sys.path.append('lib')
import pAccurateTable
import calculateGraphs
import calculateApproximateTable

__author__ = 'stenver'


pTable = []
gaussianPTable = []
nSize = 9
kSize = 0
for n in range (nSize):
    kSize += n
vValuesFileName = 'vTable' + str(nSize) + '.txt'
pValuesFileName = 'pTable' + str(nSize) + '.txt'
gaussianPValuesFileName = 'gaussianPvalues' + str(nSize) + '.txt'


def readFile(name):
    table = []
    f = open("wilxdata/" + name, 'r')
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


#Calculate the v and p tables. Create files

pAccurateTable.kSize = kSize
pAccurateTable.nSize = nSize
vTable = pAccurateTable.calculateVValues()
for i in range(9):
    print(vTable[i])
'''
#pAccurateTable.printVValues(vTable)
#pAccurateTable.createVValuesFile(vValuesFileName, vTable)

#vTable = readFile(vValuesFileName)
pTable = pAccurateTable.calculatePValues(vTable)
#pAccurateTable.printPValues(pTable)
#pAccurateTable.createPValuesFile(pTable, pValuesFileName)
'''

#Read the already calculated files in
#gaussianPTable = readFile(gaussianPValuesFileName)
#pTable = readFile(pValuesFileName)

#Do various calculations or graphs on the tables
'''
(table1, table2) = findWhenGaussianIsEffective(pTable, gaussianPTable)
table = findHighestApproximationError(pTable, gaussianPTable)
printHighestApproxPTable(table)

printPvsPdata(pTable, gaussianPTable, 50)
printPvsPdata(pTable, gaussianPTable, 25)

readFile(vValuesFileName, vTable)
calculateVtableStandardDeviations(vTable)
'''

#calculateGraphs.printDifference(pTable, gaussianPTable, 49)
#calculateGraphs.printPandPapprox(pTable, gaussianPTable, 30)

#printKRelativeValues(499, pTable, gaussianPTable)
#approximateTable = calculateApproximateTable.calculateApproximateTable(pTable, gaussianPTable)
#calculateApproximateTable.writeApproximateTableFile(approximateTable, nSize)
