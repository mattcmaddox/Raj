import collections
import random
from random import randint


# Creates a set with values of 1-15
hand = ([1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12, 13, 14, 15])

# The number of players:
number_of_players = 4

# a list of the number of players
players_list = number_of_players

# Creates all players hands
players_hands = {0: hand, 1: hand, 2: hand, 3: hand}

# Creates a set of treasures valued -5-10 
treasure_deck = ([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5 ,6, 7, 8, 9, 10])

# Random pick of a treasure from treasure_deck
treasure_drawn = random.sample(treasure_deck, 1)[0]


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
        print "treasure drawn was a negative!"
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

def all_bids_bulider(bids, players):
    bid_dict = {}
    for player in range(players):
        bid = bids[player]
        print bid
        if bid in bid_dict:
            bid_dict[bid].append(player)
        else:
            print "else!"
            bid_dict[bid] = [player]
    print bid_dict
    return bid_dict



def tie_checker(treasure, bids):
    instances = collections.Counter(bids.keys())
    print "instances %r " % instances 
    instances = max(instances.values())  # highest occurances of a bid
    print "instances %r " % instances 
    if instances > 1: 
        print "running tie breaker"
        winning_bid = tie_breaker(treasure, bids)
    else:
        print "no ties"
        winning_bid = winner_picker(treasure, bids)
    return winning_bid

def tie_breaker(treasure, bids):
    previous_bid = None
    for bid in sorted(bids, reverse=True):
        print "bid %r " % bid
        print " previous bid %r " % previous_bid
        if previous_bid == bid:
            print "duplicate!"
            print "previous bid %r " % previous_bid
            print "bid %r " % bid
            print bids
        previous_bid = bid

    winning_bid = winner_picker(treasure, bids)
    return winning_bid 



def winner_picker(treasure, bids):
    if treasure < 0:
        winning_bid = negative_treasure(bids)
    elif treasure > 0:
        winning_bid = positive_treasure(bids)
    return winning_bid

def negative_treasure(bids):
    winning_bid = min(bids.values())
    return winning_bid


def positive_treasure(bids):
    winning_bid = max(bids.values())
    return winning_bid

print "bids this round: %r" % all_bids   
bid_dict = all_bids_bulider(all_bids, number_of_players)
foo = tie_checker(treasure_drawn, bid_dict)
print "winning bid: %r" % foo

#############################################
###########    T E S T I N G     ###########
#############################################

print "treasure_drawn  = *%i*" % treasure_drawn
print "computer's bids = ", player1bid, player2bid, player3bid
print "user's bid      =  %i" % player0bid






