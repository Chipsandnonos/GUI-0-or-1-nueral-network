import button
from graphics import *

class DrawBoard():
    size = 28
    scale = 20

    def __init__(self,  win, point):
        self.board_buttons =[]
        self.x = point.getX()
        self.y = point.getY()
        self.win = win

        for z in range(DrawBoard.size):
            board_row = []
            for i in range(DrawBoard.size):

                p1 = Point(self.x + i * DrawBoard.scale, self.y + z * DrawBoard.scale)
                p2 = Point(self.x + + (i+1) * DrawBoard.scale, self.y +  + (z+1)*DrawBoard.scale)
                b = button.Button(win, p1,p2 ,"white","black", "")
                board_row.append(b)

            self.board_buttons.append(board_row)



    def is_click(self,point):
        xpoint = point.getX()
        ypoint = point.getY()

        if (xpoint >= self.x  and xpoint <= self.x + DrawBoard.size * DrawBoard.scale) and (ypoint >= self.y and ypoint <= DrawBoard.size * DrawBoard.scale):
            return True
        else:
            return False

    def click(self, point):
        for i in range(DrawBoard.size):
            for y in range(DrawBoard.size):
                self.board_buttons[i][y].is_pressed(point)


    def transfer(self):
        num_board = []

        for i in range(DrawBoard.size):
            for y in range(DrawBoard.size):
                press = self.board_buttons[i][y].activate
                if (press == True):
                    num_board.append(255)
                else:
                    num_board.append(0)
        return num_board

    def undraw(self):
        for z in range(DrawBoard.size):
            for i in range(DrawBoard.size):
                b = self.board_buttons[z][i]
                b.undraw()


    def draw(self):
        for x in range(DrawBoard.size):
            for y in range(DrawBoard.size):
                self.board_buttons[x][y].draw()

    def clear(self):
        for x in range(DrawBoard.size):
            for y in range(DrawBoard.size):
                self.board_buttons[y][x].recolor()
