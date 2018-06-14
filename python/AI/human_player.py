'''
File: human_player.py
Project: AI
File Created: Wednesday, 13th June 2018 1:33:35 pm
Author: Josiah Putman (joshikatsu@gmail.com)
-----
Last Modified: Wednesday, 13th June 2018 1:33:53 pm
Modified By: Josiah Putman (joshikatsu@gmail.com)
'''

from game.tile import tile_from_string

class HumanPlayer():
    def __init__(self, player_id):
        self.player_id = player_id
        self.hand = []

    def take_turn(self, rummikub_game):
        print("Player", self.player_id, "   Hand:", self.hand)
        play_command = input("Enter your play:")

        new_tile_sets = []

        # parse the play command
        tile_set_split = play_command.split(";")
        for tile_set_string in tile_set_split:
            print("tile_set_string =", tile_set_string)

            tile_set = []
            tiles_split = tile_set_string.split(",")

            for tile_string in tiles_split:
                tile_set.append(tile_from_string(tile_string))

            new_tile_sets.append(tile_set)

        if rummikub_game.is_valid_play(new_tile_sets):
            rummikub_game.make_play(new_tile_sets)
