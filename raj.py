import random
from random import randint


number_of_humans = 1
number_of_computers = 3
total_players = number_of_humans + number_of_computers
list_of_players = range(total_players)


# Creates a hand (set) for every player)
def create_hands(players):
    hands = []
    for player in players:
        hands.append(set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    return hands

players_hands = create_hands(list_of_players)


# Sets players scores to zero
def create_scores(players):
    scores = []
    for player in players:
        scores.append(0)
    return scores

scores = create_scores(list_of_players)

# Creates a set of treasures valued -5-10 
treasure_deck = set([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5 ,6, 7, 8, 9, 10])


#^^^^^^^^  happens only at the beginning of game  ^^^^^^^^^^^#
#||||||||                                         |||||||||||



# Random pick of a treasure from treasure_deck and removes it from the deck
def draw_treasure(treasure_deck):
    treasure_drawn = random.sample(treasure_deck, 1)[0]
    treasure_deck.remove(treasure_drawn)
    return treasure_drawn


# Human input
def human_input(hand, treasure):
    bid = 0
    while bid not in hand:
        print "\nThe treasure is: *%r*" % treasure
        print "Choose from ", hand
        bid = raw_input("> ")
        try:
            bid = int(bid)
        except:
            print "Words are not numbers!"
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


def table_builder(humans, computers):



#############################################
###########    M    A    I    N   ###########
#############################################

#def a_players_turn(hands, treasure, seat):
#    human_input(players_hands[seat])

table_builder(number_of_humans, number_of_computers)

# draw the treasure to bid on
treasure_drawn = draw_treasure(treasure_deck)


player0bid = human_input(players_hands[0], treasure_drawn)
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

def winning_player_finder(bids, treasure):
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
    return hands

def round_winner_scores(winner, treasure, scores):
    score = scores.pop(winner)
    score += treasure
    scores.insert(winner, score)
    return scores
    



round_winner = winning_player_finder(all_bids, treasure_drawn)
players_hands = remove_cards_from_hands(players_hands, all_bids)
scores = round_winner_scores(round_winner, treasure_drawn, scores)

#############################################
###########    T E S T I N G     ###########
#############################################

print "bids this round: %r" % all_bids   
print "player %r is the winner: " % round_winner
print "treasure_drawn  = *%r*" % treasure_drawn
print "bids = *%r*" % player0bid, player1bid, player2bid, player3bid
print "players hands", players_hands
print scores
