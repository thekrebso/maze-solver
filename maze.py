import random
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
            win: Optional[Window] = None,
            seed: Optional[int] = None
    ):
        self.__win = win
        self.__cells: list[list[Cell]] = []
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__margin = margin
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        if seed is not None:
            random.seed(seed)

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

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
        self.__animate(True)

    def __animate(self, fast: bool = False):
        if self.__win is None:
            return

        self.__win.redraw()

        if fast:
            sleep(0.015)
        else:
            sleep(0.05)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols -
                     1][self.__num_rows-1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols-1, self.__num_rows-1)

    def __break_walls_r(self, col: int, row: int):
        self.__cells[col][row].visited = True

        while True:
            possible_directions: list[tuple[int, int]] = []
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for direction in directions:
                next_col = col + direction[0]
                next_row = row + direction[1]
                if (
                    next_col >= 0 and next_col < self.__num_cols and
                    next_row >= 0 and next_row < self.__num_rows and
                    not self.__cells[next_col][next_row].visited
                ):
                    possible_directions.append((next_col, next_row))

            if len(possible_directions) == 0:
                self.__draw_cell(col, row)
                return

            direction = random.randint(0, len(possible_directions) - 1)
            next_col = possible_directions[direction][0]
            next_row = possible_directions[direction][1]

            dc = next_col - col
            dr = next_row - row

            if dr == -1:
                self.__cells[col][row].has_top_wall = False
                self.__cells[next_col][next_row].has_bottom_wall = False
            if dr == 1:
                self.__cells[col][row].has_bottom_wall = False
                self.__cells[next_col][next_row].has_top_wall = False
            if dc == 1:
                self.__cells[col][row].has_right_wall = False
                self.__cells[next_col][next_row].has_left_wall = False
            if dc == -1:
                self.__cells[col][row].has_left_wall = False
                self.__cells[next_col][next_row].has_right_wall = False

            self.__draw_cell(col, row)
            self.__draw_cell(next_col, next_row)

            self.__break_walls_r(next_col, next_row)

    def __reset_cells_visited(self):
        for col in self.__cells:
            for row in col:
                row.visited = False

    def solve(self):
        return self.__solve_r(0, 0)

    def __solve_r(self, col: int, row: int):
        self.__animate()
        self.__cells[col][row].visited = True

        if col == self.__num_cols - 1 and row == self.__num_rows - 1:
            return True

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for direction in directions:
            next_col = col + direction[0]
            next_row = row + direction[1]
            dc = next_col - col
            dr = next_row - row
            if (
                next_col >= 0 and next_col < self.__num_cols and
                next_row >= 0 and next_row < self.__num_rows and
                not self.__cells[next_col][next_row].visited and
                (
                    dr == -1 and not self.__cells[col][row].has_top_wall or
                    dr == 1 and not self.__cells[col][row].has_bottom_wall or
                    dc == 1 and not self.__cells[col][row].has_right_wall or
                    dc == -1 and not self.__cells[col][row].has_left_wall
                )
            ):
                self.__cells[col][row].draw_move(
                    self.__cells[next_col][next_row])

                if self.__solve_r(next_col, next_row):
                    return True

                self.__cells[col][row].draw_move(
                    self.__cells[next_col][next_row], True)

        return False
