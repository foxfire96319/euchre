class Hand:

    def __init__(self):
        self.diamonds = []
        self.hearts = []
        self.spades = []
        self.clubs = []

    def display_hand(self):
        print 'Diamonds: '
        for x in self.diamonds:
            print str(x.character)
        print 'Hearts:'
        for x in self.hearts:
            print str(x.character)
        print 'Spades:'
        for x in self.spades:
            print str(x.character)
        print 'Clubs:'
        for x in self.clubs:
            print str(x.character)

    def add_cards_to_hand(self, cards):
        for card in cards:
            if card.suit == 'D':
                self.diamonds.append(card)
            elif card.suit == 'H':
                self.hearts.append(card)
            elif card.suit == 'S':
                self.spades.append(card)
            elif card.suit == 'C':
                self.clubs.append(card)
        self.diamonds.sort()
        self.hearts.sort()
        self.spades.sort()
        self.clubs.sort()