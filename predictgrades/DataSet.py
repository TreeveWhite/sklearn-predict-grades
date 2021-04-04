"""
DataSet.py
===============================================
This moule contains the DataSet class which is used in the predicting grades package.
"""
import pandas
from sklearn import model_selection

class DataSet:
    """
    This class is used to hold the infomation on the data set which is used to train the model
    used by the predicting grades package.
    """

    def __init__(self : object, dataLocation : str, numColumns : int, validationSize : int, seed : int, scoringBasis : str = "accuracy") -> None:
        """
        This method initialises a DataSet object.

        The objects attributes are set in acorrdance to the data in the file given by the 
        dataLocation path, which is handled in accordance to the other parameters to place the data
        in the correct format to be used by the package.

        :param dataLocation:    This is the path of the data base (.cvs) file.
        :type dataLocation:     string
        :param numColumns:      The number of columns in the data set.
        :type numColumns:       integer
        :param validationSize:  The validation size of the data set.
        :type validationSize:   integer
        :param seed:            The seed of the data set.
        :type seed:             integer
        :param scoringBasis:    The scoring basis of the data set. Defult value is accuracy.
        :type scoringBasis:     string

        :return :   None
        :rtype :    None

        """
        self.data = pandas.read_csv(dataLocation)
        self.array = self.data.values
        self.X = self.array[:, 0:numColumns]
        self.Y = self.array[:,numColumns]
        self.validationSize = validationSize
        self.seed = seed
        self.scoringBasis = scoringBasis
        self.X_train, self.X_validation, self.Y_train, self.Y_validation = model_selection.train_test_split(self.X, self.Y, test_size=self.validationSize, random_state=self.seed)
