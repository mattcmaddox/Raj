import random
from random import randint


number_of_humans = 0
number_of_computers = 6
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

last_round_treasure = None
last_round_winner = 0

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
    for diff in range(40):
        bid = target_bid + diff
        if bid in hand:
            return bid
        bid = target_bid - diff
        if bid in hand:
            return bid
    print "ERROR 23: Bid out of range!"



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
    i = randint(1, 5)
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
    elif i == 5:
        print "bid out chosen"
        computer_ai_bid = bid_out(treasure, hand)
    return computer_ai_bid



def humans_turn(humans, players_hands, treasure):
    bids = []
    humans = range(humans)
    for human in humans:
        bid = human_input(players_hands[human], treasure)
        bids.append(bid)
    return bids

def computers_turn(computers, players_hands, treasure, humans):
    bids = []
    computers = range(computers)
    for computer in computers:
        bid = pick_random_ai(treasure, players_hands[(computer + humans)])
        bids.append(bid)
    return bids

def join_bids(human, computer):
    human.extend(computer)
    bids = human
    return bids

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
    print "No one wins this trick!  Treasure carries over to next round."
    return None

def remove_cards_from_hands(hands, bids):
    players = range(len(bids))
    for player in players:
        hands[player].remove(bids[player])
    return hands

def trick_winner_scores(winner, treasure, scores):
    print "Trick winner:", winner
    if winner == None:
        return scores
    score = scores.pop(winner)
    score += treasure
    scores.insert(winner, score)
    return scores

def game_winner_tie_checker(scores):
    number_of_winners = scores.count(max(scores))
    winners = list()
    if number_of_winners > 1:
        winners = [i for i,x in enumerate(scores) if x == max(scores)]
        print "There are %r winners for this game!" % number_of_winners
        return winners
    game_winner = scores.index(max(scores))    
    return game_winner

            

#############################################
###########    M    A    I    N   ###########
#############################################

while len(treasure_deck) > 0:
    #if last_round_winner == None:

    
    
    # draw the treasure to bid on
    treasure_drawn = draw_treasure(treasure_deck)
    print "treasure drawn %r, last rounds treasure %r" % (treasure_drawn, last_round_treasure)

    # Tally all bids for humans and computers
    humans_bids = humans_turn(number_of_humans, players_hands, treasure_drawn)
    computers_bids = computers_turn(number_of_computers, players_hands, treasure_drawn, number_of_humans)
    all_bids = join_bids(humans_bids, computers_bids)

    # Pick the winner of this trick    
    trick_winner = winning_player_finder(all_bids, treasure_drawn)
    # Clean up played cards
    players_hands = remove_cards_from_hands(players_hands, all_bids)
    # Tally up score
    scores = trick_winner_scores(trick_winner, treasure_drawn, scores)

    # If no one wins a trick, the treasure carries over
    last_round_treasure = treasure_drawn
    last_round_winner = trick_winner

#############################################
###########    T E S T I N G     ###########
#############################################

    #print "bids this trick: %r" % all_bids   
    #print "player %r is the winner " % trick_winner
    #print "treasure_drawn  = *%r*" % treasure_drawn
    print "scores so far: ", scores

game_winner = game_winner_tie_checker(scores)
print "Player(s) %r wins the game!" % game_winner
    
