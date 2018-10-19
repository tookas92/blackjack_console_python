"""
Simple Text Blackjack Game written by using OOP
"""
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card():
    """
    object that defines single card attributes
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        #print(f"{self.suit} {self.rank} Created!")

    def __str__(self):
        return self.rank+' OF '+self.suit

class Deck():
    """
    Instance creates full deck of 52 cards
    """
    def __init__(self):
        self.card_list= []
        for suit in suits:
            for rank in ranks:
                self.card = Card(suit, rank)
                self.card_list.append(self.card)

                

    def __str__(self):
        deck_comp = ''
        for card in self.card_list:
            deck_comp += card.__str__() + "\n"
        return deck_comp

    def shuffle(self):
        return random.shuffle(self.card_list)

    def deal(self):
        self.dealtCard = self.card_list[0]
        self.card_list.pop(0)
        return self.dealtCard

class Hand():
    """
    Instance that defines card types and values that player currently have
    """
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0


    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
        return self.cards

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips():
    """
    Managing chips
    """
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    """
    Function that takes bet amount for game
    """
    while True:
        try:
            chips.bet = int(input("Please write bet amount:"))
            if chips.bet <= chips.total:
                break
            else:
                print("Sorry not enough chips.")
        except:
            print("You need to write a number!!. Write bet:")
            continue
    return chips.bet

def hit(deck, hand):
    """
    Function that takes card from deck and checks for ace value
    """
    deck.deal()
    hand.add_card(deck.dealtCard)
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    """
    Function that asks to hit or stand in the game
    """
    global playing
    hit_or_stand =''
    while not hit_or_stand == 'hit' or 'stand':
        hit_or_stand = input("Do you want to hit or stand?:")
        if hit_or_stand.lower() == "hit":
            hit(deck, hand)
            break
        elif hit_or_stand.lower() == "stand":
            playing = False
            print("Player chosen stand.")
            break


def show_some(player, dealer):
    """
    Showing cards in player hands and hiding first of
    dealers card
    """
    print("Current Hand status: \n")
    print("Player cards: \n")
    for card in player.cards:
        print(card.rank+' of '+card.suit)
    print("Cards value: {}".format(player.value)) 
    print("Dealer cards: \n")
    for card in dealer.cards:
        if card == dealer.cards[0]:
            print("Hidden card")
        else:
            print(card.rank+' of '+card.suit)

def show_all(player, dealer):
    """
    Shows all the cards on hands
    """
    print("Current Hand status: \n")
    print("Player cards: \n")
    for card in player.cards:
        print(card.rank+' of '+card.suit)
    print("Cards value: {}".format(player.value)) 
    print("Dealer cards: \n")
    for card in dealer.cards:
        print(card.rank+' of '+card.suit)
    print("Cards value: {}".format(dealer.value)) 

def player_busts(chips):
    """
    takes bet from total amount as busted
    """
    print("Player busts!")
    chips.lose_bet()

def player_win(chips):
    print("Player win!")
    chips.win_bet()

def dealer_busts(chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_win(chips):
    print("Dealer win!")
    chips.lose_bet()

def push():
    print("It is a Tie.")
PlayerChips = Chips()
while True:
    deck = Deck()
    player = Hand()
    dealer = Hand()
    deck.shuffle()
    for i in range(0,2):
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())
    print("Cards distributed \n")
    show_some(player, dealer)
    print("\n")
    print("Your chips {} \n".format(PlayerChips.total))
    take_bet(PlayerChips)
    while playing == True:
        hit_or_stand(deck, player)
        show_some(player, dealer)
        if player.value > 21:
            show_all(player, dealer)
            player_busts(PlayerChips)
            playing = False
        elif player.value == 21:
            playing = False

    while dealer.value <= 17 and player.value <=21:
        hit(deck, dealer)
    
    if dealer.value > player.value and dealer.value <= 21:
        show_all(player, dealer)
        dealer_win(PlayerChips)

    elif dealer.value > 21:
        show_all(player, dealer)
        dealer_busts(PlayerChips)
        
    elif dealer.value == player.value:
        show_all(player,dealer)
        push()
    elif player.value > dealer.value:
        show_all(player, dealer)
        player_win(PlayerChips)
    if PlayerChips.total == 0:
        print("You lost all chips")
        break
    reply=''
    while not reply == 'yes' or reply == 'no':
        reply = input("Distribute again?:")
        if reply == 'yes':   
            playing = True
        elif reply == 'no':
            print("Thanks for playing your balance is {}".format(PlayerChips.total))
            break



# reply nie działa
# scenariusze wygranych sprawdzic













