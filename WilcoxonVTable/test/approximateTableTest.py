import unittest
import sys
sys.path.append('../lib')
sys.path.append('helpers')
import approximateTable
import pTableServer
import gaussianPtableServer
import approximateTableServer

class vTest(unittest.TestCase):

  def test_linear_interpolate_when_points_horizontal(self):
    self.assertEqual(approximateTable.linearInterpolate(2, 3, 1, 1, 1), 1)

  def test_linear_interpolate_when_points_diagonal(self):
    self.assertEqual(approximateTable.linearInterpolate(2, 1, 3, 1, 3), 2)

  # http://www.isda.org/c_and_a/pdf/Linear-interpolation-example.pdf
  def test_linear_interpolate_when_points_diagonal_and_answer_float(self):
    self.assertEqual(approximateTable.linearInterpolate(45, 64, 35, 4.3944, 4.3313), 4.353058620689655)

  def test_calculate_approximate_table_when_n_is_2(self):
    calculation_result = approximateTable.calculate(pTableServer.get_table(2), gaussianPtableServer.get_table(2))
    self.assertEqual(calculation_result, approximateTableServer.get_table(2))

  def test_calculate_approximate_table_when_n_is_5(self):
    calculation_result = approximateTable.calculate(pTableServer.get_table(5), gaussianPtableServer.get_table(5))
    self.assertEqual(calculation_result, approximateTableServer.get_table(5))

  def test_write_approximate_table_size_correct(self):
    approxTable = approximateTableServer.get_table(5)
    approximateTable.write(approxTable)
    read_table = self.read_approximate_table()
    for i in range(5):
      mergedlist = self.merge_list(approxTable[i])
      for j in range(len(mergedlist)):
        self.assertEqual(mergedlist[j], read_table[i][j])

  def merge_list(self, big_list):
    mergedlist = []
    for j in big_list:
      mergedlist += j
    return mergedlist

  def read_approximate_table(self):
    f = open("approximateTable5.txt")
    table = []
    i = 0
    for line in f:
      tableRow = []
      splittedString = line.split(",")
      for s in splittedString:
        readyToConvert = s.replace("\n", "").replace(" ", "").replace("[", "").replace("]", "")
        if(readyToConvert != ""):
          tableRow.append(float(readyToConvert))

      table.append(tableRow)
      i += 1
    return table

if __name__ == '__main__':
  unittest.main()
