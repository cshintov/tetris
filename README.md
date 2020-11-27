# Tetris

We all have played this game in our childhood. It needs no intro.

The thing to worry about here, how to write the game in Python. And more importantly
how do we represent the components and actions in the game.

The aim of this project is to make it possible to play the game in the commandline as well
as in the GUI.

## Tetriminoes

A tetrimino is nothing but the pieces in the game. There are 7 available, namely;
I, J, L, S, Z, T, O.

Next component in the game is the Tetris board. Standard size is 20 rows and 10 columns.

We have to allow the player to move the tetrimino left, right, down and rotate.

## Scoring

Let's keep it simple. 100 for each line cleared.

score = line x 100


