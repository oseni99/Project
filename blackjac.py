
import random
# global variables
suit = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
rank = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
myvalues = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,"Jack": 10, "Queen": 10, "King": 10, "Ace": 11}



class Card():
    def __init__(self,suit,rank):
        self.suit = suit 
        self.rank = rank 
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
the_card = Card("Two","Hearts")
print(the_card)

#deck class 
class Deck():
    def __init__(self):
        self.all = []
        for suits in suit:
            for ranks in rank:
                self.all.append(Card(suits,ranks))

    def shuffle_deck(self):
        return random.shuffle(self.all)
    
    def deal_one(self):
        single_card = self.all.pop()
        return single_card
    
    def __str__(self):
        deckofcard = ""
        for card in self.all:
            deckofcard+= "\n"+card.__str__()
        return "The cards has : "+deckofcard

the_deck = Deck()
print(the_deck)
the_deck.shuffle_deck()
print(the_deck)

class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_cards(self,card):
        #from the deck deal_one 
        self.cards.append(card)
        self.value += myvalues[card.rank]

        #tracking the aces 
        if card.rank == "Ace":
            self.aces += 1 
    def adjust_ace(self):
        # if total value > 21 and i still have an ace 
        # change my ace to be a 1 instead of an 11 
        # most times 0 == truthy and other nubers are falsy so i can say self.aces alone below 
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

#player testing 
test_player = Hand()
#add card from deck to player hand 
pulled_card = the_deck.deal_one()
#show the pulled card 
print(pulled_card)
#add it 
test_player.add_cards(pulled_card)
print(test_player.value)


class Chips:
    def __init__(self):
        #can be set up in the instance level automatically by changing it defaultly to (self,total=100)
        self.total = 100
        self.bet = 0 
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet 

