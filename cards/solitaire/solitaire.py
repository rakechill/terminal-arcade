"""The game of solitaire, playable from the command line. To play, type:  python3 solitaire.py  """

import pyCardDeck

class Card:
    ## maintain suit, color, and value
    # value: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K in str format?
    # suit: clubs, spades, hearts, diamonds
    # color: red/black
    # suits: unicode rep
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.color = ('red' if suit == 'hearts' or suit == 'diamonds' else 'black')
        self.visible = False
        self.suit_strs = {hearts: '\u2661', diamonds: '\u2662', spades: '\u2664', clubs: '\u2667'}

    def unicode(self):
        return self.suit_strs[self.suit]

    def __repr__(self):
        return '[%s%s ]' % (unicode(self), self.value)

"""<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>"""

class GameState:
    """ 
    Class that represents the current game state. Asks as a helper to the Game class.
    REMEMBER: only a K can be placed on empty stack and only an A can be played on empty slot!!!
    """

    def __init__(self, deck):
        self.deck = pyCardDeck.deck(deck)
        self.slots = [] # initialized with 4 lists of empty cards
        self.stacks = [] # initialized with 7 stacks and each stack has its # of cards and ONE is visible
    
    def __repr__(self):
        top_line = 'deck           s1   s2   s3   s4'
        deck_and_slots = ''
        return str


class Game:
    """init"""
    
    # deck in top left
    # 4 slots at top, which are just empty stacks
    # 7 stacks at bottom
    """
    deck           s1   s2   s3   s4
    [**]           [sA] [hA] [cA] [dA]

    1    2    3    4    5    6    7
    [s1] [**] [**] [**] [**] [**] [**]
         [h2] [**] [**] [**] [**] [**]
              [d3] [**] [**] [**] [**]
                   [c4] [**] [**] [**]
                        [s5] [**] [**]
                             [h6] [**]
                                  [d9] *
    """     
    def __init__(self):
        self.game_state = GameState(self, build_deck())
        self.deck = self.game_state.deck
        self.moves = []


    def move(card, destination):
        """Moves a card to a destination if it's a valid move."""
        return
    
    def undo():
        return 
    
    def build_deck():
        suits = [hearts, diamonds, clubs, spades]
        values = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


"""things to remember
- only K can be placed in empty space
- NOT EVERY GAME will be solvable, so need a quick way to start a new game
- way to access cards:  column numbers to be displayed and you ask 
                        for a specific card in that column. Returned will be
                        that card and all the cards above it IN CORRECT ORDER. 

- way to move cards:    make sure it's a valid move, and move the card to the to

- way to undo, keep past moves on stack!!! jus like amazons
        cases: card used to be in deck, card used to be on 1/7 stacks, card used to be in slots
"""
