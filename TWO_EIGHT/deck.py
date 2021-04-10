#
#  Part of Lab 8
#

import random
import card
import hand

class Deck():
    """
    Represents a deck of 40 standard playing cards,
        as a list of Card refs
    """

    def __init__(self):
        '''
        Initialize deck: field _cards is list containing
            40 Card refs, initially
        :return: nothing
        '''

        self._cards = []
        for rank in range(1, 11):
            for suit in range(4):
                c = card.Card(rank, suit)
                self._cards.append(c)

    def __str__(self):
        '''
        "Stringified" deck: string of all Card names,
        in deck order separated by '\n' for easier reading
        '''

        deck_str_to_return = ''

        # visit every card in deck this way:
        #
        # for index in range(len(self._cards)):
        #     self._cards[index]
        #
        # but it's easier to do it as follows:

        for c in self._cards:
            temp = str(c)  # temp is the stringified card
            deck_str_to_return = deck_str_to_return + temp + "\n"  # note \n at end

        return deck_str_to_return

    def shuffle(self):
        random.shuffle(self._cards)  # note random function to do this

    def deal_card(self):
        top_card = self._cards.pop(0)  # get and remove top card from deck
        return top_card

    ### L8-3: add new method deal_hand() to Deck (requires import of Hand class)

    def deal_hand(self):
        hand_to_return = hand.Hand()
        for count in range(5):
            try:
                next_card = self.deal_card()
            except IndexError:
                #refill the deck and shuffle
                self.__init__()
                self.shuffle()
                next_card = self.deal_card()
            hand_to_return.add_card(next_card)
        return hand_to_return


def main():
    '''
    Create, print then shuffle, print again
    Then deal first two cards and print, along with bottom card
    '''

    deck = Deck()
    print(str(deck))

    print("Now we shuffle:\n")

    deck.shuffle()
    print(str(deck))

    card_1 = deck.deal_card()
    card_2 = deck.deal_card()

    print("The first card dealt is", card_1, "and the second is", card_2)
    print("Bottom of deck is", deck._cards[-1])  # can't hide the implementation!


# only run main() if we're not importing it...
if __name__ == "__main__":
    main()
