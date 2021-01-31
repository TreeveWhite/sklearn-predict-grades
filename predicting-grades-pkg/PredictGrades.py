"""
Program to predict final A-level Grade from AS Grade
"""
from DataSet import *
from Models import *
from Predictor import *
from Enums import *
from TextInterface import *


def main():
    dataLocation = "gradesComparison.cvs"
    numColumns = 2
    validationSize = 5
    seed = 7
    
    currentInterface = TextInterface()
    data = DataSet(dataLocation, numColumns, validationSize, seed)
    models = Models()
    
    inputedPredictions = currentInterface.getPredictionValue()

    newPredictionMeathod = Predictor(ModelType.KNeighborsClassifier, data)
    prediction = newPredictionMeathod.predict(inputedPredictions)


    currentInterface.showPrediction(Grade(prediction))

if __name__ == "__main__":
    main()