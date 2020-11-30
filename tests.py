from tetrimino import *

rows, colns = 20, 10
board = create_board(rows, colns)

tet = O

tet["pos"] = (18, 0)
place(tet, board)
tet["pos"] = (8, 0)
place(tet, board)
tet["pos"] = (0, 8)
place(tet, board)
print(board)
move_left(tet, board)
place(tet, board)
print(board)

tet["pos"] = (0, 0)
place(tet, board)
print(board)
move_right(tet, board)
print(board)
move_down(tet, board)
place(tet, board)
tet["pos"] = (18, 8)
move_down(tet, board)
place(tet, board)
print(board)
move_right(tet, board)
print(board)

tet = L
# L["pos"] = (0, 5)
# place(L, board)
# print(board)
# rotate_clockwise(L, board)
# print(board)
# rotate_anticlockwise(L, board)
# print(board)
