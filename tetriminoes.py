""" Module defines tetriminoes and their operations 

The available tetriminoes are I, L, J, S, Z, O, T.

I and O has its bounding box size 4. Rest only has 3.

T = array([[0, 1, 0],
           [1, 1, 1],
           [0, 0, 0]])

Shape = {
    'grid': [],
    'next': S1,
    'prev': S3
}
"""

import numpy as np
from collections import deque

from board import size

sizes = {
    **dict.fromkeys(["I", "O"], 4),
    **dict.fromkeys(["L", "J", "S", "Z", "T"], 3),
}


def doseq(f, seq):
    for item in seq:
        f(item)


class Cycle(object):
    def __init__(self, iterable):
        self._iter = deque(iterable)

    def __repr__(self):
        return repr(self._iter).replace("deque", "Cycle")

    def next(self):
        self._iter.rotate(1)
        return self._iter[0]

    def previous(self):
        self._iter.rotate(-1)
        return self._iter[0]

    def __getitem__(self, y):
        return self._iter[y]


def repeat(f, init, n):
    out = [init]
    for i in range(n - 1):
        init = f(init)
        out.append(init)
    return out


class Tetrimino(object):
    def __init__(self, name, init, pos=(0, 4), rotations=4):
        self.name = name
        self.shapes = Cycle(repeat(np.rot90, init, rotations))
        self.color = ""
        self.pos = pos

    def __repr__(self):
        return f"Tetrimino<{self.name}>\n{self.shapes[0]}"

    def get_shape(self):
        return self.shapes[0]

    def next(self):
        return self.shapes.next()

    def previous(self):
        return self.shapes.previous()

    def size(self):
        r = len(self.get_shape())
        return (r, r)


# Create Tetriminoes
O = Tetrimino("O", np.array([[1, 1, 0], [1, 1, 0], [0, 0, 0]]), rotations=1)
T = Tetrimino("T", np.array([[0, 1, 0], [1, 1, 1], [0, 0, 0]]))
L = Tetrimino("L", np.array([[1, 0, 0], [1, 0, 0], [1, 1, 0]]))
J = Tetrimino("J", np.array([[0, 1, 0], [0, 1, 0], [1, 1, 0]]))
S = Tetrimino("S", np.array([[0, 1, 1], [1, 1, 0], [0, 0, 0]]))
Z = Tetrimino("Z", np.array([[1, 1, 0], [0, 1, 1], [0, 0, 0]]))
I = Tetrimino("I", np.array([[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]))

TETRIMINOES = {"O": O, "T": T, "L": L, "J": J, "S": S, "Z": Z, "I": I}


def get_ones(grid):
    r, c = size(grid)
    return [(i, j) for i in range(r) for j in range(c) if grid[i][j] == 1]


print(get_ones(O.get_shape()))


def show(piece):
    for i in range(4):
        print(piece.get_shape())
        piece.shapes.next()


if __name__ == "__main__":
    # main()
    # doseq(print, [O, L])
    # show(O)
    pass
