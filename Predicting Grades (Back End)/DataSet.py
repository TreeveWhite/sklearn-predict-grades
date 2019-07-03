"""
Class to control the dataset ebing used,
"""
import pandas
from sklearn import model_selection


class DataSet:

    def __init__(self, dataLocation, numColumns, validationSize, seed, scoringBasis = "accuracy"):
        self.data = pandas.read_csv(dataLocation)
        self.array = self.data.values
        self.X = self.array[:, 0:numColumns]
        self.Y = self.array[:,numColumns]
        self.validationSize = validationSize
        self.seed = seed
        self.scoringBasis = scoringBasis
        self.X_train, self.X_validation, self.Y_train, self.Y_validation = model_selection.train_test_split(self.X, self.Y, test_size=self.validationSize, random_state=self.seed)
