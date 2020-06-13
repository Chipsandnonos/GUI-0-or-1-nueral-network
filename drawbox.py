from graphics import *

class DrawBox():

    def __init__(self, win):
        self.win = win
        self.comp_guess = Text(Point(292.5, 650), "Computer: ")
        self.comp_guess.setTextColor("white")
        self.activationt = Text(Point(295, 670), "Activation: ")
        self.activationt.setTextColor("white")
        self.activation = False

    def draw(self):
        self.comp_guess.draw(self.win)
        self.activationt.draw(self.win)
        self.activation = True

    def undraw(self):
        self.comp_guess.undraw()
        self.activationt.undraw()
        self.activation == False

    def update(self,activation):
        guess = 0
        if (activation > .5):
            guess = 1
        self.comp_guess.setText(f"Computer: {guess}")
        self.activationt.setText(f"Activation: {activation}")



