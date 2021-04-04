"""
Modeltype.py
=====================================================
This module contains the ModelType enum which is used by the predicting grades package.
"""
import enum

class ModelType(enum.Enum):
    """
    This is the enumerator for the different Models.
    """

    KNeighborsClassifier = 1
    LogisticRegression = 2
    LinearDiscriminantAnalysis = 3
    DecisionTreeClassifier = 4
    GaussianNB = 5
    SVC = 6
