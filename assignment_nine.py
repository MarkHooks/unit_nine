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

def main():
    deckocards = create_deck()
    deal(deckocards)
    draw_a_card()
    compare()