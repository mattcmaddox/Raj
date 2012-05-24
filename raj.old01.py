from random import choice
from random import randint

# Creates a list with values of 1-15
hand = list(range(1, 16))

# Creates all players hands
players_hands = [list(hand), list(hand), list(hand), list(hand)]

# Creates a list of treasures valued -5-10 
treasure_deck = list(range(-5, 16))

# Removes zero-valued treasure from list
treasure_deck.remove(0)

# Random pick of a treasure from treasure_deck
treasure_drawn = choice(treasure_deck)

# Remove chosen treasure from treasure_deck
treasure_deck = treasure_deck.remove(treasure_drawn)


#print players_hands
#print treasure_drawn

#turn(player_bids, computer_bids, computer_bids, computer_bids)

def int_checker(i, hand):
    a = raw_input(">>>")
    try:
        int(a)
        return a
    except:
        print "r% is not a card in your hand." % a

# player0 inputs his/her bid
def player_bids(hand):
    print "The current treasure is %r.  What will you bid?" % treasure_drawn
    bid = raw_input("> ")
    int_checker(bid, players_hands[0])
    bid = int(bid)

# Checks if player can make the bid
def player_bid_check(hand):
    if bid in hand:
        hand.remove(bid)
        print hand
    else: 
        print "something else"        
    return hand


print "testing..."
print players_hands[0]
player_bids(players_hands[0])
#player_bid_check(players_hands[0])

# A rough idea of getting the computer to bid in different ways
#def computer_how_to_bid(treasure, hand):
#    fickle = randint(1, 4)
#    if fickle == 1:
#        computer_bid = treasure * 2 
#    elif fickle == 2:
#        computer_bid = treasure / 2
#    elif fickle == 3:
#        computer_bid = treasure 
#    elif fickle == 4:
#        computer_bid = randint(1, 15)
#    return computer_bid


# Check if bid is valid
#def check_if_bid_is_valid(bid, hand):
#    if bid in hand:


# The Computer's Turn:
#def computers_turn():
#    computer_bid = computer_how_to_bid(treasure_drawn, players_hands)
#    check_if_bid_is_valid(computer_bid, players_hands)

#print "computer's bid %d" % computer_bid



# def player0Turn():
#print "The treasure to bid on is %d, what will you bid?" % treasure_drawn
#print "Cards remaining in your hand:"
#print players_hands[0]
#player0Bid = raw_input("> ")

#if player0Bid 

# checks playerbid against playerhand to see if it's a valid bid
#def player1check():
    #if player1bid.__contains__ !=


