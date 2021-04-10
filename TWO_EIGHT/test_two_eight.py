#
#   from two_aces.py -> L8-1
#
# 	Experimental % of drawing two aces in a row from a shuffled Deck

#   remember that this deck is different from 52-cards deck, this deck only has 40 cards.


import deck

TRIALS = 100000
def has_two_ten():  # 10,10
    two_ten_count = 0  # accumulator for no. of times 2 tens are drawn

    for count in range(TRIALS):
        new_deck = deck.Deck()  # create a new Deck

        new_deck.shuffle()  # shuffle the Deck

        # deal card1 from new_deck
        card1=new_deck.deal_card()
        # deal card2 from new_deck
        card2 = new_deck.deal_card()
        # complete this!

        # if card1 and card2 are both aces,
        if card1._rank==10 and card2._rank==10:

        # add 1 to both_aces_count
          two_ten_count += 1
        # complete this!
    if two_ten_count>=1:
        return True
    else:
        return False

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
def has_two_and_eight():  # not 8,8 but 2 and 8.
    two_eight_count = 0  # accumulator for no.2 and 8  are drawn

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
def has_three_seven():
    three_seven_count = 0  # accumulator for no. of times 2 aces are drawn

    for count in range(TRIALS):
        new_deck = deck.Deck()  # create a new Deck

        new_deck.shuffle()  # shuffle the Deck

        # deal card1 from new_deck
        card1=new_deck.deal_card()
        # deal card2 from new_deck
        card2 = new_deck.deal_card()
        # complete this!

        # if card1 and card2 are both aces,
        if card1._rank==3 and card2._rank==7:

        # add 1 to both_aces_count
          three_seven_count += 1
        # complete this!
    if three_seven_count>=1:
        return True
    else:
        return False
def has_diff_cards():
    diff_cards_count = 0  # accumulator for no. of times 2 aces are drawn

    for count in range(TRIALS):
        new_deck = deck.Deck()  # create a new Deck

        new_deck.shuffle()  # shuffle the Deck

        # deal card1 from new_deck
        card1=new_deck.deal_card()
        # deal card2 from new_deck
        card2 = new_deck.deal_card()
        # complete this!

        # if card1 and card2 are both aces,
        if card1._rank != card2._rank:

        # add 1 to both_aces_count
          diff_cards_count += 1
        # complete this!
    if diff_cards_count>=1:
        return True
    else:
        return False
def main():
    two_aces_count = 0  # accumulator for no. of times 2 aces are drawn
    two_and_eight_count = 0
    four_five_count=0
    two_ten_count=0
    three_seven_count=0
    diff_cards_count=0
    same_cards_count=0
    TRIALS=int(input('Enter the times you want to test: '))
    for count in range(TRIALS):
        new_deck = deck.Deck()  # create a new Deck

        new_deck.shuffle()  # shuffle the Deck

        # deal card1 from new_deck
        card1=new_deck.deal_card()
        # deal card2 from new_deck
        card2 = new_deck.deal_card()
        # complete this!
        if card1._rank==10 and card2._rank==10:

        # add 1 to both_aces_count
          two_ten_count += 1
        # if card1 and card2 are both aces,
        if card1._rank==1 and card2._rank==1:

        # add 1 to both_aces_count
          two_aces_count += 1
        # complete this!
        if card1._rank==2 and card2._rank==8:
          two_and_eight_count += 1

        if card1._rank==4 and card2._rank==5:
           four_five_count += 1
        if card1._rank == 3 and card2._rank == 7:
            three_seven_count += 1
        if card1._rank != card2._rank:   # two cards have different ranks.

            diff_cards_count += 1
        if card1._rank == card2._rank: # two cards have same ranks.

            same_cards_count += 1
    print(two_ten_count)
    print('The percentage of two tens hand is: ', 100.0 * two_ten_count / TRIALS)
    print (two_aces_count)
    print ('The percentage of two aces hand is: ',100.0 * two_aces_count / TRIALS)
    print (two_and_eight_count)
    print ('The percentage of two_and_eight hand is: ',100.0 * two_and_eight_count / TRIALS)
    print (four_five_count)
    print ('The percentage of four_five hand is: ',100.0 * four_five_count / TRIALS)
    print(three_seven_count)
    print('The percentage of three_seven hand is: ', 100.0 * three_seven_count / TRIALS)
    print(diff_cards_count)
    print('The percentage of different cards hand is: ', 100.0 * diff_cards_count / TRIALS)
    print(same_cards_count)
    print('The percentage of different cards hand is: ', 100.0 * same_cards_count / TRIALS)
#main()
def test_has_two_ten():
    assert has_two_ten()==True  #  assert has_two_ten()    is also OK
def test_has_two_aces():
    assert has_two_aces()==True  #  assert has_two_aces()    is also OK
def test_has_two_and_eight():
    assert has_two_and_eight()==True   #  assert has_two_and_eight()    is also OK
def test_has_four_five():
    assert has_four_five()==True   #  assert has_four_five()    is also OK
def test_has_three_seven():
    assert has_three_seven()==True   #  assert has_three_seven()    is also OK


'''
if you run pytest

collecting ... collected 5 items

test_two_eight.py::test_has_two_ten PASSED                               [ 20%]
test_two_eight.py::test_has_two_aces PASSED                              [ 40%]
test_two_eight.py::test_has_two_and_eight PASSED                         [ 60%]
test_two_eight.py::test_has_four_five PASSED                             [ 80%]
test_two_eight.py::test_has_three_seven PASSED                           [100%]


if you run main()

Enter the times you want to test: 100000
771
The percentage of two tens hand is:  0.771
775
The percentage of two aces hand is:  0.775
992
The percentage of two_and_eight hand is:  0.992
1002
The percentage of four_five hand is:  1.002
1034
The percentage of three_seven hand is:  1.034
92341
The percentage of different cards hand is:  92.341
7659
The percentage of different cards hand is:  7.659

'''