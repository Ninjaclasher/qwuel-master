import random

import text
import QwuelMode as qMode
import QwuelPlayer as qPlayer

packages = text.packages

class QwuelGame:
    def __init__(self, send_function, channel):
        self.MENTION = True
        self.cur_round = 0
        self.num_players = 0
        self.mode = qMode.QwuelMode("classic")
        self.players = []
        self.packages_added = set()
        self.word_list = set()
        self.word_avail = None
        self.word_cur = None
        self.in_progress = False
        self.word_picked = None
        self.channel = channel
        self.send_function = send_function
    async def send(self,message):
        await self.send_function(self.channel,content=message)
    def mention_user(self, user):
        return str(user.mention if self.MENTION else user.name + "#" + user.discriminator)
    def reset(self):
        self.num_players = 0
        self.cur_round = 0
        self.mode = qMode.QwuelMode("classic")
        self.players = []
        self.packages_added = set()
        self.word_list = set()
        self.word_avail = None
        self.word_cur = None
        self.word_picked = None
        self.in_progress = False

    def eliminate_players(self):
        pass

    def win_players(self):
        win_condition, second_condition = self.mode.WIN_CONDITION.split('_')
        msgs = []
        if win_condition == "PLAYER":
            if second_condition == "LAST":
                if len(self.players) == 1:
                    msgs.append(self.mention_user(self.players[0].player) + " has won the game!!!")
        elif win_condition == "POINT":
            winners = ""
            for i in self.players:
                if i.points >= int(second_condition):
                    winners += self.mention_user(i.player) + " "
            winners = winners.strip()
            if len(winners.split(" ")) > 1:
                msgs.append(winners + " have tied the game!")
            elif len(winners.split(" ")) == 1:
                msgs.append(winners + " has won the game!")
        if len(msgs) > 0:
            self.reset()
        return msgs

    def add_points(player_idx, word_idx):
        pass

    def start_game(self):
        if len(self.players) != self.num_players:
            if len(self.players) > self.num_players:
                return ["Too many players! Cannot start game."]
            return []
        elif len(self.word_list) < self.num_players**2 * int(self.mode.WORD.split('_')[1]):
            # Not enough packages, add more randomly
            textPacks = list(text.packs.keys())
            while len(self.packs) < (2 + self.capacity):
                while True:
                    # Choose random pack
                    choose = textPacks[random.randint(0,len(textPacks)-1)]
                    if not chose.lower() in self.packages_added:    # Ensure no repeats
                        self.word_list.update(packages[package_name.lower()])
                        self.packages_added.add(package_name.lower())
                        break

        if random.randint(0,1) == 0:
            self.word_list.update([text.legendary[random.randint(0,len(text.legendary)-1)]])
            
        self.in_progress = True
        self.word_avail = set(self.word_list)
        msgs = []
        msgs.append("The game has begun!!")
        msgs.append(self.start_round())
        msgs.append("QWUEL!")
        return msgs

    def start_round(self):
        word_gen_type, word_gen_num = self.mode.WORD.split('_')
        word_gen_num = int(word_gen_num)
        if word_gen_type == "ROUND":
            self.word_cur = random.sample(self.word_avail,k = word_gen_num)
            self.word_picked = [[] for x in range(word_gen_num)]
        elif word_gen_type == "PLAYER":
            self.word_cur = random.sample(self.word_avail,k = len(self.players)*word_gen_num)
            self.word_picked = [[] for x in range(len(self.players)*word_gen_num)]

        self.word_avail = self.word_avail - set(self.word_cur)
        self.cur_round += 1
        for user in self.players:
            user.words_typed = 0
        return "The words are: **" + " ".join(self.word_cur) + "**"        

    async def start(self, user, game_mode, game_players):
        if self.num_players != 0:
            await self.send("A game has already been started in this channel!")
            return
        try:
            self.mode = qMode.QwuelMode(game_mode)
        except KeyError:
            await self.send("Cannot start the game. Invalid game mode \""+ game_mode + "\" selected.")
            return
        if game_players < self.mode.MIN_PLAYER or game_players > self.mode.MAX_PLAYER:
            await self.send("Cannot start the game with " + str(game_players) + " players. Too many or not enough players for this game mode.")
            return
        self.num_players = game_players
        await self.send(self.mention_user(user) + " has started a game for " + str(game_players) + " players in the " + game_mode + " gamemode!")
        await self.join(user)

    async def join(self, user):
        msgs = []
        if self.in_progress:
            msgs.append("A game is in progress in this channel! Please wait until the game is over.")
        elif qPlayer.QwuelPlayer(user, self.mode.HEALTH) in self.players:
            msgs.append("You are already in the game, " + self.mention_user(user) + "!")
        elif self.num_players == 0:
            msgs.append("There is no game running in this channel! Please start a game")
        elif len(self.players) == self.num_players:
            msgs.append("Cannot join the game! The game is already full.")
        else:
            self.players.append(qPlayer.QwuelPlayer(user, self.mode.HEALTH))
            msgs.append(self.mention_user(user) + " has joined the game! (" + str(len(self.players)) + "/" + str(self.num_players) + ")")
            msgs.extend(self.start_game())
        await self.send('\n'.join(msgs))

    async def leave(self, user):
        msgs = []
        if self.in_progress:
            msgs.append("You cannot leave the game while the game is in progress! Please wait until the game is over.")
        elif not qPlayer.QwuelPlayer(user, self.mode.HEALTH) in self.players:
            msgs.append("You are not in the game, " + self.mention_user(user) + "!")
        else:        
            self.players.remove(qPlayer.QwuelPlayer(user, self.mode.HEALTH))
            msgs.append(self.mention_user(user) + " has left the game! (" + str(len(self.players)) + "/" + str(self.num_players) + ")")
        await self.send('\n'.join(msgs))

    async def pick(self, user, word):
        msgs = []
        if word in self.word_cur:
            idx = self.word_cur.index(word)
            player = self.players.index(user)
            if self.players[player] in self.word_picked[idx]:
                msgs.append('You already picked ' + word + ', ' + self.mention_user(user) + '!')
            else:
                self.word_picked[idx].append(self.players[player])
                self.add_points(player, idx)
        else:
            msgs.append(word + " does not exist in this round!")

    #    await self.send('\n'.join(self.win_players()))
    
    async def add(self, user, package_name):
        msgs = []
        if self.in_progress:
            msgs.append("A game is already running in this channel. Please wait until the game is over.")
        elif package_name.lower() in self.packages_added:
            msgs.append(package_name + " has already been added to this game!")
        else:
            try:
                self.word_list.update(packages[package_name.lower()])
                self.packages_added.add(package_name.lower())
                msgs.append(self.mention_user(user) + " added the " + package_name + " package!")
                msgs.extend(self.start_game())
            except KeyError:
                msgs.append("No package named " + package_name)
        await self.send('\n'.join(msgs))

    async def end(self, user):
        if self.num_players == 0:
            await self.send("There is no game running in this channel!")
            return
        if not qPlayer.QwuelPlayer(user, self.mode.HEALTH) in self.players:
            await self.send("You are not in the game, " + self.mention_user(user) + ", and therefore cannot end the game!")
            return
        self.reset()
        await self.send(self.mention_user(user) + " has ended the game!")

    async def show(self, user):
        pass

    async def account(self, user):
        pass
