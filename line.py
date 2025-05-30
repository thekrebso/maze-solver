from tkinter import Canvas 
from point import Point


class Line:
    def __init__(self, begin: Point, end: Point):
        self.begin = begin
        self.end = end

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.begin.x, self.begin.y, self.end.x, self.end.y,
            fill=fill_color, width=2
        )
