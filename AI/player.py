'''
File: player.py
Project: AI
File Created: Wednesday, 13th June 2018 1:53:59 pm
Author: Josiah Putman (joshikatsu@gmail.com)
-----
Last Modified: Wednesday, 13th June 2018 1:54:09 pm
Modified By: Josiah Putman (joshikatsu@gmail.com)
'''
from abc import abstractmethod

class Player():
    def __init__(self):
        pass

    
    @abstractmethod
    def take_turn(self, rummikub_game):
        pass
