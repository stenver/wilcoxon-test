import unittest
import sys
sys.path.append('../lib')
import vTableServer
import pTableServer
import pTable

class vTest(unittest.TestCase):

  def test_when_n_is_0(self):
    self.assertTrue(pTableServer.get_table(0) == pTable.calculate(vTableServer.get_table(0)))

  def test_when_n_is_2(self):
    self.assertTrue(pTableServer.get_table(1) == pTable.calculate(vTableServer.get_table(1)))

  def test_when_n_is_3(self):
    self.assertTrue(pTableServer.get_table(2) == pTable.calculate(vTableServer.get_table(2)))

  def test_when_n_is_5(self):
    self.assertTrue(pTableServer.get_table(5) == pTable.calculate(vTableServer.get_table(5)))

unittest.main()

