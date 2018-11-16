class Card:

    def __init__(self, rank, suit):

        self.rank = rank
        self.suit = suit

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
