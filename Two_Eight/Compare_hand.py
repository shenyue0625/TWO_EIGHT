from hand import Hand
import deck as d
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
    for count in range(2):
        card1=deck.deal_card()
        h1.add_card(card1)
        h1rank.append(int(card1._rank))
        card2= deck.deal_card()
        h2.add_card(card2)
        h2rank.append( int(card2._rank))
        card3 = deck.deal_card()
        h3.add_card(card3)
        h3rank.append(int(card3._rank))
        card4 = deck.deal_card()
        h4.add_card(card4)
        h4rank.append(int(card4._rank))

    print(h1)
    print(h2)
    print(h3)
    print(h4)
    print(h1rank)
    print(h2rank)
    print(h3rank)
    print(h4rank)
    print(sum(h1rank))
    print(sum(h2rank))
    print(sum(h3rank))
    print(sum(h4rank))
    # compare=[card1._rank,card2._rank,card3._rank, card4._rank]
    # print(h1[0])
if __name__ == "__main__":
    main()
'''
Eight of Clubs
Nine of Hearts

Ten of Hearts
Ten of Clubs

Eight of Spades
Seven of Spades

Two of Diamonds
Six of Diamonds

[8, 9]
[10, 10]
[8, 7]
[2, 6]
17
20
15
8

'''