from typing import Optional
from time import sleep
from point import Point
from cell import Cell
from window import Window


class Maze:
    def __init__(
            self,
            margin: Point,
            num_rows: int,
            num_cols: int,
            cell_size_x: float,
            cell_size_y: float,
            win: Optional[Window] = None
    ):
        self.__win = win
        self.__cells: list[list[Cell]] = []
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__margin = margin
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y

        self.__create_cells()
        self.__break_entrance_and_exit()

    def __create_cells(self):
        for col in range(self.__num_cols):
            curr_col: list[Cell] = []
            for row in range(self.__num_rows):
                curr_col.append(Cell(self.__win))
            self.__cells.append(curr_col)

        for col in range(self.__num_cols):
            for row in range(self.__num_rows):
                self.__draw_cell(col, row)

    def __draw_cell(self, col: int, row: int):
        self.__cells[col][row].draw(
            Point(
                self.__margin.x + col * self.__cell_size_x,
                self.__margin.y + row * self.__cell_size_y
            ),
            Point(
                self.__margin.x + (col+1) * self.__cell_size_x,
                self.__margin.y + (row+1) * self.__cell_size_y
            )
        )
        self.__animate()

    def __animate(self):
        if self.__win is None:
            return

        self.__win.redraw()
        sleep(0.05)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols -
                     1][self.__num_rows-1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols-1, self.__num_rows-1)
