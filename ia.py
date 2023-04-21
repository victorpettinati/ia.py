import random

class SimpleAI:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self):
        available_moves = [point for point in XO_points if not point.value]

        if available_moves:
            move = random.choice(available_moves)
            move.set()

