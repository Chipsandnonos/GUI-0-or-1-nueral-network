from graphics import *

class Button():


    def __init__(self,window, Point1, Point2, color, clickcolour, label):
        self.win = window
        self.r = Rectangle(Point1,Point2)
        self.r.setFill(color)
        self.clickcolour = clickcolour
        self.color = color
        self.x1 = Point1.getX()
        self.y1 = Point1.getY()

        self.x2 = Point2.getX()
        self.y2 = Point2.getY()

        self.label = Text(self.r.getCenter(), label)

        self.activate = False

    def is_pressed(self, Point):
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        y2 = self.y2


        x_click = Point.getX()
        y_click = Point.getY()

        if (x_click >= x1 and x_click <= x2) and (y_click >= y1 and y_click <= y2) :
            self.r.setFill(self.clickcolour)
            self.activate = True
            return True

        else:
            return False

    def undraw(self):
        self.r.undraw()
        self.label.undraw()

    def draw(self):
        self.r.draw(self.win)
        self.label.draw(self.win)

    def recolor(self):
        self.r.setFill("white")