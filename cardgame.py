from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

allcards = [(s, r) for s in SUITE for r in RANKS]


class Deck:
    def __init__(self):
        print("Creating deck")
        self.allcards = allcards

    def shuffle(self):
        print("Shuffling")
        shuffle(self.allcards)

    def divide_in_half(self):
        print("Dividing in half")
        return self.allcards[0:26], self.allcards[26:]


class Hand:
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "contains {} cards".format(len(self.cards))

    def add_cards(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        self.cards.pop()


class Player:
    pass


def main():
    pass


if __name__ == '__main__':
    main()
        