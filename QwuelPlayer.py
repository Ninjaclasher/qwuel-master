class QwuelPlayer:
    def __init__(self, user, start_health):
        self.health = start_health
        self.points = 0
        self.words_typed = set()
        self.player = user
    def __eq__(self, other_player):
        return self.player == other_player.player
