class Card:

    cardCount = 24
    cardValues = {9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K', 14: 'A'}
    cardSuits = ['H', 'D', 'S', 'C']

    def __init__(self, suit, value):
        assert Card.cardCount > 0
        Card.cardCount -= 1
        self.value = value
        self.character = Card.cardValues.get(value)
        self.suit = Card.cardSuits[suit]

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value

    def print_card(self):
        print self.character + ' ' + self.suit
