import random
import copy
from card import Card

"""Reference dictionary to represent Euchre deck (all four suits 9 through Ace)"""
cards = {0: [9, 10, 11, 12, 13, 14], 1: [9, 10, 11, 12, 13, 14],
         2: [9, 10, 11, 12, 13, 14], 3: [9, 10, 11, 12, 13, 14]}


def get_card():
    """Returns a tuple with (suit,value)"""
    _card = (random.randint(0, 3), random.randint(9, 14))
    return _card


def deal():
    """ Returns dictionary with 4 hands of 5 cards apiece """
    ref_deck = copy.deepcopy(cards)
    player_hands = []
    for player in range(0, 4):
        player_hand = []
        for x in range(0, 5):
            need_card = True
            while need_card:
                card = get_card()
                if card[1] in ref_deck.get(card[0]):
                    player_hand.append(Card(card[0], card[1]))
                    need_card = False
                    ref_deck.get(card[0]).remove(card[1])
        player_hands.append(player_hand)
    blind = []
    for a in ref_deck.keys():
        for b in ref_deck.get(a):
            blind.append(Card(a, b))
    player_hands.append(blind)
    return player_hands

    '''for x in player_hands:
        for y in x:
            y.print_card()
        print "Player"
    print "Remaining cards :" + str(ref_deck.values())
    print "Deck : " + str(cards.values())'''
