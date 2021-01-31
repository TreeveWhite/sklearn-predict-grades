"""
Unit Test for the DataSet class.
"""

from DataSet import DataSet
import unittest

class MyTest(unittest.TestCase):
	def test_DataSet(self):

		data = DataSet("testData.cvs", 2, 4, 7)

		self.assertEqual(data.validationSize, 4)
		self.assertEqual(data.seed, 7)
		self.assertEqual(data.scoringBasis, "accuracy")


if __name__ == "__main__":
	unittest.main()