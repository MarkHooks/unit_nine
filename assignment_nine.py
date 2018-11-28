# mark hooks 11/28/18
# this program creates a compare card game using classes

import deck


def create_deck():
    """
    this creates the deck
    :return: the deck of cards
    """
    deckocards = deck.Deck()
    deckocards.shuffle()
    return deckocards


def deal(deckocards):
    """
    this deals out the cards to the user and computer
    :param deckocards:
    :return: the user's and computer's cards
    """
    user_card = []
    computer_cards = []
    for cards in range(5):
        user_card.append(deckocards.draw_a_card())
        computer_cards.append(deckocards.draw_a_card())
    return user_card, computer_cards


def show_cards(user_card, computer_cards):
    """
    this shows the number and suit of the card
    :param user_card:
    :param computer_cards:
    :return: none
    """
    print("user has a ", user_card)
    print("the computer has a ", computer_cards)


def compare(user_card, computer_cards, user_total, computer_total):
    """
    this program compares the cards and decides which one is larger
    :param user_card:
    :param computer_cards:
    :param user_total:
    :param computer_total:
    :return: both of their totals
    """
    higher = user_card.compared_to(computer_cards)
    if user_card == higher:
        user_total += 1
        print("user gets a point")
        print("")
    else:
        computer_total += 1
        print("computer gets a point")
        print("")
    return computer_total, user_total


def main():
    user_total = 0
    computer_total = 0
    deckocards = create_deck()
    user_card, computer_cards = deal(deckocards)
    for x in range(len(user_card)):
        show_cards(user_card[x], computer_cards[x])
        computer_total, user_total = compare(user_card[x], computer_cards[x], user_total, computer_total)
    if user_total > computer_total:
        print("you win")
    else:
        print("computer wins")


main()
