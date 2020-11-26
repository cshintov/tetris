""" The game of Tetris 

https://tetris.fandom.com/wiki/SRS

The game happens in a grid of size R x C. Each cell will have a color. Each shape like
S, T, I, L, etc. will represented by their own colors. Each shape has varying number of rotations.
For example L has 4 and O has only 1. We have to also represent locked positions.

Get random shaped pieces. 
Set speed of falling down. Represent falling down.
Keys: L, R, U, D

U: rotate the piece

Start falling piece on the center.

Check if the move is valid.

Clear rows when the row is filled.

Check lost.


Classes: Tetris, TetrisBoard, Tetriminoes

Tetris will handle game play.

TetrisBoard: everything related to piece movement.

Tetriminoes: The pieces.
"""

import numpy as np
import pygame
from board import *
import tetriminoes as tet

fps = pygame.time.Clock()

# while True:
#     fps.tick(2)  # Makes the loop run twice a second
#     print("frame")


class Tetris(object):
    def __init__(self, r, c):
        self.board = TetrisBoard(r, c)
        self.cur_piece = None
        self.next_piece = None
        self.piece_position = (4, 0)

    def __str__(self):
        return str(self.board)

    def get_current_piece(self):
        return self.cur_piece

    def get_next_piece(self):
        return self.next_piece

    def get_current_piece_size(self):
        return size(self.cur_piece)

    def update(self):
        self.board.place(self.cur_piece)

    def remove_piece(self):
        size = self.cur_piece.size()
        empty = tet.Tetrimino("E", np.zeros(size), self.cur_piece.pos)
        self.board.place(empty)

    def move_piece_left(self):
        piece = self.cur_piece
        try:
            x, y = left(self.board, *piece.pos)
        except TypeError:
            print("Can't move left!")
            return
        self.remove_piece()
        piece.pos = x, y
        self.update()

    def move_piece_right(self):
        piece = self.cur_piece
        try:
            # __import__("nose").tools.set_trace()
            x, y = right(self.board, *piece.pos)
        except TypeError:
            print("Can't move right!")
            return
        self.remove_piece()
        piece.pos = x, y
        self.update()

    def move_piece_down(self):
        piece = self.cur_piece
        try:
            # __import__("nose").tools.set_trace()
            x, y = down(self.board, *piece.pos)
        except TypeError:
            print("Can't move down!")
            return
        self.remove_piece()
        piece.pos = x, y
        self.update()

    def rotate_piece(self):
        pass


def main():
    tetris = Tetris(20, 10)
    o = tet.TETRIMINOES["O"]
    tetris.cur_piece = o
    tetris.update()
    print(tetris)

    tetris.move_piece_right()
    tetris.move_piece_right()
    tetris.move_piece_right()
    # tetris.move_piece_right()
    print(tetris)


if __name__ == "__main__":
    main()
