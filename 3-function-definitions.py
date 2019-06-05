def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How much would you like to bet? Enter a number: "))
        
        except ValueError:
            print("Sorry, that wasn't a number, try again: ")
        
        else:
            if chips.bet > chips.total_chips:
                print("That amount exceeds your balance of {0}!".format(chips.total_chips))
            else:
                print("You have bet {0} of your {1} total.".format(chips.bet, chips.total_chips))
                
                break


def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_aces()


def hit_or_stand(deck, hand):
    global playing
    
    while True:
    
        if hand.value <= 21:
            turn = input("Do you want to Hit or Stand? Enter Hit or Stand: ")
            if turn[0].lower() == "h":
                hit(deck,hand)
                
            elif turn[0].lower() == "s":
                print("Player stands. Dealer is playing. \n")
                playing = False
            else:
                print("Answer not valid. Please, enter Hit or Stand: ")
                continue
            break


def show_some_cards(player, dealer):
    print("\nDealer hand:")
    print(" <card hidden>")
    print("",dealer.hand[1],"\n")
    print("\nPlayer's hand:", *player.hand, sep='\n')
    
def show_all_cards(player, dealer):
    print("\nDealer's hand:", *dealer.hand, sep='\n')
    print(" Dealer's hand value", dealer.value, "\n")
    print("\nPlayer's hand:", *player.hand,sep='\n')
    print(" Player's hand value:", player.value, "\n")


def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()
    
def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")
