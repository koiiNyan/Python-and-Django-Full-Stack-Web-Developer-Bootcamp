#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        print("Creating New Ordered Deck")
        # list comprehension
                # for r in RANKS:
                #     for s in SUITE:
                #         cards.append((s,r))

        # List of all cards in the deck
        self.cards = [(s,r) for s in SUITE for r in RANKS]

    def __str__(self):
        return f"I'm a deck with cards: {self.cards}"

    def shuffle(self):
        print("Shuffling")
        shuffle(self.cards)

    def split_in_half(self):
        # As there are 52 cards in the deck, splitting them in half gives us 26
        return (self.cards[:26], self.cards[26:])

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        # Reports back how many cards are left
        return f"Contains {len(self.cards)} cards"

    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        # Pops the last card
        return self.cards.pop()

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print(f"{self.name} has placed: {drawn_card}")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        for x in range(3):
            war_cards.append(self.hand.remove_card())
        return war_cards

    def still_has_cards(self):
        """
        Returns true if player still has cards left
        """
        return len(self.hand.cards) != 0



######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!

# Creating a new deck and splitting it in half:
deck = Deck()
deck.shuffle()
half1, half2 = deck.split_in_half()

# Creating both players
# Computer
computer = Player("computer", Hand(half1))
# Player
# Ask for player's name
player_name = input("What is your name? ")
player = Player(player_name, Hand(half2))

total_rounds = 0
war_count = 0

# Automatically playing the game as there are no decisions
while player.still_has_cards() and computer.still_has_cards():
    total_rounds += 1
    print("Time for a new round!")
    print(f"Now is round {total_rounds}")
    print("Here're the current standings:")
    print(f"{player.name} has {len(player.hand.cards)} cards")
    print(f"{computer.name} has {len(computer.hand.cards)} cards")
    print("Play a card!")
    print("\n")

    # Playing cards
    table_cards = []
    computer_card = computer.play_card()
    player_card = player.play_card()

    # Appending cards om the table
    table_cards.append(computer_card)
    table_cards.append(player_card)

    # Checking if there's a war, comparing ranks(index1)
    if computer_card[1] == player_card[1]:
        war_count += 1

        print("WAR!")

        # Each player turns up three cards
        table_cards.extend(player.remove_war_cards())
        table_cards.extend(computer.remove_war_cards())
        # Checking the highest rank
        # If player's card is higher, than he grabs all 6 cards
        if RANKS.index(player_card[1]) > RANKS.index(computer_card[1]):
            player.hand.add(table_cards)
        else:
            computer.hand.add(table_cards)

    # If there's no war
    else:
        print("NO WAR!")
        if RANKS.index(player_card[1]) > RANKS.index(computer_card[1]):
            player.hand.add(table_cards)
        else:
            computer.hand.add(table_cards)


# Game Over, when the while loop breaks
print("Game Over!")
print(f"Total number of rounds: {total_rounds}")
print(f"A war happed {war_count} times")
print(f"Computer still has cards? {computer.still_has_cards()}")
print(f"Player still has cards? {player.still_has_cards()}")
