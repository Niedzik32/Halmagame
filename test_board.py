from board import Board
from constants import ROWS, COLS, PIECES, Color
from piece import Piece


def test_create_board_object():
    # PIECES = 6
    board = Board()
    assert board.red_left == 6
    assert board.green_left == 6
    assert board.winner_green == 0
    assert board.winner_red == 0

    # board.board[0][0] = Piece(11, 11, BUTTON_WHEELUP)
    # assert repr(board.board[0][11]) == '(0, 204, 0)'


def test_create_board_table():
    board = Board()
    piece = board.board[0][COLS-1]
    assert isinstance(piece, Piece)
    assert piece.color == "GREEN"


def test_check_winner():
    board = Board()
    for row in range(ROWS):
        for col in range(COLS):
            PIECES == 6
            max_piec_in_row = PIECES//2
            if col >= COLS - max_piec_in_row and row < max_piec_in_row:
                if col >= COLS - max_piec_in_row + row:
                    board.board[row][col] = Piece(row, col, Color.RED.name)

    board.check_winner()
    assert board.winner_red == 6
    assert board.check_winner() == "RED WON"


def test_get_moves():
    # WIDTH, HEIGHT = 800, 800
    # ROWS, COLS = 10, 10
    # SQUARE_SIZE = WIDTH//COLS
    # # 3 possible amount of pieces: 6, 13, 19
    # PIECES = 6
    board = Board()
    result = board._left(2, 0, -1, Color.GREEN.name, 0, skipped=[])
    assert result == {(0, 2): []}


def test_calculate_distance():
    board = Board()
    piece = Piece(0, 5, Color.GREEN.name)
    desination_zone = [(4, 0), (4, 1)]
    assert board.calculate_distance(piece, desination_zone) == 8


def test_move():
    board = Board()
    piece = Piece(1, 0, Color.GREEN.name)
    board.move(piece, 2, 0)
    assert piece.row == 2
    assert piece.col == 0
    assert piece.x == 50
    assert piece.y == 250


def test_get_piece():
    board = Board()
    piece = Piece(0, 6, Color.GREEN.name)
    assert board.get_piece(0, 6).color == piece.color
    assert board.get_piece(0, 6).row == piece.row
    assert board.get_piece(0, 6).col == piece.col


def test_get_options_of_move():
    board = Board()
    piece = Piece(6, 1, Color.RED.name)
    assert board.get_options_of_move(piece) == {(5, 2): [], (5, 1): [], (6, 2): []}
