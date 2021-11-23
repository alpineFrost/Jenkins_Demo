import unittest
from main import multiply

class test_multiply(unittest.TestCase):
  def test_mul1(self):
    self.assertEqual(multiply(12, 10), 120)  

  def test_mul2(self):
    self.assertEqual(multiply(4, 5), 20)  

if __name__ == '__main__':
  unittest.main()
