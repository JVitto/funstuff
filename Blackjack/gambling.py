#first runthrough
import random

card_deck = [('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10), ('J', 10), ('Q', 10), ('K', 10), ('A', 11)] * 4
random.shuffle(card_deck)

def deal(card_deck):
    return card_deck.pop()

def value_conf(hand):
    value = 0
    ace = 0
    for card, card_val in hand:
        if card == 'A':
            ace += 1
        value += card_val

    while value > 21 and ace:
        value -= 10
        ace -= 1

    return value

def display(hand, player):
    disp = " ".join([f'[{card}]' for card, val in hand])
    print(f"{player}'s hand: {disp}")

def play():
    player_hand = [deal(card_deck), deal(card_deck)]
    dealer_hand = [deal(card_deck), deal(card_deck)]
    
    while True:
        display(player_hand, "Player")
        player_value = value_conf(player_hand)
        print(f"Player's hand value: {player_value}")
        
        if player_value > 21:
            print("Player's hand is busted. Dealer wins.")
            return
        
        choice = input("[H]it or [S]tand: ").lower()

        if choice == "h":
            player_hand.append(deal(card_deck))
        elif choice == "s":
            break

    while value_conf(dealer_hand) < 17:
        dealer_hand.append(deal(card_deck))

    display(dealer_hand, "Dealer")
    dealer_value = value_conf(dealer_hand)
    print(f"Dealer's hand value: {dealer_value}")

    if dealer_value > 21:
        print("Dealer's hand is busted. Player wins!")
    elif dealer_value >= player_value:
        print("Dealer wins")
    else:
        print("Player wins")

play()
#gambling!!!!