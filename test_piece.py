from piece import Piece
from constants import GREEN


def test_create_piece():
    piece = Piece(0, 7, GREEN)
    assert piece.row == 0
    assert piece.col == 7
    assert piece.color == GREEN


def test_calc_pos():
    piece = Piece(0, 7, GREEN)
    assert piece.x == 750
    assert piece.y == 50


def test_move():
    piece = Piece(1, 0, GREEN)
    piece.move(2, 0)
    assert piece.x == 50
    assert piece.y == 250
