'''
File: rummi.py
Project: game
File Created: Wednesday, 13th June 2018 12:58:18 pm
Author: Josiah Putman (joshikatsu@gmail.com)
-----
Last Modified: Wednesday, 13th June 2018 12:58:19 pm
Modified By: Josiah Putman (joshikatsu@gmail.com)
'''

from random import shuffle

from game.tile import Tile, TileColor

class RummikubGame():
    def __init__(self, players):
        """Constructor for a game of rummikub
        """

        self.players = players

        self.tiles = []
        self.tile_sets = []
        self.tiles_in_play = []

        self.init_tiles()
        

    def init_tiles(self):
        """Initializes the tiles
        """

        # initializes the tiles to a full rummikub game
        for num in range(1, 14):    # 1-13
            for color in TileColor:

                print("Created tile with num", num, "and color", color)
                self.tiles.append(Tile(num, color))

        # add jokers, denoted by 0
        self.tiles.append(Tile(0, TileColor.RED))
        self.tiles.append(Tile(0, TileColor.BLACK))

    def shuffle(self):
        """Shuffles the list of tiles
        """

        shuffle(self.tiles)

    def deal_hand(self, player):
        """Shuffles the tiles and deals a random hand of 14 tiles
        
        Returns:
            hand -- the hand dealt
        """

        self.shuffle()

        player.hand = []

        for _ in range(14):     # deal 14 cards
            player.hand.append(self.tiles.pop())


    def make_play(self, new_tile_sets, played_tiles):
        """Makes a play by changing the sets
        
        Arguments:
            new_sets {list} -- list of sets to replace with
        """

        self.tile_sets = new_tile_sets
        self.tiles_in_play += played_tiles

    def get_valid_plays(self, played_tiles):
        """Method to get all valid plays using a given piece
        
        Arguments:
            played_tile {Tile} -- [description]
        """

        # consider all plays 
        pass

    def is_valid_play(self, new_sets):
        """Method to check if a list of new sets is valid
        
        Arguments:
            new_sets {list} -- list of sets of tiles
        
        Returns:
            bool -- true if valid, false otherwise
        """


        # check all sets, which should be sorted to begin with
        for tile_set in new_sets:
            
            run_color = tile_set[0].color
            run_num = tile_set[0].num
            is_run = len(tile_set) >= 3

            group_num = tile_set[0].num
            group_colors = set([tile_set[0].color])
            is_group = len(tile_set) >= 3

            for tile in tile_set[:-1]:
                
                # if it could still be a run, check if this tile is valid for the run
                if is_run:
                    increasing = tile.num == run_num + 1
                    same_color = run_color == tile.color
                    is_run = (increasing and same_color) or tile.num == 0

                # if it could still be a group, check if this tile is valid for the group
                if is_group:
                    same_number = tile.num == group_num
                    diff_color = tile.color not in group_colors
                    is_group = (same_number and diff_color) or tile.num == 0

                if not is_run and not is_group:
                    return False

        # if it is a run or a group, return true
        return True

    def deal_hands(self):
        for player in self.players: 
            self.deal_hand(player)

    def take_turns(self):
        for player in self.players:
            player.take_turn(self)

    def game_over(self):
        return 
