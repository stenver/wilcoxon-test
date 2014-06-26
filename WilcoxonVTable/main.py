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


# Calculate the v and p tables. Create files

# vTable = vTable.calculate(n)

# matrixUtils.show_V_table(vTable)
# matrixUtils.write_V_table(vTable, vValuesFileName)

# vTable = matrixUtils.read_V_table(vValuesFileName)
# pTable = pTable.calculate(vTable)
# matrixUtils.show_P_table(pTable)
# matrixUtils.write_P_table(pTable, pValuesFileName)



# Read the already calculated files in

# gaussianPTable = matrixUtils.read_P_table(gaussianPValuesFileName)
# pTable = matrixUtils.read_P_table(pValuesFileName)



# Do various calculations or graphs on the tables

# (table1, table2) = findWhenGaussianIsEffective(pTable, gaussianPTable)
# table = findHighestApproximationError(pTable, gaussianPTable)
# printHighestApproxPTable(table)

# calculateGraphs.printPvsPdata(pTable, gaussianPTable, 50)
# calculateGraphs.printPvsPdata(pTable, gaussianPTable, 25)

# matrixUtils.read_V_table(vValuesFileName, vTable)
# calculateVtableStandardDeviations(vTable)

# calculateGraphs.printDifference(pTable, gaussianPTable, 49)
# calculateGraphs.printPandPapprox(pTable, gaussianPTable, 30)



# Calculate approximate table and write it

# approximateTable.printKRelativeValuesForR(50, pTable, gaussianPTable)
# table = approximateTable.calculate(pTable, gaussianPTable)
# approximateTable.write(table)

