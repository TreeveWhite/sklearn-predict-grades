"""
TextInterface.py
================================================
This module contains the TextInterface class which is used by the predicting grades package.
"""

class TextInterface:
    """
    This class contains all the text interface methods.

    The object controls all interctions with the user via a text based terminal. This form of interface
    with teh user could be swapped or interchanged with another GUI or similar so long as the same methods
    are carried out and can be called by the main program of the package.
    """

    def getPredictionValue(self : object) -> list:
        """
        This method is used to get th users input data for the students mock grade and attendance.

        :param self:    The Text Interfance object
        :type self:     TextInterface (object)

        :return :   The students mock grade and attendance in a array.
        :rtype :    list
        """
        predictGrade = input("What is the Student's Mock grade?")
        attendance = input("What is the attendance?")
        return [predictGrade, attendance]

    def showPrediction(self, prediction):
        """
        This method displays the calculated prediction for the grade.

        :param self:        The Text Interfance object
        :type self:         TextInterface (object)
        :param prediction:  The predicted grade.
        :type prediction:   string

        :return :   None
        :rtype :    None
        """
        print("The prediction is {}".format(prediction))