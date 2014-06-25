import unittest
import sys
sys.path.append('../lib')
sys.path.append('helpers')
import matrixUtils
import vTableServer
import pTableServer

class vTest(unittest.TestCase):

  def test_V_write_read(self):
    fileName = "temp.txt"
    matrixUtils.write_V_table(vTableServer.get_table(5), fileName)
    self.assertTrue(matrixUtils.read_P_table(fileName) == vTableServer.get_table(5))

  def test_P_write_read(self):
    fileName = "temp.txt"
    matrixUtils.write_P_table(pTableServer.get_table(5), fileName)
    self.assertTrue(matrixUtils.read_P_table(fileName) == pTableServer.get_table(5))

unittest.main()

