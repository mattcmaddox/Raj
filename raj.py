from random import choice
from random import randint

# Simple range variable 1-15
#random_card = randint(1, 15)

# Creates a list with values of 1-15
hand = list(range(1, 16))

# Creates all players hands
players_hands = [list(hand), list(hand), list(hand), list(hand)]

# Creates a list of treasures valued -5-10 
treasure_deck = list(range(-5, 11))

# Removes zero-valued treasure from list
treasure_deck.remove(0)

# Random pick of a treasure from treasure_deck
treasure_drawn = choice(treasure_deck)

# Remove chosen treasure from treasure_deck
treasure_deck = treasure_deck.remove(treasure_drawn)

# Checks and makes sure that the guess is NOT a string or a word
def bid_checker(bid, hand):
    try: 
        bid = int(bid)
    except:
        print "Words are not numbers"
    return bid 

# Human input
def player0input(treasure, hand):
    bid = 0
    while bid not in hand:
        print "\nThe treasure is: *%i*" % treasure
        print "Choose from "
        print hand
        bid = raw_input("> ")
        bid = bid_checker(bid, hand)
    return bid





# Finds the closest card in hand - Defaults to return the lower value if equal distance 
# **might not be true anymore**
def find_closest_card(bid, hand):
    i = 0
    falling_bid = bid 
    raising_bid = bid 
    while (falling_bid and raising_bid) not in hand:
        i += 1
        print "%i times through the loop" % i
        print falling_bid
        print raising_bid
        if i > 19:
            break
        falling_bid -= 1
        raising_bid += 1
    if falling_bid in hand:
        bid = falling_bid
    elif raising_bid in hand:
        bid = raising_bid
    return bid






# Bidding Method 1 - Bid about half the value of the treasure
def bid_low(treasure, hand):
    if treasure < 2:
        treasure = 2
    bid = treasure / 2
    bid = find_closest_card(bid, hand)
    return bid

# Bidding Method 2 - Bid about twice the value of the treasure
def bid_high(treasure, hand):
    bid = treasure + treasure 
    bid = find_closest_card(bid, hand)
    return bid

# Bidding Method 3 - Random 1-15
def bid_random(hand):
    bid = randint(1, 15)
    bid = find_closest_card(bid, hand)
    return bid

# Bidding Method 4 - Bid the same as the treasure
def bid_same(treasure, hand):
    if treasure < 0:
        treasure = -treasure
    bid = find_closest_card(treasure, hand)
    return bid

# Bidding Method 5 - Bid as low as possible
def bid_out(treasure, hand):
    bid = 1
    bid = find_closest_card(bid, hand)
    return bid


# Computer picks a random AI for bidding 
def pick_random_ai(treasure, hand):
    i = randint(1, 4)
    if i == 1:
        print "bid low chosen"
        computer_ai_bid = bid_low(treasure, hand)
    elif i == 2:
        print "bid high chosen"
        computer_ai_bid = bid_high(treasure, hand)
    elif i == 3:
        print "bid random chosen"
        computer_ai_bid = bid_random(hand)
    elif i == 4:
        print "bid same chosen"
        computer_ai_bid = bid_same(treasure, hand)
    return computer_ai_bid




#############################################
###########    M    A    I    N   ###########
#############################################



player0bid = player0input(treasure_drawn, players_hands[0])
# Set up how computers will bid
player1bid = bid_same(treasure_drawn, players_hands[1])
player2bid = bid_low(treasure_drawn, players_hands[2])
player3bid = bid_random(players_hands[3])

all_bids = [player0bid, player1bid, player2bid, player3bid]

#def highest_wins(treasure, bids):


def tie_checker(treasure, bids):
    winning_bid = None
    for bid in bids:
        print bid
        print bids
        tie = bids.count(bid)
        print "ties??", tie
        if tie > 1:
            print "there's a tie!"
            winning_bid = tie_breaker(treasure, bids)
    winning_bid = max(bids[0], bids[1], bids[2], bids[3])
    return winning_bid


def tie_breaker(treasure, bids):
    print bids


#def negitive_treasure(treasure, bids):

#def positive_treasure(treasure, bids):
    
foo = tie_checker(treasure_drawn, all_bids)
print foo

#############################################
########### C O M M E N T   O U T ###########
#############################################

print "treasure_drawn  = *%i*" % treasure_drawn
print "computer's bids = ", player1bid, player2bid, player3bid
print "user's bid      =  %i" % player0bid






