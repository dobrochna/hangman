"""Player class for the hangman game"""


class Player(object):
    def __init__(self, name):
        """Init player with name and chances"""
        self.name = name
        self.chances = 5

    def wrong_letter(self):
        """Decrement chances when wrong letter was passed"""
        self.chances -= 1
        return self.chances

    def reset_chances(self):
        """Reset chances when the new game has started"""
        self.chances = 5
