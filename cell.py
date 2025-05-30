from point import Point
from line import Line
from window import Window 


class Cell:
    def __init__(self, window: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__win = window
        self.__begin = Point(-1, -1)
        self.__end = Point(-1, -1)

    def draw(self, begin: Point, end: Point):
        self.__begin = begin
        self.__end = end

        if self.has_left_wall: 
            self.__win.draw_line(
                Line(self.__begin, Point(self.__begin.x, self.__end.y)), 
                "black"
            )
        if self.has_right_wall: 
            self.__win.draw_line(
                Line(Point(self.__end.x, self.__begin.y), self.__end), 
                "black"
            )
        if self.has_top_wall: 
            self.__win.draw_line(
                Line(self.__begin, Point(self.__end.x, self.__begin.y)), 
                "black"
            )
        if self.has_bottom_wall: 
            self.__win.draw_line(
                Line(Point(self.__begin.x, self.__end.y), self.__end), 
                "black"
            )
