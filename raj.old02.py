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

# Takes the player's guess
def player0input(treasure):
    print "The treasure to bid on is %d, what will you bid?" % treasure
    bid = bid_checker(players_hands[0])
    print bid

# Checks and makes sure that the guess is a valid one
def bid_checker(hand):
    while True:
        try:
            bid = raw_input("> ")
            bid = int(bid)
            print "You entered a card that is not in your hand"
        except:
            print "Please bid on a card from your hand"
        if bid in hand:
            return bid
            break


# Computer picks a random AI for bidding 
def pick_random_AI():
    i = randint(1, 4)
    return i

#### run seperate  bid_higher/lower += 1's then compare and chose the shortest <


def find_next_highest(bid, hand):
    if (bid in hand) == True:
        print "bid was in hand in 'find_next_highest'"
    else:
        bid += 1
        return bid


def find_next_lowest(bid, hand):
    if (bid in hand) == True:
        print "bid was in hand in 'find_next_lowest'"
    else:
        bid += 1
        return bid



# Pick the closest card to the one the AI wants
def find_closest_card(bid, hand): pass
    print "Finding Closest Card"
    i = 0
    bid_higher = bid 
    bid_lower = bid
    print "About to enter While loop; i is %d " %i
    while ((bid_higher in hand) == False) and ((bid_lower in hand) == False):
        print "In While loop %dst times" %i
        i += 1
        if (bid_higher in hand) == False:
            print "a"
            bid_higher += 1
            print bid_higher
            bid_lower -= 1
        elif (bid_lower in hand) == False:
            print "b"
            bid_higher += 1
            bid_lower -= 1
        elif (bid_higher in hand) == True:
            print "c"
            return bid_higher
        elif (bid_lower in hand) == True:
            print "d"
            return bid_lower
    print "Finished WhileLoop"    
    print bid
    print bid_higher
    print bid_lower
    print hand



# Bidding Method 1 - Bid about twice the value of the treasure
def bid_high(hand):
    print hand

# Bidding Method 4 - Bid the same as the treasure
#def bid_same(hand, treasure):
    #try treasure in hand:
    #    return treasure
    #else:
    #    find_closest_card(hand)

#player0bid = player0input(treasure_drawn)
#bid_same(players_hands[1], treasure)
dumb_card = randint(1, 20)
test = find_closest_card(dumb_card, players_hands[1])
print test


