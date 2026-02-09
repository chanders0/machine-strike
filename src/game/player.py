class Player:
    def __init__(self, name, score=0, is_computer=False):
        self.name = name
        self.score = score
        self.is_computer = is_computer
        self.pieces = []