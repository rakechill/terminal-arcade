import pyCardDeck
from random import randint
import os
import time

"""<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>"""
class Player:

    def __init__(self, name, is_computer):
        self.name = name
        self.cards = []
        self.is_computer = is_computer
        self.uno = False

    def __repr__(self):
        return "Player: " + self.name

"""<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>"""
class Card:
    def __init__(self, value, color):
        self.value = value # 0-9 OR "plus4  ", "plus2  ", "skip   ", "reverse", "wild   "
        self.color = color # "yellow ", "red    ", "green  ", "blue   ", "choose "
        self.played = False

    def is_valid_play(self, discarded):
        if (discarded.value == "plus2  " or discarded.value == "plus4  ") and discarded.played == False:
            if self.value == discarded.value:
                return True
            else:
                return False
        elif self.color == discarded.color or self.value == discarded.value or self.value == "plus4  " or self.value == "wild   ":
            return True
        else:
            return False

    def is_adder(self):
        if self.value == "plus2  " or self.value == "plus4  ":
            return True
        return False 

    def __repr__(self):
        """
        Example: 
        =========
        |yellow |
        |6      |
        =========
        """
        val_str = ""
        if isinstance(self.value, int):
            val_str = str(self.value) + "      " 
        else:
            val_str = self.value
        
        return '\n=========\n|%s|\n|%s|\n=========\n' % (self.color, val_str)


"""<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>"""
class Game:
    def __init__(self, players, deck):
        self.players = players
        self.deck = pyCardDeck.Deck(deck)

        self.deck.shuffle()
        self.deal_cards()
        top_card = self.deck.draw()
        if top_card.color == "choose ":
            top_card.color = "red    " #for simplicity, completely arbitrary
        self.discard = top_card
        self.plus_cards = 0
        self.discarded = []

    def deal_cards(self):
        for card in range(7):
            for player in self.players:
                player.cards.append(self.deck.draw())

    def take_turn(self):
        
        if self.deck.cards_left < 10:
            self.deck = pyCardDeck.Deck(discarded).shuffle()
            self.discarded = []

        print("\nDISCARD PILE")
        print(self.discard)
        time.sleep(2)
        colors = ["red    ", "yellow ", "green  ", "blue   "]
        player = self.players[0] 
        valid_plays = [card for card in player.cards if Card.is_valid_play(card, self.discard)]

        if valid_plays == []:
            card_drawn = self.deck.draw()
            print(player.name + " drew a card.\n")
            time.sleep(1)

            if Card.is_valid_play(card_drawn, self.discard):
                player.cards.append(card_drawn)
                valid_plays.append(card_drawn)
            else:
                if Card.is_adder(self.discard):
                    self.discard.played = True
                for _ in range(self.plus_cards):
                    player.cards.append(self.deck.draw())
                if self.plus_cards > 0:
                    print(player.name + " had to draw " + str(self.plus_cards) +  " cards!")
                time.sleep(2)
                self.plus_cards = 0
                self.shift_players()
                return

        if player.is_computer:
            card = valid_plays[randint(0, len(valid_plays) - 1)]
            if card.color == "choose ":
                card.color = colors[randint(0, 3)]

        else:
            print("\nYOUR HAND")
            print(player.cards)

            index = input("\nPlay a card by typing a number between 1 and the number of cards in your hand: ").strip()
            while not isinstance(int(index), int):
                index = input("\nThat wasn't a valid number. Try again: ").strip()
            index = int(index) - 1

            card = player.cards[index]
            while card not in valid_plays:
                index = int((input("\nSorry, that's not a valid play. Try again: ")).strip()) - 1
                card = player.cards[index]
            
            if card.color == "choose ":
                print("What's the next color?")
                letter = (input("Type r for red, y for yellow, g for green, or b for blue: ")).strip() 
                for color in colors:
                    if letter == color[0]: # "red    ", "yellow ", "blue   ", "green  "
                        card.color = color   

        if Card.is_adder(card):
            for i in range(int(card.value[4])): # "plus2  " or "plus4  " at index 4 gives num of cards
                self.plus_cards += 1 

        print("\n" + player.name + " played a " + "\n")
        print(card)
        self.discarded.append(self.discard)
        self.discard = card
        player.cards.remove(card)
        self.effect()

    def effect(self):
        if self.discard.value == "reverse":
            self.players = self.players[::-1]
            print("\nREVERSED!\n")
        
        elif self.discard.value == "skip   ":
            print("\n" + self.players[1].name + " has been skipped!\n")
            self.shift_players()
            self.shift_players()

        else:
            self.shift_players()
        
        time.sleep(3)

    def shift_players(self):
        p = self.players
        p[0], p[1], p[2], p[3] = p[1], p[2], p[3], p[0]
        self.players = p

    def uno_or_over(self):
        for player in self.players:
            if len(player.cards) == 0:
                print("\nCongratulations, " + player.name + " you win!\n")
                time.sleep(1)
                return True
            elif len(player.cards) == 1:
                if player.uno == False:
                    print(player.name + " has an UNO!")
                    player.uno = True
                time.sleep(1) 
            else:
                player.uno = False
        return False


"""<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>"""
# deck is the same initially every time, so it
# didn't make sense to me to take a class-based approach.
def deck():
    my_deck = []
    colors = ["red    ", "yellow ", "green  ", "blue   "]
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, "skip   ", "reverse", "plus2  "]

    for color in colors:
        my_deck.append(Card(0, color))
        for value in values:
            my_deck.append(Card(value, color))
            my_deck.append(Card(value, color))
    
    for num in range(4):
        my_deck.append(Card("plus4  ", "choose "))
        my_deck.append(Card("wild   ", "choose "))

    return my_deck


"""<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>"""
def play_game():
    print("\nWelcome to the game of UNO!\n")

    option = input("\nType ONE to play against 3 computers\nor TWO to play with 2-4 people. ")
    while option != "ONE" and option != "TWO":
        option = input("\nType ONE to play against 3 computers\nor TWO to play with 2-4 people. ")

    if option == "ONE":
        name = input("\nWhat's your name, Player 1? ")
        game = Game([Player(name, False), Player("computer1", True), Player("computer2", True), Player("computer3", True)], deck())
        
    if option == "TWO":
        num_players = int(input("\nHow many people (including you) will be playing? ").strip())
        count = 0
        players = []
        while count < num_players:
            name = input("\nWhat's your name, Player " + str(count + 1) + " ")
            players.append(Player(name, False))
            count += 1
        while num_players != 4:
            players.append(Player("computer" + str(num_players), True))
            num_players += 1
        game = Game(players, deck())

    while not game.uno_or_over():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n")
        if game.players[0].is_computer:
            print(game.players[0].name + " is playing now...")
            time.sleep(1)
        else:
            input("It's your turn, " + game.players[0].name + ". Press any key to start. ")
        game.take_turn()

play_game()

    
again = input("Wanna play again? y/n ")
os.system('cls' if os.name == 'nt' else 'clear')
if again == "y":
    play_game()
