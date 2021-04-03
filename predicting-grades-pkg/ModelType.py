"""
File for the different types of models
"""
import enum

class ModelType(enum.Enum):
    KNeighborsClassifier = 1
    LogisticRegression = 2
    LinearDiscriminantAnalysis = 3
    DecisionTreeClassifier = 4
    GaussianNB = 5
    SVC = 6
