import unittest
import sys
sys.path.append('../lib')
sys.path.append('helpers')
import vTable
import vTableServer

class vTest(unittest.TestCase):

  def test_when_n_is_0(self):
    self.assertTrue(vTableServer.get_table(0) == vTable.calculate(0))

  def test_when_n_is_2(self):
    self.assertTrue(vTableServer.get_table(1) == vTable.calculate(1))

  def test_when_n_is_3(self):
    self.assertTrue(vTableServer.get_table(2) == vTable.calculate(2))

  def test_when_n_is_5(self):
    self.assertTrue(vTableServer.get_table(5) == vTable.calculate(5))

unittest.main()

