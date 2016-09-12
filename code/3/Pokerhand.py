"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""
from __future__ import division
from Card import *
import sys

__author__ = "Ankur Kataria"

class PokerHand(Hand):


    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.
        Stores the result in attribute ranks.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1


    def has_pair(self):
        """Returns True if the hand has a pair"""

        if len(self.ranks) == 0:
            self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

    def has_two_pair(self):
        """Returns True if the hand has more than 2 pairs or 2 pairs"""

        if len(self.ranks) == 0:
            self.rank_hist()
        no_of_pairs = 0
        for val in self.ranks.values():
            if val >= 2:
                no_of_pairs += 1
            if no_of_pairs >= 2:
                return True
        return False

    def has_three_of_a_kind(self):
        """Returns True if the hand has three of a kind"""

        if len(self.ranks) == 0:
            self.rank_hist()
        for val in self.ranks.values():
            if val == 3:
                return True
        return False

    def has_straight(self):
        """Returns True of the hand has a Straighy"""
        ranks = self.rank
        count = 0
        for i in xrange(1, 15):
            if ranks.get(i):
                count += 1
                if count == 5:
                    return True
            else:
                count = 0
        return False


    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        if len(self.suits) == 0:
            self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def full_house(self):
        """Returns True if the hand has a full house i.e three of a kind plus a pair"""
        threekind = False
        singlepair = False

        if len(self.ranks) == 0:
            self.rank_hist()
        for val in self.ranks.values():
            if val == 3:
                singlepair == True

            elif val == 3:
                threekind == True

            if singlepair == True and threekind == True:
                return True
        return False

    def has_four_of_a_kind(self):
        """Returns True if the hand has four of a kind"""

        if len(self.ranks) == 0:
            self.rank_hist()
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False

    def has_striaght_flush(self):
        if(self.has_flush()):
            if(self.has_straight()):
                for suit in xrange(1,5)
            """"Verify for all 4 suits"""

if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print hand
        print hand.has_flush()
        print ''
