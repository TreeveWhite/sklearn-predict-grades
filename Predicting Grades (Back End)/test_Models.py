"""
Unit test for Models Class.
"""

from Models import Models
import unittest

class MyTest(unittest.TestCase):

	def test_makeModels(self):
		m1 = Models()
		self.assertEqual(len(m1.modelList), 6)



if __name__ == "__main__":
	unittest.main()
