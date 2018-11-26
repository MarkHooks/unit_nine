import card
import deck


def create_deck():
    deckocards = deck.Deck()
    deckocards.shuffle()
    return deckocards


def deal(deckocards):
    user_card = []
    computer_cards = []
    for cards in range(5):
        user_card.append(deckocards.draw_a_card())
        computer_cards.append(deckocards.draw_a_card())
    return user_card, computer_cards


def show_cards(user_card, computer_cards):
    print("user has a ", user_card)
    print("the computer has a ", computer_cards)


def compare(user_card, computer_cards):
    higher = user_card.compared_to(computer_cards)
    user_total = 0
    computer_total = 0
    if user_card == higher:
        user_total = + 1
        print("user gets a point")
    else:
        computer_total = + 1
        print("computer gets a point")
    return computer_total, user_total

def main():

    deckocards = create_deck()
    user_card, computer_cards = deal(deckocards)
    for x in range(len(user_card)):
        show_cards(user_card[x], computer_cards[x])
        computer_total, user_total = (user_card[x], computer_cards[x])
    if user_total > computer_total:
        print("you win")
    else:
        print("computer wins")

main()
