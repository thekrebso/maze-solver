from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width: int, height: int):
        self.__root = Tk()
        self.__root.title("Maze solver")
        self.canvas = Canvas()
        self.canvas.pack(in_=self.__root)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False
