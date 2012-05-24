from random import choice
from random import randint

# Simple range variable 1-15
random_card = randint(1, 15)

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
    print "The treasure to bid on is %i, what will you bid?" % treasure
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


# Finds the next LOWEST card till the card is in the hand
def find_next_lowest(bid, hand):
    if (bid in hand) == True:
        print "bid was in hand in 'find_next_lowest'"
    else:
        bid -= 1
        #print "'next_lowest' bid was NOT in hand, decreasing"
    return bid

# Finds the next HIGHEST card till the card is in the hand
def find_next_highest(bid, hand):
    if (bid in hand) == True:
        print "bid was in hand in 'find_next_highest'"
    else:
        bid += 1
        #print "'next_highest' bid was NOT in hand, increasing"
    return bid



# Finds the closest card in hand - Defaults to return the lower value if equal distance
def find_closest_card(bid, hand):
    i = 0
    falling_bid = bid 
    raising_bid = bid 
    while (bid in hand) == False:
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
            print "final bid = %i " % bid
            print "falling_bid = %i " % falling_bid
            print "raising_bid = %i " % raising_bid
            return bid
        else:
            print "Trying again from top of scope"
    return bid


#dumb_card = randint(-15, 30)
#dumb_card = 5
#tester = find_closest_card(dumb_card, players_hands[1])
#tester = find_closest_card(dumb_card, [1, 9])
#print tester






# Bidding Method 1 - Bid about half the value of the treasure
def bid_low(treasure, hand):
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
    random_card = randint(1, 15)
    bid = find_closest_card(random_card, hand)
    return bid

# Bidding Method 4 - Bid the same as the treasure
def bid_same(treasure, hand):
    if treasure < 0:
        treasure = -treasure
        
    bid = find_closest_card(treasure, hand)
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

# Set up how computers will bid
player1bid = pick_random_ai(treasure_drawn, players_hands[1])
player2bid = bid_same(treasure_drawn, players_hands[2])
player3bid = bid_random(players_hands[3])


player0bid = player0input(treasure_drawn)
print player0bid
#############################################
########### C O M M E N T   O U T ###########
#############################################

#print "treasure_drawn  =  %i" % treasure_drawn
#print "computer's bids = ", player1bid, player2bid, player3bid
print "user's bid      =  %i" % player0bid






