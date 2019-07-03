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
class Grade(enum.Enum):
    a = 6
    b = 5
    c = 4
    d = 3
    e = 2
    f = 1
