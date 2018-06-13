'''
File: tile.py
Project: game
File Created: Wednesday, 13th June 2018 12:55:46 pm
Author: Josiah Putman (joshikatsu@gmail.com)
-----
Last Modified: Wednesday, 13th June 2018 12:55:51 pm
Modified By: Josiah Putman (joshikatsu@gmail.com)
'''
from enum import Enum

class TileColor(Enum):
    RED = 1
    BLACK = 2
    ORANGE = 3
    BLUE = 4

class Tile():
    def __init__(self, num, color):
        """Constructor for tile
        
        Arguments:
            num {int} -- number on the tile
            color {TileColor} -- color of the tile
        """

        self.num = num
        self.color = color

    def __str__(self):
        """To string method for a tile
        
        Returns:
            string -- string representation
        """

        color_map = {
            TileColor.RED : 'R',
            TileColor.BLACK : 'B',
            TileColor.ORANGE : 'O',
            TileColor.BLUE : 'b'
        }

        return color_map[self.color] + str(self.num)

    def __repr__(self):
        return str(self)

def tile_from_string(tile_string):
    """Method to convert a string into a tile
    
    Arguments:
        tile_string {string} -- string representation of a tile
    
    Returns:
        Tile -- tile corresponding to the given string
    """

    color_char = tile_string[0]
    num = int(tile_string[1:])

    color_map = {
        'R' : TileColor.RED,
        'B' : TileColor.BLACK,
        'O' : TileColor.ORANGE,
        'b' : TileColor.BLUE
    }

    return Tile(num, color_map[color_char])
