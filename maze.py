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
            win: Window
    ):
        self.__win = win
        self.__cells: list[list[Cell]] = []
        self.__create_cells(margin,
                            num_rows,
                            num_cols,
                            cell_size_x,
                            cell_size_y)

    def __create_cells(self,
                       margin: Point,
                       num_rows: int,
                       num_cols: int,
                       cell_size_x: float,
                       cell_size_y: float,
                       ):
        for col in range(num_cols):
            curr_col: list[Cell] = []
            for row in range(num_rows):
                curr_col.append(Cell(self.__win))
            self.__cells.append(curr_col)

        for col in range(num_cols):
            for row in range(num_rows):
                self.__draw_cell(margin, col, row, cell_size_x, cell_size_y)

    def __draw_cell(self, margin: Point, col: int, row: int, cell_size_x: float, cell_size_y: float):
        self.__cells[col][row].draw(
            Point(
                margin.x + col * cell_size_x,
                margin.y + row * cell_size_y
            ),
            Point(
                margin.x + (col+1) * cell_size_x,
                margin.y + (row+1) * cell_size_y
            )
        )
        self.__animate()

    def __animate(self):
        self.__win.redraw()
        sleep(0.05)
