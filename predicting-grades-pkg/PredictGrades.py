"""
PredictGrade.py
================================================
This module contains the runner code for the predict grade package.
"""
from DataSet import DataSet
from Models import Models
from Predictor import Predictor
from ModelType import ModelType
from Grade import Grade
from TextInterface import TextInterface

DATA_PATH = "gradesComparison.cvs"
NUM_COLUMNS = 2
VALIDATION_SIZE = 5
SEED = 7

def main(dataLocation : str, numColumns : int, validationSize : int, seed : int) -> None:
    """
    This method is the runner for the predict gardes package.

    The method initialises all the other neccessary objects and then created a peciction based
    upon the model selected and the inputted data from the user.

    :param dataLocation:    The path of the database (.csv) file which holds the existing data to be used
                            by the sklearn model.
    :type dataLocation:     string
    :param numColumns:      The number of columns in the dataset.
    :type numCulumns:       integer
    :param validationSize:  The validation size of the data set.
    :type validationSize:   integer
    :param seed:            The seed of the data set.
    :type seed:             integer

    :return :   None
    :rtype :    None
    """
    # Initialise the objects
    currentInterface = TextInterface()
    data = DataSet(dataLocation, numColumns, validationSize, seed)
    models = Models()
    
    # Get the user's data for the predicted grade
    inputedPredictions = currentInterface.getPredictionValue()

    # Calculate the prediction
    newPredictionMeathod = Predictor(ModelType.KNeighborsClassifier, data)
    prediction = newPredictionMeathod.predict(inputedPredictions)

    # Display the prediction
    currentInterface.showPrediction(Grade(prediction))

if __name__ == "__main__":
    main(DATA_PATH,
        NUM_COLUMNS,
        VALIDATION_SIZE,
        SEED)