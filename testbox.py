from graphics import *

class TestBox():

    def __init__(self, win):
        self.win = win
        self.comp_guess = Text(Point(292.5, 650), "Computer: ")
        self.comp_guess.setTextColor("white")
        self.actual = Text(Point(283, 670), "Actual: ")
        self.actual.setTextColor("white")
        self.accuracy = Text(Point(308, 690), "Accuracy: ")
        self.accuracy.setTextColor("white")
        self.activation = False

    def draw(self):
        self.comp_guess.draw(self.win)
        self.actual.draw(self.win)
        self.accuracy.draw(self.win)
        self.activation = True

    def undraw(self):
        self.comp_guess.undraw()
        self.actual.undraw()
        self.accuracy.draw()
        self.activation == False

    def update(self,activation, actual, accuracy):
        guess = 0
        if (activation > .5):
            guess = 1
        self.comp_guess.setText(f"Computer: {guess}")
        self.actual.setText(f"Actual : {actual}")
        self.accuracy.setText(f"Accuracy: {accuracy}%")


