from game.tile import Tile
import random

class Board:
    def __init__(self):
        self.size = 8
        self.grid = [[None for _ in range(self.size)] for _ in range(self.size)]
    
    def setup_terrain(self):
        terrain_options = [
            ("grassland", 0),
            ("forest", 1),
            ("hill", 2),
            ("mountain", 3)
        ]

        for y in range(self.size//2):
            for x in range(self.size):
                terrain_type, height = random.choice(terrain_options)
                
                mirror_x = self.size - 1 - x
                mirror_y = self.size - 1 - y

                self.grid[y][x] = Tile(terrain_type, height) # top half
                self.grid[mirror_y][mirror_x] = Tile(terrain_type, height) # bottom half
    
    def print_board(self):
        for row in self.grid:
            line = ""
            for tile in row:
                if tile.terrain_type == "grassland":
                    line += "G "
                elif tile.terrain_type == "forest":
                    line += "F "
                elif tile.terrain_type == "hill":
                    line += "H "
                elif tile.terrain_type == "mountain":
                    line += "M "
            print(line)