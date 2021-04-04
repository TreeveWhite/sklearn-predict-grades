"""
Models.py
=======================================================
This mdule contains the models class which is used by the predicting grades package.
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
    """
    This class is used to handle all the possible models.

    These models are taken from the sklearn library and all could be used to analyse the data and
    create prodictions.
    """

    def __init__(self : object) -> None:
        """
        This method initialises a Models object.

        The objects attributes are all set to be empty to allow the makeModels method to later add
        mdels to the modelList array and their respective accuracy to the modelAccuracy array.
        
        :param self:    The current Models Object
        :type self:     Models (object)

        :return :   None
        :rtype :    None
        """
        self.modelList = []
        self.modelAccuracy = []
        
        self.makeModels()
        
    def makeModels(self):
        """
        This method makes and appends all the models to the modelsList array.

        :param self:    The current Models Object
        :type self:     Models (object)

        :return :   None
        :rtype :    None
        """
        self.modelList.append((ModelType.LogisticRegression, LogisticRegression(solver='liblinear', multi_class='ovr')))
        self.modelList.append((ModelType.LinearDiscriminantAnalysis, LinearDiscriminantAnalysis()))
        self.modelList.append((ModelType.KNeighborsClassifier, KNeighborsClassifier()))
        self.modelList.append((ModelType.DecisionTreeClassifier, DecisionTreeClassifier()))
        self.modelList.append((ModelType.GaussianNB, GaussianNB()))
        self.modelList.append((ModelType.SVC, SVC(gamma='auto')))

    def analyseModels(self, dataset):
        """
        This metod loop over the models and compares thir accuracy in regard to the given data set to calculae their overall
        accuracy percentage out of 100. 

        This infomation can then later be used to determine whih model is the best to use for a specific data set.

        :param self:    The current Models Object
        :type self:     Models (object)
        :param dataset: The dataset which the model accuracy shoud be analysed in relation to.
        :type dataset:  DataSet (object)

        :return :   None
        :rtype :    None
        """
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
        
    
