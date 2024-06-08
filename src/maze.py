from cell import Cell
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
    
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
        cell_x = self._x1 + self._cell_size_x * i
        cell_y = self._y1 + self._cell_size_y * j

        self._cells[i][j].draw(cell_x, cell_y, cell_x + self._cell_size_x,cell_y + self._cell_size_y)
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

