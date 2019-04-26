from random import shuffle


# Create a class that assigns each tile with a color and declares that all cards start unmatched and face down
class Tile:
    def __init__(self, color):
        self.color = color
        self.matched = False
        self.backgroundColor = "black"
        self.score = 11

# These are to put each tile into the tile class and define what color they are. Each tile will have 1 match


tile1 = Tile("blue")
tile2 = Tile("blue")
tile3 = Tile("red")
tile4 = Tile("red")
tile5 = Tile("lightGreen")
tile6 = Tile("lightGreen")
tile7 = Tile("yellow")
tile8 = Tile("yellow")
tile9 = Tile("purple")
tile10 = Tile("purple")
tile11 = Tile("white")
tile12 = Tile("white")
tile13 = Tile("gray")
tile14 = Tile("gray")
tile15 = Tile("darkGreen")
tile16 = Tile("darkGreen")
tile17 = Tile("teal")
tile18 = Tile("teal")
tile19 = Tile("orange")
tile20 = Tile("orange")

# Here is a list of all the possible tiles
tiles = [tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9, tile10,
         tile11, tile12, tile13, tile14, tile15, tile16, tile17, tile18, tile19, tile20]

# This function will shuffle the cards every time the user opens
shuffle(tiles)
