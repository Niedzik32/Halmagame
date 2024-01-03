# HalmaGame


## Name
Halma Game


## Description
This project enable to play Halma game with another user, computer or watch play computer vs computer.
Rules of Halma:
PL - https://bonaludo.com/2018/08/06/halma-piekno-tkwi-w-prostocie/
ENG - https://bonaludo.com/2018/08/17/halma-the-beauty-of-simplicity/

I decided to consider 3 options of number of pieces and every imgaginable size of board. User can change detalis in constants.py. Every parameter is listed and change there will influence whole project without breaking it.
In order to improve testing I added option of play with 6 pieces per player. This is not accroding to Halma rules, but it significantly decrease gameplay time.

All tests are based on constants:
    WIDTH, HEIGHT = 800, 800
    ROWS, COLS = 8, 8
    SQUARE_SIZE = WIDTH//COLS
    PIECES = 6
    Color = Enum('Color', {"RED": (255, 0, 0), "GREEN": (0, 204, 0)})
    BROWN = (188, 170, 164)
    WHITE = (255, 255, 255)
    GREY = (128, 128, 128)



## Instruction manual
In order to choose game mode, number of pieces, colors and size of the board, go to constants.py change values of the parametrs. Attention! The number of pieces can only be 6, 13 or 19. In case of other parameters you can choose size of board between 6 and 16 while playing with 6 pieces and size board between 8 and 16 while playing with 13 or 19 pieces.
However, if you are playing with 6 pieces, I recommend choosing a board with a maximum of 10 by 10.
Also, as rules of the game says, while playing with 19 pieces it is better to choose board 16x16.


## Construction

Game is based on pygame library to better visualise board and moves of pieces.
Project consists of main.py, board.py, game.py, piece.py, test_board.py, test_piece.py, algorithm.py and constants.py.
I decided to divide project into such files as it is more readable.

Files:
main.py - contains most of the pygame visualization and check different events such mouse press on window, it also initialize minimax algorithm depending on game mode

board.py - the most developed file - consists of creating board from drawing it to placement of pieces, it checks winner, implements moves of pieces to every direction and add evaluation used in algorithm of computer - it is so developed as most of the game logic is based on "self.board" which is description of every square of the board

piece.py - contains mechanism of creating single piece

constants.py - it is a separate file, beacause it enables changing basic parameters at the pleasure of user (such as mode of the game, size of the board, colors of pieces and board)

game.py - contains basic functions, which are necessary to proper swaping turns

algorithm.py - contains minimax algorithm, which is a module implementing the computer game algorithm


Classes:
Board - while initializing there is created board which is two-dimensional list which "first demenstion" are rows and "second demension" are columns. It also consists the number of pieces and how many pieces are in the winning zone.

Piece - enable to create single piece with parameteres such as color, position (x, y) and placement on board (row, column)

Game - handles game logic


## Visuals
[An example of a game player vs player](https://youtu.be/hypF6F5U-0w)
[An example of a game computer vs player](https://youtu.be/97xK1LM-6Z0)


## Author
Klaudia Niedziałkowska


## Project status
Minimax algorithm works good only on depth 1. However according to foundation of minimax the bigger depth the better game of computer.
In case of game mode compvscomp there is a problem while finishing the game. Pieces seem to be in loop.
I tried my best to fix it., but I failed.

Lines which are too long can't be shortened as it would break the code.