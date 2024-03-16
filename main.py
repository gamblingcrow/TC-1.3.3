import random

 

class Card:

 

    SUITS = ("clubs", "spades", "hearts", "diamonds")

 

    RANKS = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "j": 11,
        "q": 12,
        "k": 13,
        "a": 14,
    }

 

    face_up = False # is this needed?

 

    def __init__(self, suit, rank, face_up=False):
        self.suit = suit
        self.rank = rank
        self.face_up = face_up

 

    @property
    def rank(self):
        return self._rank

 

    @rank.setter
    def rank(self, rank):
        self._rank = rank

 

    @property
    def face_up(self):
        return self._face_up

 

    @face_up.setter
    def face_up(self, face_up):
        self._face_up = face_up

 

#class game:

 

# Game start, deck build, shuffle and split

 

deck = []

 

for suit in SUITS:
    for rank in RANKS:
        card = Card(suit, rank)
        deck += card

 

random.shuffle(deck)

 

computer_deck = deck[:27]
user_deck = deck[28:]

 

 

# Game logic

 

computer_cards_in_play = []

 

user_cards_in_play = []

 

def computer_move():
    computer_cards_in_play += computer_deck[0].face_up(True)
    computer_deck.pop(0)

 

def user_move():
    if input("Press 'Enter' to make a move"):
        computer_cards_in_play += computer_deck[0].face_up(True)
        computer_deck.pop(0)

 

def compare_last_cards():
    if computer_cards_in_play[-1:].rank > user_cards_in_play[-1:].rank:
        return_cards("computer") # merge both cards in play, shuffle and append to computer's deck
    elif computer_cards_in_play[-1:].rank < user_cards_in_play[-1:].rank:
        return_cards("user") # merge both cards in play, shuffle and append to user's deck
    elif computer_cards_in_play[-1:].rank == user_cards_in_play[-1:].rank:
        war() # both place a face down card and face up card, check again

 

def war():
    computer_cards_in_play += computer_deck[0]
    computer_deck.pop(0)
    computer_move()
    user_cards_in_play += user_deck[0]
    user_deck.pop(0)
    user_move()
    compare_last_cards()

 

def return_cards(winner):
    return_pile += computer_cards_in_play + user_cards_in_play
    for card in return_pile:
        card.face_up(False)
    random.shuffle(return_pile)
    if winner == "computer":
        computer_deck += return_pile
    if winner == "user":
        user_deck += return_pile

 

def print_cards_in_play():
    print("Computer: ", end="")
    for card in computer_cards_in_play:
        print(card, end="")
    print()
    print("User: ", end="")
    for card in user_cards_in_play:
        print(card, end="")
    print()

 

def main():
    computer_move()
    user_move()
    compare_last_cards()