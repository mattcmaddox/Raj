#! /usr/bin/python
import sys
import random
import argparse
from random import randint


# Builds Command Line Argument Parser
def build_parser():
    parser = argparse.ArgumentParser(description='Command Line Implementation of Raj')#add_help=False)
    #parser.add_argument('-h', '--humans', type=int, default=1, help='Number of Human Players')
    #parser.add_argument('-c', '--computers', type=int, default=5, help='Number of Computer Players')
    parser.add_argument('-d', '--debug', action='store_true', help='Debug Mode:  Displays messy debugging information.')
    parser.add_argument('-s', '--stats', action='store_true', help='Stats Mode:  Displays stats about efficiency.')
    parser.add_argument('-e', '--easy', action='store_true', help='Easy Mode:  Keeps track of other players remaining points and remaining treasures.')
    parser.add_argument('humans', type=int, nargs='?', default=1, help='Positionial Argument for Number of Humans')
    parser.add_argument('computers', type=int, nargs='?', default=5, help='Positionial Argument for Number of Computers')
    
    #parser.add_argument('--help', action='store_true')
    args = vars(parser.parse_args())
    return args


# Sets players scores to zero
def create_scores(players):
    scores = []
    for player in players:
        scores.append(0)
    return scores

# Creates a hand (set) for every player)
def create_hands(players):
    hands = []
    for player in players:
        hands.append(set(range(1, 16)))
    return hands

def remove_cards_from_hands(hands, bids):
    players = range(len(bids))
    for player in players:
        hands[player].remove(bids[player])
    return hands

# Random pick of a treasure from treasure_deck and removes it from the deck
def draw_treasure(treasure_deck, last_round_winner, last_round_treasure):
    treasure_drawn = random.sample(treasure_deck, 1)[0]
    treasure_deck.remove(treasure_drawn)
    if last_round_winner is None:
        combined_treasure = treasure_drawn + last_round_treasure
        return combined_treasure
    return treasure_drawn

def join_bids(human, computer):
    human.extend(computer)
    bids = human
    return bids

def bidding_dict_builder(bids):
    bid_dict = {}
    for player in range(len(bids)):
        bid = bids[player]
        if bid in bid_dict:
            bid_dict[bid].append(player)
        else:
            bid_dict[bid] = [player]
    return bid_dict


## Stats
# Finds the value of the treasure based on number of players in game
def relative_treasure_value_determiner(total_players, treasure_drawn):
    relative_treasure_value = round(0.0666666 * (35 - (40 / float(total_players))) * treasure_drawn, 2)
    return relative_treasure_value

def determine_trick_efficiency(bids, treasure):
    trick_efficiency = []
    for i in bids:
        trick_efficiency.append(treasure - i)
    return trick_efficiency

def empty_stat_builder(list_of_players):
    empty = []
    for i in list_of_players:
        empty.append(0)
    return empty

def remaining_bids_finder(players_hands):
    bids = []
    for i in players_hands:
        bids.append(sum(i))
    return bids

def list_zipper(total_efficiency, trick_efficiency):
    current = [sum(i) for i in zip(total_efficiency, trick_efficiency)]
    return current

def winner_stat_tracker(winner, total_stat, trick_stat):
    if winner == None:
        pass
    elif winner == len(total_stat):
        total_stat.append(total_stat.pop(winner) + trick_stat[winner])
    else:
        total_stat.insert(winner, (total_stat.pop(winner) + trick_stat[winner]))
    return total_stat


## Who won?
def winning_player_finder(bids, treasure):
    bid_dict = bidding_dict_builder(bids)
    reverse = treasure >= 0
    for bid in sorted(bid_dict, reverse=reverse):
        players = bid_dict[bid]
        # For single player games
        if len(players) == 1:
            return players[0]
    print "\n No one wins this trick!  Treasure carries over to next round.", "\n"
    return None

def trick_winner_scores(winner, treasure, scores):
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
        print "\n There are %r winners for this game!" % number_of_winners
        return winners
    game_winner = scores.index(max(scores))    
    return game_winner


# Finds the closest card in hand - Defaults to return the HIGHER value if equal distance 
def find_closest_card(hand, target_bid):
    for i in range(40):
        bid = target_bid + i
        if bid in hand:
            return bid
        bid = target_bid - i
        if bid in hand:
            return bid
    print "ERROR 23: Bid out of range!"


## Human
def humans_turn(humans, players_hands, treasure, treasure_deck, all_bids):
    bids = []
    humans = range(humans)
    for human in humans:
        bid = human_input(players_hands[human], treasure, treasure_deck, human)
        bids.append(bid)
    return bids

def human_input(hand, treasure, treasure_deck, human):
    bid = 0
    while bid not in hand:
        print "                  Turn: Player %r" % human
        print "       The treasure is: *%r*" % treasure
        print " Choose from your hand:", sorted(hand)
        print " Treasures   remaining:", sorted(treasure_deck)
        bid = raw_input("\n             Your bid : >")
        try:
            bid = int(bid)
        except:
            print "\n Words are not numbers!"
        if bid not in hand:
            print "\n Try again!"
    return bid

## Computer
def build_computer_bidding_methods_list(number_of_computers):
    computer_bidding_methods = []
    size = range(number_of_computers)
    for i in size:
        computer_bidding_methods.append(bid_smart)
    return computer_bidding_methods

def computer_turn(computer_bidding_methods, players_hands, treasure, humans):
    bids = []
    for i in computer_bidding_methods:
        bid = i(treasure, players_hands[humans])
        humans += 1
        bids.append(bid)
    return bids

def computer_players_hands(players_hands, humans):
    # remove humans hands from the list
    if humans > 0:
        hum = range(humans)
        for i in hum:
            del players_hands[i]
    return players_hands


# Bidding Method 1 - Bid Smart
def bid_smart(treasure, hand):
    if treasure <= 0:
        bid = low_treasure(hand)
    elif treasure in range(1, 6): 
        bid = medium_treasure(hand)
    elif treasure > 5:
        bid = high_treasure(hand)
    return bid

def low_treasure(hand):
    bid = bid_chance()
    if bid in hand:
        return bid
    bid = bid_high()
    if bid in hand:
        return bid
    bid = bid_low()
    if bid in hand:
        return bid
    bid = find_closest_card(hand, bid_chance())
    return bid

def medium_treasure(hand):
    bid = bid_chance()
    if bid in hand:
        return bid
    bid = bid_high()
    if bid in hand:
        return bid
    bid = bid_low()
    if bid in hand:
        return bid
    bid = find_closest_card(hand, bid_chance())
    return bid 

def high_treasure(hand):
    bid = bid_high()
    if bid in hand:
        return bid
    bid = bid_low()
    if bid in hand:
        return bid
    bid = bid_chance()
    if bid in hand:
        return bid
    bid = find_closest_card(hand, bid_high())
    return bid 

def bid_low():
    bid = randint(1, 5)
    return bid
def bid_chance():
    bid = randint(6, 10)
    return bid
def bid_high():
    bid = randint(11, 15)
    return bid

# Bidding Method #2 - AI
def bid_ai(treasure, hand):
    if treasure > 5:
        bid = ai_high()
    elif treasure in range(1-6):
        bid = ai_medium()
    elif treasure <= 0:
        bid = ai_low()
    return bid

def ai_high():
    pass
    

def count_hands(players_hands, number_of_computers):
    print "players_hands >", players_hands
        #their_hands = del players_hands [i]
        #print "their_hands", their_hands


#############################################
###########    M    A    I    N   ###########
#############################################
def main():
    """Raj, a bidding game of perfect information
    $raj.py [humans] [computers]
    """
    games_won = 0
    trick_number = 0
    args = build_parser()
    number_of_humans = args.get('humans')
    number_of_computers = args.get('computers')
    total_players = number_of_humans + number_of_computers
    list_of_players = range(total_players)
    players_hands = create_hands(list_of_players)

    scores = create_scores(list_of_players)
    treasure_deck = set(x for x in range(-5, 11)if x !=0)
    last_round_treasure = None
    last_round_winner = 0
    all_bids = []
    total_efficiency = empty_stat_builder(list_of_players)
    winner_efficiency = empty_stat_builder(list_of_players)
    trick_winner_tally = empty_stat_builder(list_of_players)
    # How the computer plays
    computer_bidding_methods = build_computer_bidding_methods_list(number_of_computers)


    ## Debug!
    if args.get('debug') == True:
        print "args!", args
        print "number_of_humans", number_of_humans
        print "number_of_computers", number_of_computers

    
    ## Trick Loop
    while len(treasure_deck) > 0:
        trick_number += 1
        print "\n                 Trick: #%d" % trick_number
        # Draw the treasure to bid on
        treasure_drawn = draw_treasure(treasure_deck, last_round_winner, last_round_treasure)

        print count_hands(players_hands, number_of_computers)
        ## Easy Mode
        if args.get('easy') == True:
            total_bids_remaining = remaining_bids_finder(players_hands)
            print "              Bid points remaining: ", total_bids_remaining
            treasure_points_remaining = sum(x for x in treasure_deck if x > 0)
            print "Positive treasure points remaining: ", treasure_points_remaining
            negative_points_remaining = sum(x for x in treasure_deck if x < 0)
            print "Negative treasure points remaining: ", negative_points_remaining
            relative_treasure_value = relative_treasure_value_determiner(total_players, treasure_drawn)
            print "           Relative treasure value: ", relative_treasure_value


        # Human's turn(s)
        humans_bids = humans_turn(number_of_humans, players_hands, treasure_drawn, treasure_deck, all_bids)
        # Computer's turn(s)
        computers_bids = computer_turn(computer_bidding_methods, players_hands, treasure_drawn, number_of_humans)
        # Tally all bids for humans and computers
        all_bids = join_bids(humans_bids, computers_bids)
        # Find the winner of this trick    
        trick_winner = winning_player_finder(all_bids, treasure_drawn)


        ## Stats
        # Find efficiency of all bids per trick
        trick_efficiency = determine_trick_efficiency(all_bids, treasure_drawn)
        if args.get('stats') == True:
            print "trick efficiency", trick_efficiency
            # How efficient is the player who won the trick?
            winner_efficiency = winner_stat_tracker(trick_winner, winner_efficiency, trick_efficiency)
            print "winner_efficiency", winner_efficiency


        # Clean up played cards
        players_hands = remove_cards_from_hands(players_hands, all_bids)
        # Tally up score
        scores = trick_winner_scores(trick_winner, treasure_drawn, scores)
        
        # If no one wins a trick, the treasure carries over
        last_round_treasure = treasure_drawn
        last_round_winner = trick_winner
        
        print "      Treasure: *%r*" % treasure_drawn
        print "  Trick winner: <%r>" % trick_winner
        print "  Cards played: %r" % all_bids
        print " Scores so far: %r\n" % scores


    # Game is Finished!
    game_winner = game_winner_tie_checker(scores)
    print "\n Player(s)      <%r>     wins the game!" % game_winner
    print "  Final Scores: %r\n" % scores
    games_won += 1

if __name__ == '__main__':
    main()

