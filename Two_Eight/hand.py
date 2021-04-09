#
#  hand.py -> L8-2
#
#  Class that represents a hand of Cards
#

import card as c
import deck as d

class Hand():
    """
    Hand represents an ordered list of 0 or more Cards,
    with one list attribute: _cards_in_hand

    Each card in the hand has its Card ref as an element of _cards_in_hand.

    """

    def __init__(self):
        '''
        Initialize this hand (referenced by self)
            so _cards_in_hand is the empty list
        '''

        self._cards_in_hand = []

    def __str__(self):
        '''
        return a string with each Card c in _cards_in_hand
            added to result, followed by '\t' (tab)
        '''
        to_return=''
        for card in self._cards_in_hand:
            to_return = to_return + str(card) + '\n'
        return to_return

    def add_card(self,card_to_add):
        '''
        add card_to_add to _cards_in_hand by appending
            to it
        '''

        self._cards_in_hand.append(card_to_add)
def main():
    """
    Create a Deck, shuffle, then create two Hands by
        dealing 10 cards, alternating.
    """
    deck=d.Deck()
    deck.shuffle()
    h1 = Hand()
    h2 = Hand()
    h3 = Hand()
    h4 = Hand()
    h1rank = []
    h2rank = []
    h3rank = []
    h4rank = []
    h1suit = []
    h2suit = []
    h3suit = []
    h4suit = []
    for count in range(2):
        card1=deck.deal_card()
        h1.add_card(card1)
        h1rank.append(int(card1._rank))
        h1suit.append(card1._suit)
        card2= deck.deal_card()
        h2.add_card(card2)
        h2rank.append( int(card2._rank))
        h2suit.append(card2._suit)
        card3 = deck.deal_card()
        h3.add_card(card3)
        h3rank.append(int(card3._rank))
        h3suit.append(card3._suit)
        card4 = deck.deal_card()
        h4.add_card(card4)
        h4rank.append(int(card4._rank))
        h4suit.append(card4._suit)
    #h1ele=h1[0]
    #print(str(card1))
    print(h1)
    print(h2)
    print(h3)
    print(h4)
    # print(h1rank)
    # print(h2rank)
    # print(h3rank)
    # print(h4rank)
    # print('Next are suits of four players.')
    # print(h1suit)
    # print(h2suit)
    # print(h3suit)
    # print(h4suit)
    # print('Next are sum  of four players\' rank.')
    # print(sum(h1rank))
    # print(sum(h2rank))
    # print(sum(h3rank))
    # print(sum(h4rank))
    # compare=[card1._rank,card2._rank,card3._rank, card4._rank]
    #print(h1[0])
if __name__ == "__main__":
    main()


'''
Six of Clubs
Two of Clubs

Eight of Hearts
Two of Spades

Five of Spades
Eight of Diamonds

Four of Clubs
Five of Clubs

[6, 4]
[3, 3]
[8, 8]
[10, 10]
'''