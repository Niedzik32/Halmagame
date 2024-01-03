import pygame
from constants import MODE, PIECES, SQUARE_SIZE, ROWS, COLS
from constants import BROWN, WHITE, Color
from piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.green_left = PIECES
        self.winner_red = 0
        self.winner_green = 0
        self.create_board()

    def draw_squares(self, screen):
        """
        Drawing brown squares on board
        """
        screen.fill(WHITE)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                sq = SQUARE_SIZE
                x = col * SQUARE_SIZE
                y = row * SQUARE_SIZE
                pygame.draw.rect(screen, BROWN, (x, y, sq, sq))

    def create_board(self):
        """
        create self.board which consists lists of rows,
        inside of each of list of rows there're pieces or empty square (0)
        """
        constant = PIECES // 4
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):

                if PIECES == 6:
                    max_piec_in_row = PIECES//2
                    if col >= COLS - max_piec_in_row and row < max_piec_in_row:
                        if col >= COLS - max_piec_in_row + row:
                            self.board[row].append(Piece(row, col, Color.GREEN.name))
                        else:
                            self.board[row].append(0)
                    elif row >= ROWS-max_piec_in_row and col < max_piec_in_row:
                        if row >= ROWS - max_piec_in_row + col:
                            self.board[row].append(Piece(row, col, Color.RED.name))
                        else:
                            self.board[row].append(0)
                    else:
                        self.board[row].append(0)

                elif PIECES == 13 or PIECES == 19:
                    if col >= COLS - constant - 1:
                        if row <= PIECES // 4:
                            if row == 0:
                                self.board[row].append(Piece(row, col, Color.GREEN.name))
                            elif col >= COLS - 2 - constant + row:
                                self.board[row].append(Piece(row, col, Color.GREEN.name))
                            else:
                                self.board[row].append(0)
                        else:
                            self.board[row].append(0)
                    elif row >= ROWS - constant - 1:
                        if col <= constant:
                            if col == 0:
                                self.board[row].append(Piece(row, col, Color.RED.name))
                            elif row >= ROWS - 2 - constant + col:
                                self.board[row].append(Piece(row, col, Color.RED.name))
                            else:
                                self.board[row].append(0)
                        else:
                            self.board[row].append(0)
                    else:
                        self.board[row].append(0)
                else:
                    raise ValueError("Number of pieces can be 6, 13 or 19")

    def evaluate(self, current_turn):
        """
        Maxmaizing player: GREEN,
        Minimizing player: RED
        The higher result of the function the better move for the green,
        the smaller result of the function the better move for the red
        """
        green_score = 0.5*self.calculate_score("GREEN")
        red_score = 0.5*self.calculate_score("RED")
        score = red_score - green_score
        green_turn = 10*self.winner_green - 10*self.winner_red
        red_turn = self.winner_red - self.winner_green
        if MODE == 'COMPvsCOMP':
            if current_turn == "GREEN":
                return green_turn + score
            else:
                return red_turn - score

        elif MODE == 'COMPvsPLAYER':
            return green_turn + score

    def get_destination_zone(self):
        """
        Creates list of positions
        where player's pieces should be to win
        """
        constant = PIECES // 4
        green_des_pos = []
        red_des_pos = []

        for row in range(ROWS):
            for col in range(COLS):
                if PIECES == 6:
                    max_p_in_row = PIECES//2
                    if col >= COLS - max_p_in_row and row < max_p_in_row:
                        if col >= COLS - max_p_in_row + row:
                            red_des_pos.append((row, col))
                    elif row >= ROWS - max_p_in_row and col < max_p_in_row:
                        if row >= ROWS - max_p_in_row + col:
                            green_des_pos.append((row, col))

                elif PIECES == 13 or PIECES == 19:
                    if col >= COLS - constant - 1:
                        if row <= PIECES // 4:
                            if row == 0:
                                red_des_pos.append((row, col))
                            elif col >= COLS - 2 - constant + row:
                                red_des_pos.append((row, col))

                    elif row >= ROWS - constant - 1:
                        if col <= constant:
                            if col == 0:
                                green_des_pos.append((row, col))

                            elif row >= ROWS - 2 - constant + col:
                                green_des_pos.append((row, col))

        return green_des_pos, red_des_pos

    def calculate_distance(self, piece, destination_zone):
        """
        calculate distance from every piece to every winning square
        """
        min_distance = float('inf')

        for dest_row, dest_col in destination_zone:
            distance = abs(piece.row - dest_row) + abs(piece.col - dest_col)
            min_distance = min(min_distance, distance)

        return min_distance

    def calculate_score(self, color):
        """
        calculate sum of distances to every winning square
        """
        total_distance = 0
        green_des_pos, red_des_pos = self.get_destination_zone()

        if color == "GREEN":
            for piece in self.get_all_pieces(color):
                total_distance += self.calculate_distance(piece, green_des_pos)
        elif color == "RED":
            for piece in self.get_all_pieces(color):
                total_distance += self.calculate_distance(piece, red_des_pos)

        return total_distance

    def get_all_pieces(self, color):
        """
        get possible moves for all of the pieces of particular color
        """
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def check_winner(self):
        """
        Counts how much pieces of every color are at winning squares
        """
        constant = PIECES // 4
        green_winners = set()  # Use a set to store unique green winners
        red_winners = set()  # Use a set to store unique red winners

        for row in range(ROWS):
            for col in range(COLS):
                if PIECES == 6:
                    max_piec_in_row = PIECES//2
                    if col >= max_piec_in_row and row < max_piec_in_row:
                        if col >= COLS - max_piec_in_row + row:
                            current_piece = self.board[row][col]

                            if isinstance(current_piece, Piece):
                                if current_piece.color == Color.RED.name:
                                    red_winners.add(current_piece)

                    elif row >= max_piec_in_row and col < max_piec_in_row:
                        if row >= ROWS - max_piec_in_row + col:
                            current_piece = self.board[row][col]

                            if isinstance(current_piece, Piece):
                                if current_piece.color == Color.GREEN.name:
                                    green_winners.add(current_piece)

                elif PIECES == 13 or PIECES == 19:
                    if col >= COLS - constant - 1:
                        if row <= PIECES // 4:
                            if row == 0:
                                current_piece = self.board[row][col]
                                if isinstance(current_piece, Piece):
                                    if current_piece.color == Color.RED.name:
                                        red_winners.add(current_piece)
                            elif col >= COLS - 2 - constant + row:
                                current_piece = self.board[row][col]
                                if isinstance(current_piece, Piece):
                                    if current_piece.color == Color.RED.name:
                                        red_winners.add(current_piece)

                    elif row >= ROWS - constant - 1:
                        if col <= constant:
                            if col == 0:
                                current_piece = self.board[row][col]
                                if isinstance(current_piece, Piece):
                                    if current_piece.color == Color.GREEN.name:
                                        green_winners.add(current_piece)

                            elif row >= ROWS - 2 - constant + col:
                                current_piece = self.board[row][col]
                                if isinstance(current_piece, Piece):
                                    if current_piece.color == Color.GREEN.name:
                                        green_winners.add(current_piece)

        self.winner_green = len(green_winners)  # Count unique green winners
        self.winner_red = len(red_winners)  # Count unique red winners

        if self.winner_green == PIECES:
            return "GREEN WON"
        elif self.winner_red == PIECES:
            return "RED WON"

        return None

    def draw(self, screen):
        """
        draw pieces on board
        """
        self.draw_squares(screen)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(screen)

    def move(self, piece, row, col):
        """
        Moving single piece
        Swaping positions of piece and "0" in empty square
        """
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

    def get_piece(self, row, col):
        return self.board[row][col]

    def get_options_of_move(self, piece):
        """
        Start - min_jump from row of the piece, stop - max_jump for 2 rows
        """
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        col = piece.col
        row = piece.row
        # (4,5): [(2,3)]

        # traverse left up
        moves.update(self._traverse_left(row-1, max(row-3, -1), -1, piece.color, left))

        # traverse right up
        moves.update(self._traverse_right(row-1, max(row-3, -1), -1, piece.color, right))

        # traverse left down
        moves.update(self._traverse_left(row+1, min(row+3, ROWS), 1, piece.color, left))

        # traverse right down
        moves.update(self._traverse_right(row+1, min(row+3, ROWS), 1, piece.color, right))

        # go up
        moves.update(self._up(row-1, max(row-3, -1), -1, piece.color, col))

        # go down
        moves.update(self._down(row+1, min(row+3, ROWS), 1, piece.color, col))

        # go right
        moves.update(self._right(col+1, min(col+3, COLS), 1, piece.color, row))

        # go left
        moves.update(self._left(col-1, max(col-3, -1), -1, piece.color, row))

        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._traverse_left(r+step, row, step, color, left-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left+1, skipped=last))
                    moves.update(self._traverse_left(r-step, row, -step, color, left-1, skipped=last))
                    moves.update(self._traverse_right(r-step, row, -step, color, left+1, skipped=last))

                break
            else:
                last = [current]
            left -= 1

        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._traverse_left(r+step, row, step, color, right-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right+1, skipped=last))
                    moves.update(self._traverse_left(r-step, row, -step, color, right-1, skipped=last))
                    moves.update(self._traverse_right(r-step, row, -step, color, right+1, skipped=last))

                break
            else:
                last = [current]
            right += 1
        return moves

    def _up(self, start, stop, step, color, up, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if up < 0:
                break

            current = self.board[r][up]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, up)] = last + skipped
                else:
                    moves[(r, up)] = last
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._up(r+step, row, step, color, up, skipped=last))
                    moves.update(self._down(r-step, row, -step, color, up, skipped=last))
                break
            else:
                last = [current]
        return moves

    def _down(self, start, stop, step, color, down, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if down >= ROWS:
                break

            current = self.board[r][down]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, down)] = last + skipped
                else:
                    moves[(r, down)] = last
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._down(r+step, row, step, color, down, skipped=last))
                    moves.update(self._up(r-step, row, -step, color, down, skipped=last))

                break
            else:
                last = [current]
        return moves

    def _right(self, start, stop, step, color, right_row, skipped=[]):
        moves = {}
        last = []
        for c in range(start, stop, step):
            if c > COLS:
                break

            current = self.board[right_row][c]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(right_row, c)] = last + skipped
                else:
                    moves[(right_row, c)] = last
                if last:
                    if step == -1:
                        row = max(c-3, 0)
                    else:
                        row = min(c+3, ROWS)

                    moves.update(self._right(c+step, row, step, color, right_row, skipped=last))
                    moves.update(self._left(c-step, row, -step, color, right_row, skipped=last))
                break
            else:
                last = [current]

        return moves

    def _left(self, start, stop, step, color, left_row, skipped=[]):
        moves = {}
        last = []
        for c in range(start, stop, step):
            if c < 0:
                break

            current = self.board[left_row][c]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(left_row, c)] = last + skipped

                else:
                    moves[(left_row, c)] = last

                if last:
                    if step == -1:
                        row = max(c-3, 0)
                    else:
                        row = min(c+3, ROWS)

                    moves.update(self._left(c+step, row, step, color, left_row, skipped=last))
                    moves.update(self._right(c-step, row, -step, color, left_row, skipped=last))

                break
            else:
                last = [current]

        return moves
