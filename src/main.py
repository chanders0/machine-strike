from src.game.player import Player
from src.game.board import Board
from src.game.piece import Piece

def main():
    print("Welcome to Machine Strike!")

    # player setup
    name = input("Enter your name: ")
    human = Player(name)
    computer = Player("Computer", is_computer=True)

    # board setup
    board = Board()
    board.setup_terrain()
    board.print_board()

# call main
if __name__ == "__main__":
    main()