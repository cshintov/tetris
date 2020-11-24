""" 
Represents a four-in-a-row board.

Uses a grid (2 X 2 matrix) to represent the board.
"""

from numpy import zeros


class Board(object):
    def __init__(self, rows, colns):
        """ Creates a rows X colns grid """
        self.b = zeros((rows, colns))
        self.size = rows, colns

    @property
    def size(self):
        return self.size

    def __str__(self):
        return str(self.b)

    def place(self, cell):
        x, y = cell.pos
        self.b[x][y] = cell.val


class Cell(object):
    def __init__(self, x, y, val=1):
        self.pos = x, y
        self.val = val


def size(board):
    """ Calculate the size (rows, cols) of the board """
    try:
        return (len(board), len(board[0]))
    except:
        return (0, 0)


def place(piece, board):
    """
    Place piece on the board
    """
    x, y = piece.pos
    shape = piece.get_shape()
    print(x, y)
    print(shape)
    r, c = size(shape)

    for i in range(r):
        for j in range(c):
            board[i + x][j + y] = shape[i][j]


def up(b, x, y):
    """ Returns the coordinates of the above cell in the grid """
    x1, y1 = x - 1, y
    if x1 < 0:
        return None
    return (x1, y1)


def down(b, x, y):
    """ Returns the coordinates of the below cell in the grid """
    r, c = size(b)
    x1, y1 = x + 1, y
    if not x1 < r:
        return None
    return (x1, y1)


def left(b, x, y):
    """ Returns the coordinates of the left cell in the grid """
    x1, y1 = x, y - 1
    if y1 < 0:
        return None
    return (x1, y1)


def right(b, x, y):
    """ Returns the coordinates of the right cell in the grid """
    r, c = size(b)
    x1, y1 = x, y + 1
    if not y1 < c:
        return None
    return (x1, y1)


def diagonals(d1, d2):
    """A higher order function that accepts two directions d1 and d2
    and returns the coordinates of the cell reached after moving
    first d1 and then d2"""

    def inner(b, x, y):
        coord = d1(b, x, y)
        return None if not coord else d2(b, *coord)

    return inner


# The below functions created using 'diagonals' can be used
# to get the coordinates of the adjacent cells of a cell when
# moved diagonally

left_up = diagonals(left, up)
left_down = diagonals(left, down)
right_up = diagonals(right, up)
right_down = diagonals(right, down)


if __name__ == "__main__":
    from tetriminoes import *

    ROW, COL = 20, 10

    b1 = create_board(ROW, COL)
    place(O, b1)

    print(b1)
