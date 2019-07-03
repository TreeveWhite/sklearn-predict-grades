"""
A class to control all text interface actions.
"""

class TextInterface:
    def getPredictionValue(self):
        predictGrade = input("What is the Student's Mock grade?")
        attendance = input("What is the attendance?")
        return [predictGrade, attendance]
    def showPrediction(self, prediction):
        print("The prediction is {}".format(prediction))