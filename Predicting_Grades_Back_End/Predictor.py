"""
A class for making all predictions
"""
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
from Enums import *
import numpy

class Predictor:
    def __init__(self, typePredict, dataset):
        self.prediction = None
        self.typePredict = typePredict
        self.dataset = dataset

    def predict(self, valueToPredictFrom):
        intGradePredict = eval("Grade."+valueToPredictFrom[0]+".value")
        attendance = valueToPredictFrom[1]        
        if self.typePredict == ModelType.KNeighborsClassifier:
            return self.KNeighborsClassifier([[intGradePredict, attendance]])
        
    def KNeighborsClassifier(self, valueToPredictFrom):
        knn = KNeighborsClassifier()
        knn.fit(self.dataset.X_train, self.dataset.Y_train)
        return (knn.predict(valueToPredictFrom))
