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

    _init_ = 'value __doc__'

    KNeighborsClassifier = 1, "The K-Neighbors Classifier model"
    LogisticRegression = 2, "The Logistic Regression model"
    LinearDiscriminantAnalysis = 3, "The Linear Discriminant Analysis model"
    DecisionTreeClassifier = 4, "The Decision Tree Classifier model"
    GaussianNB = 5, "The GaussianNB model"
    SVC = 6, "The SVC model"
