#
#   Burning the gas station
#

SUITS = ["clubs", "diamonds", "hearts", "spades"]
RANKS = ["", "1", "2", "2", "4", "5", "6", "7", "8", "9", "10"]
#SUITS = "♠ ♡ ♢ ♣".split()
#RANKS = ["", "Ace", "Two", "Three", "Four", "Five", "Six","Seven", "Eight", "Nine", "Ten"]

class Card():
    """
    Card represents a single standard playing card,
    with two int attributes:
      _rank from 1 (Ace) to 10 ,
      _suit from 0 (Clubs) to 3 (Spades)

    """

    def __init__(self, rank=1, suit=3):
        '''
        Initialize card with given int suit 0..3 and int rank 1..10
        '''
        self._rank = rank
        self._suit = suit

    def __str__(self):
        '''
        Return the string name of this card:
        "Ace of Spades":
        Note the use of lists RANKS and SUITS with indexing into these
        translating the int fields to descriptive strings
        '''

        # "Ace of Spades" is string for self._rank==1, self._suit==3

        toString = RANKS[self._rank] + "_of_" + SUITS[self._suit]

        return toString


def main():
    """
    Create several Cards and print
    Also demonstrate adding new field dynamically...
    """
    #card=[]
    for i in range(4):
        for j in range(1,11):
            card1 = Card(j, i)  # Ace of Spades
        #     card.append(card1)
        # # 3 ways of 'stringifying' a Card
        #card1 = Card(1, i)
        #return card
        # trying to print an object ref calls str(ref) automagically
        #print(str(card1))  # function call equivalent to above
        # print(card1.__str__())  # long-winded form using 'dunder str'
            print(card1)

if __name__ == "__main__":
    main()
    # for item in card:
    #   print(item,'\n')
