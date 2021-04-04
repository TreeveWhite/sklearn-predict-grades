"""
Predictor.py
=====================================================
This module conatins th Predictor class which is used by the predicting grades module.
"""
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
import numpy

from predictgrades.ModelType import ModelType
from predictgrades.Grade import Grade
from PredictGrades.DataSet import DataSet

class Predictor:
    """
    This class is used to create predictions using the sklearn models. For the 
    purpose of the predicting grades package the only model which has been
    implimented is the KNeighborsClassifier model.
    """

    def __init__(self : object, typePredict : ModelType, dataset : DataSet) -> None:
        """
        This method initialises a Predictor object.

        The objects attributes are set in this method in accordance to the parameter provided 
        when creating a new instgance of the class. These attributes are then used to create
        predictions in the later methods of the object.

        :param self:            The Predictor object
        :type self:             Predictor (object)
        :param typePredict:     The model to use to create a prediction.
        :type typePredict:      ModelType
        :param dataset:         The dataset to train the model using.
        :type dataset:          Dataset (object)
        
        :return :   None
        :rtype :    None
        """
        self.prediction = None
        self.typePredict = typePredict
        self.dataset = dataset

    def predict(self : object, valueToPredictFrom : int) -> str:
        """
        This method creates a prediction.

        The method has limited functionality and will only compute a prediction if the typePrediction
        attribute of the current object is set as KNeighborsClassifier. The project uses the sklearn 
        library to create a prediction using this model.

        :param self:                The Predictor object
        :type self:                 Predictor (object)
        :param valueToPredictFrom:  The data to use to calculate a prediction for.
        :type valueToPredictFrom:   int

        :return prediction: The predicted grade the model has decided.
        :rtype prediction:  Grade (enum)
        """
        intGradePredict = eval("Grade."+valueToPredictFrom[0]+".value")
        attendance = valueToPredictFrom[1]        
        if self.typePredict == ModelType.KNeighborsClassifier:
            prediction = self.KNeighborsClassifier([[intGradePredict, attendance]])
            return prediction
        
    def KNeighborsClassifier(self : object, valueToPredictFrom : Grade) -> str:
        """
        This method creates a prediction using the KNeighboursCassifier model.

        The method trais the model using the dataset and then craeted a prediction of a pair of variables
        of the third variable (given the attendance and mock grade calculates a prediction of the final grade).

        :param self:                The Predictor object
        :type self:                 Predictor (object)
        :param valueToPredictFrom:  The data to use to calculate a prediction for.
        :type valueToPredictFrom:   int

        :return prediction: The predicted grade the model has decided.
        :rtype prediction:  Grade (enum)
        """
        knn = KNeighborsClassifier()
        knn.fit(self.dataset.X_train, self.dataset.Y_train)
        return (knn.predict(valueToPredictFrom))
