from Tile import Tile


class Agent:

    def __init__(self, game, color, max_depth):
        self.game = game
        self.color = color
        self.max_depth = max_depth

    def do_min_max(self, current_board):
        move, value = self.max(current_board, self.color, 0, float('-inf'), float('+inf'))

        return move

    def max(self, current_board, current_color, depth, a, b):

        if self.game.check_terminal(current_board, current_color):
            return None, self.game.evaluate(current_board, current_color, -1000)

        if depth == self.max_depth:
            return None, self.game.evaluate(current_board, current_color)

        possible_moves = self.game.generate_all_possible_moves(current_board, current_color)
        best_move = None
        best_move_value = float('-inf')
        for move in possible_moves:
            temp_move, value = self.min(current_board.next_board(current_color, move), self.game.opponent(current_color), depth + 1, a, b)
            if value > best_move_value:
                best_move_value = value
                best_move = move

                if value >= b:
                    return best_move, best_move_value
                if a < value:
                    a = value

        return best_move, best_move_value

    def min(self, current_board, current_color, depth, a, b):
        if self.game.check_terminal(current_board, current_color):
            return None, self.game.evaluate(current_board, current_color, +1000)

        if depth == self.max_depth:
            return None, self.game.evaluate(current_board, current_color)

        possible_moves = self.game.generate_all_possible_moves(current_board, current_color)
        best_move = None
        best_move_value = float('+inf')
        for move in possible_moves:
            temp_move, value = self.max(current_board.next_board(current_color, move), self.game.opponent(current_color), depth + 1, a, b)
            if value < best_move_value:
                best_move_value = value
                best_move = move

                if value <= a:
                    return best_move, best_move_value
                if b > value:
                    b = value

        return best_move, best_move_value
