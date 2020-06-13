from graphics import *
import button
import drawboard
import displayboard


class Screens():

    def __init__(self, win):

        self.elements = []
        self.win = win
        self.display_screen_on = False
        self.draw_screen_on = False

        n = (20*28)
        f = n/3
        xsize = 125
        space = f - xsize

        #------------------------------------------------------------
        self.trainb = button.Button(self.win,Point(25,590),Point(25 + 150,620),"pink","pink", "Train")
        self.testb = button.Button(self.win, Point(25 + 150 + 55, 590), Point(25 + 150 + 55 + 150, 620),"pink","pink", "Test")
        self.drawb = button.Button(self.win, Point(25 +20*28 - 150,590), Point(25 +20*28, 620),"pink","pink", "Draw your own")

        self.quitb = button.Button(self.win, Point(25 +20*28-100,760), Point(25 +20*28, 790),"pink","pink", "Quit")

        self.checkb = button.Button(self.win, Point(25,590), Point(250, 620), "pink","pink", "Ask the Computer")
        self.eraseb = button.Button(self.win, Point(25 +20*28 - 225,590), Point(25 +20*28, 620), "pink","pink", "Erase")
        self.backb = button.Button(self.win, Point(25 +20*28 - 150+50,760), Point(25 +20*28, 790),"pink","pink", "Back")

        self.costlabel = Text(Point(308, 710),"Cost: ")
        self.costlabel.setTextColor("white")

        self.displayboard = displayboard.DisplayBoard(win, 25,25)
        self.drawboard = drawboard.DrawBoard(win, Point(25,25))

        self.trainlable = Text(Point(300,735), "THE MACHINE HAS NOT BEEN TRAINED YET")
        self.trainlable.setTextColor("red")
        self.trainlable.draw(self.win)
        self.namelabel = Text(Point(60, 790), "By: Rahul Gudise")
        self.namelabel.setTextColor("white")
        self.namelabel.draw(self.win)
        self.quit = False
        #------------------------------------------------------------

    def display_screen(self):
        if (self.draw_screen_on == True):
            self.undraw_draw_screen()

        self.trainb.draw()
        self.testb.draw()
        self.drawb.draw()
        self.quitb.draw()
        self.displayboard.draw()
        self.costlabel.draw(self.win)

        self.display_screen_on = True
        self.draw_screen_on = False


    def draw_screen(self):
        self.drawboard.draw()
        self.checkb.draw()
        self.backb.draw()
        self.eraseb.draw()

        if (self.display_screen_on == True):
            self.undraw_display_screen()
        self.display_screen_on = False
        self.draw_screen_on = True

    def undraw_display_screen(self):
        self.trainb.undraw()
        self.testb.undraw()
        self.drawb.undraw()
        self.quitb.undraw()
        self.displayboard.undraw()
        self.costlabel.undraw()


    def undraw_draw_screen(self):
        self.drawboard.undraw()
        self.checkb.undraw()
        self.backb.undraw()
        self.eraseb.undraw()

    def update_cost(self, cost):
        self.costlabel.setText(f"Cost: {cost}")