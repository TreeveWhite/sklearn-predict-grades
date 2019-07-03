"""
A class for comtrolling all models
"""

from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
from Enums import ModelType


class Models:
    def __init__(self):
        self.modelList = []
        self.modelAccuracy = []
        
        self.makeModels()
        
    def makeModels(self):
        self.modelList.append((ModelType.LogisticRegression, LogisticRegression(solver='liblinear', multi_class='ovr')))
        self.modelList.append((ModelType.LinearDiscriminantAnalysis, LinearDiscriminantAnalysis()))
        self.modelList.append((ModelType.KNeighborsClassifier, KNeighborsClassifier()))
        self.modelList.append((ModelType.DecisionTreeClassifier, DecisionTreeClassifier()))
        self.modelList.append((ModelType.GaussianNB, GaussianNB()))
        self.modelList.append((ModelType.SVC, SVC(gamma='auto')))

    def analyseModels(self, dataset):
        results = []
        names = []
        self.accuracyScores = []
        for name, model in self.modelList:
            kfold = model_selection.KFold(n_splits=10, random_state=dataset.seed)
            cv_results = model_selection.cross_val_score(model, dataset.X_train, dataset.Y_train, cv=kfold, scoring=dataset.scoringBasis)
            results.append(cv_results)
            names.append(name)
            modelScore = [name, cv_results.mean()]
            self.accuracyScores.append(modelScore)
        
    
