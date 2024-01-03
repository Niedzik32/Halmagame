from copy import deepcopy
import pygame
from constants import Color


def minimax(position, depth, alpha, beta, max_player, game):
    """
    position - Takes some board which tells detalis about pieces
    depth - how many positions we want to consider
    max_player - if we want maximize the score or minimize
    minimax - give the best possible move for particular gamer
    """
    if depth == 0 or position.check_winner() is not None:
        print(f"{10*position.winner_green - 10*position.winner_red +  0.5*position.calculate_score('RED') -0.5*position.calculate_score('GREEN')} algo")
        return position.evaluate(game.turn), position

    if max_player:

        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, max_player, game):
            evaluation = minimax(move, depth-1, alpha, beta, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break

        return maxEval, best_move

    else:

        minEval = float('inf')
        best_move = None
        if game.turn == 'GREEN':

            for move in get_all_moves(position, Color.RED.name, game):

                evaluation = minimax(move, depth-1, alpha, beta, True, game)[0]
                minEval = min(minEval, evaluation)

                if minEval == evaluation:
                    best_move = move
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break

        else:

            for move in get_all_moves(position, Color.GREEN.name, game):
                evaluation = minimax(move, depth-1, alpha, beta, True, game)[0]
                minEval = min(minEval, evaluation)

                if minEval == evaluation:
                    best_move = move
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break

        return minEval, best_move


def simulate_move(piece, move, board, game):
    board.move(piece, move[0], move[1])

    return board


def get_all_moves(board, color, game):
    """
    get options of moves for every piece
    and create for it new board and take this piece to new board
    """
    # moves = [[board, piece], [new_board, piece]]
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_options_of_move(piece)
        # (row, col): [pieces]
        for move, skip in valid_moves.items():
            draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game)
            moves.append(new_board)
    return moves


def draw_moves(game, board, piece):
    valid_moves = board.get_options_of_move(piece)
    board.draw(game.screen)
    pygame.draw.circle(game.screen, (0, 255, 0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    pygame.time.delay(50)
