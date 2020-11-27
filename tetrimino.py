""" The module handles representing a tetrimino 

There seven I, J, L, S, Z, T, O.

These are meant to be placed on a board. Moved left, right, down and rotated on the board.

The edge cases are literally at the edge of the board. How do you handle moving right at the right edge, how do you rotate, etc.

When you think of placing an O at (0, 0) on the board, let's think of a function like

place(t, board, pos)

t should have the grid representation of the tetrimino and possibly other attributes like
color, pos, type.
"""
import numpy as np


def create_board(rows, colns):
    return np.zeros((rows, colns))


def get_ones(shape):
    """ Get the cells with 1s """
    r, c = shape.shape
    return [(i, j) for i in range(r) for j in range(c) if shape[i][j] == 1]


""" Need to create a cycle 
A cycle is nothing but a sequence that can be traversed cyclically in both direction.
It will have to methods: next and previous

"""
from collections import deque


def rotate_left(deq):
    return deq.rotate(-1)


def rotate_right(deq):
    return deq.rotate()


def rotate(grid):
    return np.rot90(grid)


def ntimes(func, initial, n):
    results = [initial]

    def inner(val, n):
        if n <= 0:
            return results
        result = func(val)
        results.append(result)
        return inner(result, n - 1)

    return inner(initial, n - 1)


def create_tetrimino(typ, shape, color):
    return {
        "type": typ,
        "size": shape.shape,
        "color": color,
        "shapes": deque([get_ones(sh) for sh in ntimes(rotate, shape, 4)]),
    }


O = create_tetrimino("O", np.array(([1, 1, 0], [1, 1, 0], [0, 0, 0])), "yellow")


def ignore_error(Error):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as err:
                print(err)

        return inner

    return decorator


@ignore_error(IndexError)
def is_valid(t, board, pos):
    ones = t["shapes"][0]
    x, y = pos
    for i, j in ones:
        board[i + x][j + y]

    return True


def place(t, board, pos):
    if not is_valid(t, board, pos):
        return

    ones = t["shapes"][0]
    x, y = pos
    for i, j in ones:
        board[i + x][j + y] = 1
