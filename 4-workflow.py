while True:
    # Opening statement
    print("Welcome to Blackjack game! Get as close to 21 as you can without\
 going over!\n\
Dealer hits until reaching 17. Aces count as 1 or 11.")
    
    # Create, shuffle and deal 2 cards to each player
    deck = Deck()
    
    deck.shuffle()
    
    player_hand = Hand()
    dealer_hand = Hand()
    
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    # Set up player's chips
    player_chips = Chips()
    
    # Prompt player for bet
    take_bet(player_chips)
    
    # Show some cards
    show_some_cards(player_hand, dealer_hand)
    
    while playing:
        
        # Hit or Stand
        hit_or_stand(deck,player_hand)
        
        # Show some cards
        show_some_cards(player_hand,dealer_hand)
        
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
        
    # Plays dealer's hand
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

        # Show all cards
        show_all_cards(player_hand,dealer_hand)

        # Different winning scenearios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
            
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
            
        elif player_hand.value > dealer_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
            
        else:
            push(player_hand.value,dealer_hand.value)

    # Inform of player's chips
    print("\nPlayer's winnings stand at,", player_chips.total_chips,".")
    
    # Ask to play again
    new_game = input("Would you like to play again? Enter Yes or No: \n")
    if new_game[0].lower() == "y":
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break
