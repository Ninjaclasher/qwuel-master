class QwuelMode:
    def __init__(self, mode : str):
        mode = mode.lower()
        self.WORD = "PLAYER_1"
        self.MIN_PLAYER = 2
        self.MAX_PLAYER = 10
        self.ELIMINATE_CONDITION = "TYPE_LAST"
        self.HEALTH = 3
        self.WIN_CONDITION = "PLAYER_LAST"
        self.POINT_AWARDED = "0"
        self.POINT_CONDITION = "NONE"
        self.SPECIAL = "NONE"
        if mode == "classic":
            pass
        elif mode == "hog":
            self.WORD = "ROUND_1"
            self.POINT_CONDITION = "TYPE_FIRST_1"
            self.POINT_AWARDED = "ROUND"
            self.ELIMINATE_CONDITION = "NONE"
            self.WIN_CONDITION = "POINT_15"
        elif mode == "duel":
            self.WORD = "ROUND_1"
            self.POINT_CONDITION = "TYPE_FIRST_1"
            self.POINT_AWARDED = "1"
            self.ELIMINATE_CONDITION = "NONE"
            self.WIN_CONDITION = "POINT_5"
        elif mode == "elimination":
            self.MIN_PLAYER = 3
            self.HEALTH = 1
        elif mode == "glory":
            self.MIN_PLAYER = 3
            self.POINT_CONDITION = "TYPE_FIRST_3"
            self.POINT_AWARDED = "PLAYER"
            self.ELIMINATE_CONDITION = "NONE"
            self.WIN_CONDITION = "POINT_15"
        elif mode == "banquet":
            self.WORD = "PLAYER_2"
            self.ELIMINATE_CONDITION = "TYPE_LEAST"
            self.SPECIAL = "TYPE_MULTIPLE"
        elif mode == "tourney":
            self.WORD = "ROUND_1"
            self.MIN_PLAYER = 4
            self.HEALTH
            self.SPECIAL = "TOURNEY"
        elif mode == "hardcore":
            self.WORD = "PLAYER_3"
            self.ELIMINATE_CONDITION = "TYPE_LAST|TYPE_WRONG"
            self.HEALTH = 1
            self.SPECIAL = "TYPE_ALL"
        else:
            raise KeyError
