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
    return deq.rotate()


def rotate_right(deq):
    return deq.rotate(-1)


def rotate(grid):
    return np.rot90(grid, k=-1)


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
        "pos": (0, 4),
        "type": typ,
        "size": shape.shape,
        "color": color,
        "shapes": deque([get_ones(sh) for sh in ntimes(rotate, shape, 4)]),
    }


# Create Tetriminoes
O = create_tetrimino("O", np.array(([1, 1, 0], [1, 1, 0], [0, 0, 0])), (255, 255, 0))
T = create_tetrimino("T", np.array([[0, 1, 0], [1, 1, 1], [0, 0, 0]]), (128, 0, 128))
L = create_tetrimino("L", np.array([[1, 0, 0], [1, 0, 0], [1, 1, 0]]), (255, 165, 0))
J = create_tetrimino("J", np.array([[0, 1, 0], [0, 1, 0], [1, 1, 0]]), (0, 0, 255))
S = create_tetrimino("S", np.array([[0, 1, 1], [1, 1, 0], [0, 0, 0]]), (0, 255, 0))
Z = create_tetrimino("Z", np.array([[1, 1, 0], [0, 1, 1], [0, 0, 0]]), (255, 0, 0))
I = create_tetrimino(
    "I",
    np.array([[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]),
    (0, 255, 255),
)

TETRIMINOES = {"O": O, "T": T, "L": L, "J": J, "S": S, "Z": Z, "I": I}


def view(shape, size):
    v = np.zeros(size)
    for i, j in shape:
        v[i][j] = 1

    print(v)


def inspect(t):
    for shape in t["shapes"]:
        view(shape, t["size"])


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
    assert x * y >= 0
    for i, j in ones:
        board[i + x][j + y]

    return True


def place(t, board, symbol=1):
    pos = t["pos"]
    if not is_valid(t, board, pos):
        return False

    ones = t["shapes"][0]
    x, y = pos
    for i, j in ones:
        board[i + x][j + y] = symbol

    return True


def clear(t, board):
    place(t, board, 0)


"""
Creating tetriminos and placing it on the board on a coordinate is done.
Next is moving left, right, down and rotate.
"""


def left(pos):
    x, y = pos
    return (x, y - 1)


def right(pos):
    x, y = pos
    return (x, y + 1)


def down(pos):
    x, y = pos
    return (x + 1, y)


def move(dirn):
    def helper(t, board):
        """ Move t left on the board. """
        clear(t, board)

        cur_pos = t["pos"]
        t["pos"] = dirn(cur_pos)

        success = place(t, board)
        if not success:
            t["pos"] = cur_pos
            place(t, board)

        return success

    return helper


# Move tetriminos left, right or down
move_left = move(left)
move_right = move(right)
move_down = move(down)


def next_tetrimino(t):
    return t["shapes"][0]


def rotate_tetrimino(dirn="clockwise"):
    if dirn == "clockwise":
        forward, backward = rotate_right, rotate_left
    else:
        forward, backward = rotate_left, rotate_right

    def helper(t, board):
        clear(t, board)
        forward(t["shapes"])
        success = place(t, board)
        if not success:
            backward(t["shapes"])
            place(t, board)
        return success

    return helper


# Rotate tetrimino clockwise or anticlockwise
rotate_clockwise = rotate_tetrimino("clockwise")
rotate_anticlockwise = rotate_tetrimino("anticlockwise")
