"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from Card import *

__author__ = 'Ankur Kataria'

class PokerHand(Hand):
    labels = ['straight_flush','four_of_a_kind','full_house','flush','straight','three_of_a_kind','two_pair','pair']
    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
        #print self.suits

    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.

        Stores the result in attribute suits.
        """
        self.ranks= {}
        #print self.ranks
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
        #print self.ranks

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_pair(self):
        """Returns True if the hand has a pair, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

    def has_two_pair(self):
        """Returns True if the hand has two pair, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_hist()
        count = 0
        for val in self.ranks.values():
            if val >= 2:
                count = count + 1
            if count >= 2:
                return True

        return False

    def has_three_of_a_kind(self):
        """Returns True if the hand has three of a kind, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False


    def has_four_of_a_kind(self):
        """Returns True if the hand has three of a kind, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False

    def has_straight(self):
        """Returns True if the hand has straight, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_hist()
        count = 0
        for i in xrange(1, 15):
            if (self.ranks.get(i) or (i==14 and self.ranks.get(1))):
                count += 1
                if count == 5:
                    return True
            else:
                count = 0
        return False

    def has_full_house(self):
        """Returns True if the hand has full house, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_hist()
        three = False
        two = False
        for val in self.ranks.values():
            if (val >= 3 and three == False):
                three = True
            else:
                if(val >= 2):
                    two = True
        return (two and three)

    def has_straight_flush(self):
        """Returns True if the hand has straight flush, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        count = 0
        ss = list()
        for c in self.cards:
            ss.append((c.suit,c.rank))

        for suit in xrange(4):
            for rank in xrange(1,15):
                if (suit,rank) in ss:
                    count += 1
                    if count == 5:
                        return True
                else:
                    count = 0
        return False


        #print all_combination

    def call_all(self):

        for l in self.labels:
            func = getattr(self,'has_'+l)
            if func():
                return l
        return 'highcard'



if __name__ == '__main__':
    # make a deck

    poker_hand_Count = {'straight_flush':0, 'four_of_a_kind':0, 'full_house':0, 'flush':0,'straight':0, 'three_of_a_kind':0, 'two_pair':0, 'pair':0, 'highcard':0}
    # deal the cards and classify the hands
    for j in xrange(1000):
        deck = Deck()
        deck.shuffle()
        for i in range(7):
            hand = PokerHand()
            deck.move_cards(hand, 7)
            hand.sort()
            hand.call_all()
            poker_hand_Count[hand.call_all()] += 1

    print poker_hand_Count

    for k in poker_hand_Count:
        print "Probability of ", k, " ", poker_hand_Count[k]/7000.0
