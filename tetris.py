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

    def move_piece_left(self):
        piece = self.cur_piece
        new_pos = left(self.piece_position)
        self.place(piece)

    def move_piece_right(self):
        pass

    def rotate_piece(self):
        pass


class TetrisBoard(object):

    """Represents a Tetris Board."""

    def __init__(self, rows, colns):
        """ Creates a rows X colns grid """
        self.board = zeros((rows, colns))
        self.size = rows, colns

    def place(self, piece):
        place(piece, self.board)


def main():
    tetris = Tetris(20, 10)
    o = tet.TETRIMINOES["O"]
    tetris.cur_piece = o
    # tetris.place(o)
    print(tetris)

    tetris.move_piece_left()
    print(tetris)


if __name__ == "__main__":
    main()
