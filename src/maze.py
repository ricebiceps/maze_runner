from cell import Cell
import time
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            self._seed = random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
    
    def _create_cells(self):
        for col in range(self._num_cols):
            col_cells = []
            for row in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(col,row)
    
    def _draw_cell(self,i,j):
        if self._win is None:
            return

        cell_x = self._x1 + self._cell_size_x * i
        cell_y = self._y1 + self._cell_size_y * j

        self._cells[i][j].draw(cell_x, cell_y, cell_x + self._cell_size_x,cell_y + self._cell_size_y)
        self._animate()
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)

        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

