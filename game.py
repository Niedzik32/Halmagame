import pygame
from board import Board
from constants import GREY, SQUARE_SIZE


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.selected = None
        self.board = Board()
        self.turn = "RED"
        self.options_of_moves = {}

    def winner(self):
        return self.board.check_winner()

    def update(self):
        self.board.draw(self.screen)
        self.draw_valid_moves(self.options_of_moves)

    def reset(self):
        self.selected = None
        self.board = Board()
        self.turn = "RED"
        self.options_of_moves = {}

    def select(self, row, col):
        """
        If piece was selected: select a place to move a piece,
        Else piece wasn't selected: show possible moves
        """
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.options_of_moves = self.board.get_options_of_move(piece)
            return True

        return False

    def _move(self, row, col):
        """
        piece can only move to square which has no pieces
        """
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0:
            if (row, col) in self.options_of_moves:
                self.board.move(self.selected, row, col)
                self.change_turn()
        else:
            return False
        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.screen, GREY, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self):
        self.options_of_moves = {}
        if self.turn == "RED":
            self.turn = "GREEN"
        else:
            self.turn = "RED"

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()
