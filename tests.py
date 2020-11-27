from tetrimino import *

rows, colns = 20, 10
board = create_board(rows, colns)


place(tet_o, board, (18, 0))
place(tet_o, board, (8, 0))
place(tet_o, board, (0, 8))
place(tet_o, board, (0, 0))
print(board)
