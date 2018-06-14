'''
File: test_rummi.py
Project: RummikubAI
File Created: Wednesday, 13th June 2018 12:54:50 pm
Author: Josiah Putman (joshikatsu@gmail.com)
-----
Last Modified: Wednesday, 13th June 2018 1:32:34 pm
Modified By: Josiah Putman (joshikatsu@gmail.com)
'''

from game.rummi import RummikubGame
from AI.human_player import HumanPlayer

def main():
    
    player1 = HumanPlayer(1)
    player2 = HumanPlayer(2)

    game = RummikubGame((player1, player2))

    game.deal_hands()

    # main game loop
    while not game.game_over():
        game.take_turns()

if __name__ == "__main__":
    main()
