#
#  deal_hand.py -> L8-3
#
#   Modify Deck.deal_hand() as described in handout:
#       trying to deal from an empty Deck should
#       be handled with try...except by
#       'refilling' the Deck's _cards list
#       with a new list of 52 standard cards
#
#   The test code below is complete and when run should NOT
#       cause any exceptions to halt the program.
#

import deck as d


def main():

    the_deck = d.Deck()
    # the_deck.shuffle() # you can shuffle the_deck
    for count in range(11):
        hand = the_deck.deal_hand()  # last hand will empty the_deck: should not crash!

        print(hand) # str(hand) is implied with print()

main()
'''
Ace of Clubs
Ace of Diamonds
Ace of Hearts
Ace of Spades
Two of Clubs

Two of Diamonds
Two of Hearts
Two of Spades
Three of Clubs
Three of Diamonds

Three of Hearts
Three of Spades
Four of Clubs
Four of Diamonds
Four of Hearts

Four of Spades
Five of Clubs
Five of Diamonds
Five of Hearts
Five of Spades

Six of Clubs
Six of Diamonds
Six of Hearts
Six of Spades
Seven of Clubs

Seven of Diamonds
Seven of Hearts
Seven of Spades
Eight of Clubs
Eight of Diamonds

Eight of Hearts
Eight of Spades
Nine of Clubs
Nine of Diamonds
Nine of Hearts

Nine of Spades
Ten of Clubs
Ten of Diamonds
Ten of Hearts
Ten of Spades

Jack of Clubs
Jack of Diamonds
Jack of Hearts
Jack of Spades
Queen of Clubs

Queen of Diamonds
Queen of Hearts
Queen of Spades
King of Clubs
King of Diamonds

King of Hearts
King of Spades
Jack of Clubs
Four of Diamonds
Five of Spades


'''