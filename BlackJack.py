"""
This is a complete blackjack game that I made as a milestone project. Hope you enjoy!
"""
# imports
import random

# Global Variables
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True
# Classes


class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        my_deck = ''
        for card in self.deck:
            my_deck += '\n ' + card.__str__()
        return my_deck

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        delt = self.deck.pop()
        return delt


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def add_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# function definitions
    # Takes a valid bet as an input.

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input(f'Please place your bet. You currently have {chips.total} chips\n'))
        except ValueError:
            print('Nice try!')
        else:
            if chips.bet == 1:
                print(f'You have successfully bet {chips.bet} chip. ')
                break
            elif chips.total >= chips.bet > 1:
                print(f'You have successfully bet {chips.bet} chips.')
                break
            else:
                if chips.bet > chips.total:
                    print('You may not bet more than you have.')

# Function for player and dealer hit.


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.add_for_ace()

# Function to hit or stand


def hit_or_stand(deck, hand):
    global playing

    while playing:
        x = input('Would you like to hit or stand?: Enter "h" or "s"\n')

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print('Player stands. Dealer will now finish their turn...')
            playing = False
        else:
            print('Please enter a valid response.')
            continue
        break

# Function to show cards


def show_few(player, dealer):
    print("\nDealer's hand:")
    print('  <FACE DOWN>')
    print('',dealer.cards[1])
    print('\nMy Hand:', *player.cards, sep='\n ')

# Shows all cards


def show_all(player, dealer):
    print("\nDealer's hand: ", *dealer.cards, sep='\n ')
    print("Dealer's hand = ", dealer.value)
    print('My hand: ', *player.cards, sep='\n ')
    print('My hand is = ', player.value)

# possible outcomes


def player_busts(player,dealer,chips):
    print(f'You BUST! The house takes your {chips.bet} chips.')
    chips.lose_bet()


def player_wins(player,dealer,chips):
    chips.win_bet()
    print(f'You WON! {chips.bet} chips has been added to your bankroll.')


def dealer_busts(player, dealer,chips):
    print(f'Dealer BUSTS! {chips.bet} chips has been added to your bankroll.')
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print(f'Ouch. The Dealer wins. You lost {chips.bet} chips.')
    chips.lose_bet()


def push(player, dealer):
    print("It's a push! The game is a draw.")


def oom(chips):
    if chips.total == 0:
        print("'Taps on my shoulder'... The guards are telling me to leave.")
        quit()
# Now onto the game!


print('Welcome to "The Proud Buffalo Soars With Dancing Dog Casino"!\nNow we will play the game Black Jack\n'
          'Here are the rules:\n1.Get as close to 21 as you can without going over.\n'
          '2.Your computer dealer must hit until it reaches 17. Then it must stay.\n'
          '3.Aces do count as 1 or 11.\n4.Do not steal our land.')

player_chips = Chips()


while True:

    take_bet(player_chips)
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    show_few(player_hand,dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)
        show_few(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif player_hand.value > dealer_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand)

    print(f'Your new total is {player_chips.total} chips.')

    oom(player_chips)
    new_game = input('Would you like to play again to feed your gambling addiction?: y/n\n')
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thank you for providing our Proud Buffalo Soars With Dancing Dog Casino enough \n'
              'money for fire water. To keep the night wolf demon away. I will now leave you so I can \n'
              'make it rain with your money...'
              'Praise the GOLDEN GOD!')
        break





































































