from typing import Optional
from point import Point
from line import Line
from window import Window


class Cell:
    def __init__(self, window: Optional[Window] = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self.__win = window
        self.__begin = Point(-1, -1)
        self.__end = Point(-1, -1)

    def draw(self, begin: Point, end: Point):
        self.__begin = begin
        self.__end = end

        if self.__win is None:
            return

        self.__win.draw_line(
            Line(self.__begin, Point(self.__begin.x, self.__end.y)),
            "black" if self.has_left_wall else "white"
        )

        self.__win.draw_line(
            Line(Point(self.__end.x, self.__begin.y), self.__end),
            "black" if self.has_right_wall else "white"
        )

        self.__win.draw_line(
            Line(self.__begin, Point(self.__end.x, self.__begin.y)),
            "black" if self.has_top_wall else "white"
        )

        self.__win.draw_line(
            Line(Point(self.__begin.x, self.__end.y), self.__end),
            "black" if self.has_bottom_wall else "white"
        )

    def draw_move(self, to_cell: 'Cell', undo: bool = False):
        if self.__win is None:
            return

        from_center = Point(
            (self.__begin.x + self.__end.x) / 2,
            (self.__begin.y + self.__end.y) / 2
        )

        to_center = Point(
            (to_cell.__begin.x + to_cell.__end.x) / 2,
            (to_cell.__begin.y + to_cell.__end.y) / 2
        )

        fill_color = "gray" if undo else "red"

        self.__win.draw_line(
            Line(from_center, to_center),
            fill_color
        )
