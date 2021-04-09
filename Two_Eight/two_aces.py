#
#   from two_aces.py -> L8-1
#
# 	Experimental % of drawing two aces in a row from a shuffled Deck

#   remember that this deck is different from 52-cards deck, this deck only has 40 cards.

import deck

TRIALS = 100000


def main():
    two_aces_count = 0  # accumulator for no. of times 2 aces are drawn

    for count in range(TRIALS):
        new_deck = deck.Deck()  # create a new Deck

        new_deck.shuffle()  # shuffle the Deck

        # deal card1 from new_deck
        card1=new_deck.deal_card()
        # deal card2 from new_deck
        card2 = new_deck.deal_card()
        # complete this!

        # if card1 and card2 are both aces,
        if card1._rank==1 and card2._rank==1:

        # add 1 to both_aces_count
          two_aces_count += 1
        # complete this!

    print (two_aces_count)
    print ('The percentage of two aces hand is: ',100.0 * two_aces_count / TRIALS)


main()

'''
449
The percentage of two aces hand is:  0.449

'''