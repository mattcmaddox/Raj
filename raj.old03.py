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

# Finds the next LOWEST card till the card is in the hand
def find_next_lowest(bid, hand):
    if (bid in hand) == True:
        print "bid was in hand in 'find_next_lowest'"
        return bid
    else:
        bid -= 1
        print "'next_lowest' bid was NOT in hand, decreasing"
        return bid

# Finds the next HIGHEST card till the card is in the hand
def find_next_highest(bid, hand):
    if (bid in hand) == True:
        print "bid was in hand in 'find_next_highest'"
        return bid
    else:
        bid += 1
        print "'next_highest' bid was NOT in hand, increasing"
        return bid



# Finds the closest card in hand - Defaults to return the lower value if equal distance
def find_closest_card(bid, hand):
    print "before loop"
    i = 0
    falling_bid = bid 
    raising_bid = bid 
    while (bid in hand) == False:
        print "in loop"
        i += 1
        print "%i times through the loop" % i

        falling_bid = find_next_lowest(falling_bid, hand)
        raising_bid = find_next_highest(raising_bid, hand)
        print "first bid = %i " % bid
        
        if ((falling_bid in hand) == True) or ((raising_bid in hand) == True):
            if ((falling_bid in hand)  == True):
                print "it was a FALLING bid!!"
                bid = falling_bid
            else:
                print "it was a RAISING bid!!"
                bid = raising_bid
            print "it worked!"
            print "final bid = %i " % bid
            print "falling_bid = %i " % falling_bid
            print " raising_bid = %i " % raising_bid
            return bid
        else:
            print "the 'else' part of the loop"
    return bid


dumb_card = randint(-15, 30)
#dumb_card = 5
tester = find_closest_card(dumb_card, players_hands[1])
#tester = find_closest_card(dumb_card, [1, 9])
print tester






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


#test = find_closest_card_finder(dumb_card, players_hands[1])
#print test


