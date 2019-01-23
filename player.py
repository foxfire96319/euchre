from hand import Hand


class Player:

    player_count = 4

    def __init__(self, name):
        assert Player.player_count > 1
        Player.player_count -= 1
        self.name = name
        self.hand = Hand()

    @staticmethod
    def display_count():
        return Player.player_count

    def display_name(self):
        print "Player name: " + self.name

    def display_hand(self):
        self.hand.display_hand()

    def add_hand(self, cards):
        self.hand.add_cards_to_hand(cards)
