"""
Unit Test for Enums Class
"""

import unittest
from Enums import ModelType
from Enums import Grade

class MyTest(unittest.TestCase):
    def test_Models(self):
        
        self.assertEqual(ModelType.KNeighborsClassifier.value, 1)
        self.assertEqual(ModelType.LogisticRegression.value, 2)
        self.assertEqual(ModelType.LinearDiscriminantAnalysis.value, 3)
        self.assertEqual(ModelType.DecisionTreeClassifier.value, 4)
        self.assertEqual(ModelType.GaussianNB.value, 5)
        self.assertEqual(ModelType.SVC.value, 6)

    def test_Grade(self):

        self.assertEqual(Grade.a.value, 6)
        self.assertEqual(Grade.b.value, 5)
        self.assertEqual(Grade.c.value, 4)
        self.assertEqual(Grade.d.value, 3)
        self.assertEqual(Grade.e.value, 2)
        self.assertEqual(Grade.f.value, 1)
        
        
if __name__ == "__main__":
    unittest.main()
