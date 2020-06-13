from graphics import *

class TrainBox():

    def __init__(self, win):
        self.win = win
        self.comp_guess = Text(Point(292.5, 650), "Computer: ")
        self.comp_guess.setTextColor("white")
        self.activationt1 = Text(Point(292.5, 670), "Activation: ")
        self.activationt2 = Text(Point(292.5 + 80, 670), "")
        self.activationt1.setTextColor("white")
        self.activationt2.setTextColor("white")
        self.actual = Text(Point(308, 690), "Actual number: ")
        self.actual.setTextColor("white")
        self.activation = True
        self.moved = False


    def draw(self):
        self.comp_guess.draw(self.win)
        self.activationt1.draw(self.win)
        self.activationt2.draw(self.win)
        self.actual.draw(self.win)
        self.activation = True

    def undraw(self):
        self.comp_guess.undraw()
        self.activationt1.undraw()
        self.activationt2.undraw()
        self.actual.undraw()
        self.activation == False

    def update(self,activation, actual):
        guess = 0
        if (activation > .5):
            guess = 1
        self.comp_guess.setText(f"Computer: {guess}")
        self.activationt2.setText(f"{activation}")
        self.actual.setText(f"Actual number: {actual}")

        if (self.moved == False):
            self.activationt1.move(-5,0)
            self.moved = True



