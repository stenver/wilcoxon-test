import math
import sys
sys.path.append('lib')
import vTable
import pTable
import matrixUtils
import calculateGraphs
import approximateTable

__author__ = 'stenver'

n = 50

vValuesFileName = 'vTable' + str(n) + '.txt'
pValuesFileName = 'pTable' + str(n) + '.txt'
gaussianPValuesFileName = 'gaussianPvalues' + str(n) + '.txt'

#Calculate the v and p tables. Create files
'''
vTable = vTable.calculate(n)

matrixUtils.show(vTable)
matrixUtils.write_V_table(vValuesFileName, vTable)

vTable = matrixUtils.read_V_table(vValuesFileName)
pTable = pTable.calculate(vTable)
matrixUtils.show(pTable)
matrixUtils.write_P_table(pTable, pValuesFileName)
'''

#Read the already calculated files in
'''
gaussianPTable = matrixUtils.read_P_table(gaussianPValuesFileName)
pTable = matrixUtils.read_P_table(pValuesFileName)
'''

#Do various calculations or graphs on the tables
'''
(table1, table2) = findWhenGaussianIsEffective(pTable, gaussianPTable)
table = findHighestApproximationError(pTable, gaussianPTable)
printHighestApproxPTable(table)

calculateGraphs.printPvsPdata(pTable, gaussianPTable, 50)
calculateGraphs.printPvsPdata(pTable, gaussianPTable, 25)

matrixUtils.read_V_table(vValuesFileName, vTable)
calculateVtableStandardDeviations(vTable)

calculateGraphs.printDifference(pTable, gaussianPTable, 49)
calculateGraphs.printPandPapprox(pTable, gaussianPTable, 30)
'''

# Calculate approximate table and write it
'''
printKRelativeValues(499, pTable, gaussianPTable)
approximateTable = approximateTable.calculate(pTable, gaussianPTable)
calculateApproximateTable.write(approximateTable)
'''
