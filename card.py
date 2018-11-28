class Card:

    def __init__(self, rank, suit):

        self.rank = rank
        self.suit = suit
        self.ranks = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen",
                      "king"]
        self.suits = ["spades", "hearts", "dimonds", "clubs"]

    def compared_to(self, other_card):
        """
        this is to compare cards
        :param other_card: the other persons card
        :return: this is to return a card
        """
        if self.rank > other_card.rank:
            return self
        elif other_card.rank > self.rank:
            return other_card
        else:
            if self.suit > other_card.suit:
                return self
            else:
                return other_card

    def __str__(self):

        new_cards = self.ranks[self.rank] + " of " + self.suits[self.suit]
        return new_cards
