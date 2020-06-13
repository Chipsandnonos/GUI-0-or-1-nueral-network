from graphics import *

class DisplayBoard():
    scale = 20
    thic = .5
    pic_size = 28

    def __init__(self, win, xs, ys):
        self.col_pixel = []
        self.win = win
        self.backr = Rectangle(Point(xs-1,ys-1), Point(DisplayBoard.pic_size * DisplayBoard.scale + 1 + xs, DisplayBoard.pic_size * DisplayBoard.scale + 1 + ys))
        self.backr.setOutline("white")
        self.backr.draw(win)

        for y in range(DisplayBoard.pic_size):
            row = []
            for x in range(DisplayBoard.pic_size):
                r = Rectangle(Point(x * DisplayBoard.scale + xs, y * DisplayBoard.scale + ys), Point((x + 1) * DisplayBoard.scale + xs, (y + 1) * DisplayBoard.scale + ys))
                row.append(r)

            self.col_pixel.append(row)


    def colour_board(self, images, index):
        col_value = images[index]
        pic_size = DisplayBoard.pic_size

        for y in range(pic_size):
            for x in range(pic_size):
                pix_col = color_rgb(col_value[y * pic_size + x], col_value[y * pic_size + x],
                                    col_value[y * pic_size + x])
                r = self.col_pixel[y][x]
                r.setFill(pix_col)

    def undraw(self):
        for y in range(DisplayBoard.pic_size):
            for x in range(DisplayBoard.pic_size):
                self.col_pixel[x][y].undraw()

    def draw(self):
        for x in range(DisplayBoard.pic_size):
            for y in range(DisplayBoard.pic_size):
                self.col_pixel[x][y].draw(self.win)
