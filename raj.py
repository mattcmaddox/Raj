import collections
import random
from random import randint


# Creates a set with values of 1-15
hand = set([1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12, 13, 14, 15])

# The number of players:
number_of_players = 4

# Creates all players hands
players_hands = [hand, hand, hand, hand]

# Sets players scores to zero
players_score = [0, 0, 0, 0]

# Creates a set of treasures valued -5-10 
treasure_deck = set([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5 ,6, 7, 8, 9, 10])


# Random pick of a treasure from treasure_deck and removes it from the deck
def draw_treasure(treasure_deck):
    treasure_drawn = random.sample(treasure_deck, 1)[0]
    treasure_deck.remove(treasure_drawn)
    return treasure_drawn

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
        print "\nThe treasure is: *%r*" % treasure
        print "Choose from "
        print hand
        bid = raw_input("> ")
        bid = bid_checker(bid, hand)
    return bid



# Finds the closest card in hand - Defaults to return the lower value if equal distance 
# **might not be true anymore**
def find_closest_card(hand, target_bid):
    for diff in range(15):
        bid = target_bid + diff
        if bid in hand:
            return bid
        bid = target_bid - diff
        if bid in hand:
            return bid



# Bidding Method 1 - Bid about half the value of the treasure
def bid_low(treasure, hand):
    if treasure < 2:
        treasure = 2
    bid = treasure / 2
    bid = find_closest_card(hand, bid)
    return bid

# Bidding Method 2 - Bid about twice the value of the treasure
def bid_high(treasure, hand):
    bid = treasure + treasure 
    bid = find_closest_card(hand, bid)
    return bid

# Bidding Method 3 - Random 1-15
def bid_random(hand):
    bid = randint(1, 15)
    bid = find_closest_card(hand, bid)
    return bid

# Bidding Method 4 - Bid the same as the treasure
def bid_same(treasure, hand):
    if treasure < 0:
        print "treasure drawn was a negative!"
        treasure = -treasure
    bid = find_closest_card(hand, treasure)
    return bid

# Bidding Method 5 - Bid as low as possible
def bid_out(treasure, hand):
    bid = 1
    bid = find_closest_card(hand, bid)
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



treasure_drawn = draw_treasure(treasure_deck)


player0bid = player0input(treasure_drawn, players_hands[0])
# Set up how computers will bid
player1bid = bid_same(treasure_drawn, players_hands[1])
player2bid = bid_low(treasure_drawn, players_hands[2])
player3bid = bid_random(players_hands[3])

all_bids = [player0bid, player1bid, player2bid, player3bid]

def biding_dict_builder(bids):
    bid_dict = {}
    for player in range(len(bids)):
        bid = bids[player]
        if bid in bid_dict:
            bid_dict[bid].append(player)
        else:
            bid_dict[bid] = [player]
    return bid_dict

def winning_player(bids, treasure):
    bid_dict = biding_dict_builder(bids)
    reverse = treasure > 0
    for bid in sorted(bid_dict, reverse=reverse):
        players = bid_dict[bid]
        if len(players) == 1:
            return players[0]
    return None

def remove_cards_from_hands(hands, bids):
    players = range(len(bids))
    print "bids", bids
    for player in players:
        hands[player].remove(bids[player])
        print "player", player
        print "players", players
    return players_hands


        


remove_cards_from_hands(players_hands, all_bids)
foo = winning_player(all_bids, treasure_drawn)

#############################################
###########    T E S T I N G     ###########
#############################################

print "bids this round: %r" % all_bids   
print "player %r is the winner: " % foo
print "treasure_drawn  = *%i*" % treasure_drawn
print "bids = *%r*" % player0bid, player1bid, player2bid, player3bid
print "players hands", players_hands


