from board import Board
from piece import Piece


def test_move_playervsai():
    board = Board()
    assert board.get_destination_zone() == ([(5, 0), (6, 0), (6, 1), (7, 0), (7, 1), (7, 2)],
                                            [(0, 5), (0, 6), (0, 7), (1, 6), (1, 7), (2, 7)])

    result = board.evaluate("RED")
    assert result == 0


def test_calculate_distance():
    board = Board()
    result = board.calculate_distance(Piece(0, 5, 'GREEN'), [(5, 0)])
    assert result == 10


def test_move_compvscomp():
    board = Board()
    assert board.get_destination_zone() == ([(5, 0), (6, 0), (6, 1), (7, 0), (7, 1), (7, 2)],
                                            [(0, 5), (0, 6), (0, 7), (1, 6), (1, 7), (2, 7)])
    start = board.evaluate("RED")
    assert start == 0
    piece = Piece(1, 6, 'GREEN')
    board.move(piece, 2, 5)
    assert board.board[2] == ([0, 0, 0, 0, 0, piece, 0, Piece(1, 7, 'GREEN')])
    dist_after_move = board.evaluate('RED')
    assert board.get_destination_zone() == ([(5, 0), (6, 0), (6, 1), (7, 0), (7, 1), (7, 2)],
                                            [(0, 5), (0, 6), (0, 7), (1, 6), (1, 7), (2, 7)])
    assert dist_after_move == 1



