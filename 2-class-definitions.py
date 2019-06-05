class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for s in suits:
            for r in ranks:
                self.deck.append(Card(s,r))
    
    def __str__(self):
        deck_composition = ""
        for c in self.deck:
            deck_composition += '\n' + c.__str__()
        return "The deck has: \n" + deck_composition
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        dealt_card = self.deck.pop()
        #print("Dealt card: ", dealt_card) # for test purposes
        return dealt_card


class Hand:
    def __init__(self):
        self.hand = []
        self.value = 0
        self.aces = 0
        
    def add_card(self, card):
        self.hand.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1
        
    def adjust_aces(self):
        while self.value > 21 and self.aces: # 'and self.aces:' same as 'and self aces > 0:'
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self, total = 100):
        self.total_chips = total # This can be set toa default value or supplied by an user input
        self.bet = 0
        
    def win_bet(self):
        self.total_chips += self.bet
        
    def lose_bet(self):
        self.total_chips -= self.bet
