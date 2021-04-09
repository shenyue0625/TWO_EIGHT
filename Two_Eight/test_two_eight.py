#
#   from two_aces.py -> L8-1
#
# 	Experimental % of drawing two aces in a row from a shuffled Deck

#   remember that this deck is different from 52-cards deck, this deck only has 40 cards.


import deck

TRIALS = 100000


def has_two_aces():
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
    if two_aces_count>=1:
        return True
    else:
        return False
    # print (two_aces_count)
    # print ('The percentage of two aces hand is: ',100.0 * two_aces_count / TRIALS)
def has_two_eight():
    two_eight_count = 0  # accumulator for no. of times 2 aces are drawn

    for count in range(TRIALS):
        new_deck = deck.Deck()  # create a new Deck

        new_deck.shuffle()  # shuffle the Deck

        # deal card1 from new_deck
        card1=new_deck.deal_card()
        # deal card2 from new_deck
        card2 = new_deck.deal_card()
        # complete this!

        # if card1 and card2 are both aces,
        if card1._rank==2 and card2._rank==8:

        # add 1 to both_aces_count
          two_eight_count += 1
        # complete this!
    if two_eight_count>=1:
        return True
    else:
        return False

def has_four_five():
    four_five_count = 0  # accumulator for no. of times 2 aces are drawn

    for count in range(TRIALS):
        new_deck = deck.Deck()  # create a new Deck

        new_deck.shuffle()  # shuffle the Deck

        # deal card1 from new_deck
        card1=new_deck.deal_card()
        # deal card2 from new_deck
        card2 = new_deck.deal_card()
        # complete this!

        # if card1 and card2 are both aces,
        if card1._rank==2 and card2._rank==8:

        # add 1 to both_aces_count
          four_five_count += 1
        # complete this!
    if four_five_count>=1:
        return True
    else:
        return False
def main():
    two_aces_count = 0  # accumulator for no. of times 2 aces are drawn
    two_eight_count = 0
    four_five_count=0
    TRIALS=int(input('Enter the times you want to test: '))
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
        if card1._rank==2 and card2._rank==8:
          two_eight_count += 1
        # add 1 to both_aces_count
        if card1._rank==4 and card2._rank==5:
           four_five_count += 1

    print (two_aces_count)
    print ('The percentage of two aces hand is: ',100.0 * two_aces_count / TRIALS)
    print (two_eight_count)
    print ('The percentage of two_eight hand is: ',100.0 * two_eight_count / TRIALS)
    print (four_five_count)
    print ('The percentage of two_eight hand is: ',100.0 * two_eight_count / TRIALS)
# main()

def test_has_two_aces():
    assert has_two_aces()==True  #  assert has_two_aces()    is also OK
def test_has_two_eight():
    assert has_two_eight()==True   #  assert has_two_eight()    is also OK
def test_has_four_five():
    assert has_four_five()==True   #  assert has_two_eight()    is also OK
'''

collecting ... collected 3 items

test_two_eight.py::test_has_two_aces PASSED                              [ 33%]
test_two_eight.py::test_has_two_eight PASSED                             [ 66%]
test_two_eight.py::test_has_four_five PASSED                             [100%]


'''