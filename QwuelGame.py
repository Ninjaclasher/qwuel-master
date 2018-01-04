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
        self.round_words_typed = 0
        self.mode = qMode.QwuelMode("classic")
        self.players = []
        self.packages_added = set()
        self.word_list = set()
        self.word_avail = None
        self.word_cur = None
        self.word_cur_type = []
        self.in_progress = False
        self.channel = channel
        self.send_function = send_function
    async def send(self,message):
        await self.send_function(self.channel,content=message)
    def mention_user(self, user):
        return str(user.mention if self.MENTION else user.name + "#" + user.discriminator)
    def reset(self):
        self.num_players = 0
        self.cur_round = 0
        self.round_words_typed = 0
        self.mode = qMode.QwuelMode("classic")
        self.players = []
        self.packages_added = set()
        self.word_list = set()
        self.word_avail = None
        self.word_cur = None
        self.word_cur_type = []
        self.in_progress = False

    def damage(self, player_idx):
        self.players[player_idx].health -= 1
        if self.players[player_idx].health == 0:
            user = self.mention_user(self.players[player_idx].player)
            del self.players[player_idx]
            return user + ' has no more lives!'
        else:
            return self.mention_user(self.players[player_idx].player) + ' has ' + str(self.players[player_idx].health) + ' :hearts: left!'


    def eliminate_players(self, player_idx):
        if self.mode.ELIMINATE_CONDITION == "NONE":
            return []
        msgs = []
        for x in self.mode.ELIMINATE_CONDITION.split('|'):
            lose_condition, second_condition = x.split('_')
            if lose_condition == "TYPE":
                if second_condition == "LAST":
                    msgs.append(self.mention_user(self.players[player_idx].player) + " typed last!")
                    msgs.append(self.damage(player_idx))
                elif second_condition == "LEAST":
                    user, words_typed = -1, 10000
                    for i in range(len(self.players)):
                        if self.players[i].words_typed < words_typed:
                            user = i
                            words_typed = self.players[i].words_typed
                        elif self.players[i].words_typed == words_typed:
                            user = -1
                    if user == -1:
                        msgs.append('Multiple players typed ' + str(words_typed) + ' words! Nobody loses a life!')
                    else:
                        msgs.append(self.mention_user(self.players[user].player) + ' typed the least words (' + str(words_typed) + ')!')
                        msgs.append(self.damage(user))
            elif lose_condition == "POINT":
                if second_condition == "LEAST":
                    user, points = -1, 10000
                    for i in range(len(self.players)):
                        if self.players[i].points < points:
                            user = i
                            points = self.players[i].points
                        elif self.players[i].points == points:
                            user = -1
                    if user == -1:
                        msgs.append('Multiple players tied for ' + str(points) + ' points! Nobody loses a life!')
                    else:
                        msgs.append(self.mention_user(self.players[user].player) + ' had the least points (' + str(points) + ')!')
                        msgs.append(self.damage(user))
        return msgs

    def leaderboard(self):
        msgs = []
        if self.mode.POINT_CONDITION != "NONE" and self.mode.POINT_AWARDED != "0":
            msgs.append("The current point standings are:")
            for x in self.players:
                msgs.append(self.mention_user(x.player) + " " + str(x.points))
        if self.mode.ELIMINATE_CONDITION != "NONE":
            msgs.append("The current life standings are:")
            for x in self.players:
                msgs.append(self.mention_user(x.player) + " " + str(x.health) + ":hearts:")
        return msgs            

    def win_players(self):
        win_condition, second_condition = self.mode.WIN_CONDITION.split('_')
        msgs = []
        if win_condition == "PLAYER":
            if second_condition == "LAST":
                if len(self.players) == 1:
                    msgs.append(self.mention_user(self.players[0].player) + " has won the game!!!")
        elif win_condition == "POINT":
            winners = []
            for i in self.players:
                if i.points >= int(second_condition):
                    winners.append(self.mention_user(i.player))
            if len(winners) > 1:
                msgs.append(' '.join(winners) + " have tied the game!")
            elif len(winners) == 1:
                msgs.append(' '.join(winners) + " has won the game!")
        if len(msgs) > 0:
            self.reset()
        return msgs

    def add_points(self, player_idx, word_idx):
        if self.mode.POINT_CONDITION == "NONE" or self.mode.POINT_AWARDED == "0":
            return
        condition_type = self.mode.POINT_CONDITION.split('_')[0]
        if condition_type == "TYPE":
            place = self.mode.POINT_CONDITION.split('_')[1]
            if place == "FIRST":
                num_player_to_award_points = int(self.mode.POINT_CONDITION.split('_')[2])
                if self.round_words_typed >= num_player_to_award_points:
                    return
                try:
                    self.players[player_idx].points += int(self.mode.POINT_AWARDED)
                except:
                    if self.mode.POINT_AWARDED == "ROUND":
                        self.players[player_idx].points += self.cur_round
                    elif self.mode.POINT_AWARDED == "PLAYER":
                        self.players[player_idx].points += num_player_to_award_points - self.round_words_typed

    def start_game(self):
        global packages
        if len(self.players) != self.num_players:
            if len(self.players) > self.num_players:
                return ["Too many players! Cannot start game."]
            return []
        words_needed = self.num_players**2 * int(self.mode.WORD.split('_')[1])
        msgs = []
        if len(self.word_list) <= words_needed:
            textPacks = set(packages.keys()) - self.packages_added
            msgs.append("Not enough words in currently selected packages. Randomly selecting packages...")
            while len(self.word_list) <= words_needed:
                package_name = random.sample(textPacks,k=1)[0]
                msgs.append("Selected the " + package_name + " package.")
                textPacks.remove(package_name)
                self.word_list.update(packages[package_name])
                self.packages_added.add(package_name)

        if random.randint(0,1) == 0:
            self.word_list.update([text.legendary[random.randint(0,len(text.legendary)-1)]])
            
        self.in_progress = True
        self.word_avail = set(self.word_list)
        msgs.append("The game has begun!!")
        msgs.append(self.start_round())
        msgs.append("QWUEL!")
        return msgs

    def start_round(self):
        word_gen_type, word_gen_num = self.mode.WORD.split('_')
        word_gen_num = int(word_gen_num)
        if word_gen_type == "ROUND":
            self.word_cur = random.sample(self.word_avail,k = word_gen_num)
        elif word_gen_type == "PLAYER":
            self.word_cur = random.sample(self.word_avail,k = len(self.players)*word_gen_num)

        self.word_avail = self.word_avail - set(self.word_cur)
        self.cur_round += 1
        for user in self.players:
            user.words_typed = 0
        self.round_words_typed = 0
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
        player = self.players.index(qPlayer.QwuelPlayer(user, self.mode.HEALTH))
        if word in self.word_cur:
            idx = self.word_cur.index(word)
            if self.players[player].words_typed > 0 and self.mode.SPECIAL == "NONE":
                msgs.append("You already typed this round, " + self.mention_user(user) + "!")
            elif word in self.word_cur_type:
                msgs.append(word + " has already been picked!")
            else:
                self.add_points(player, idx)
                self.players[player].words_typed += 1
                self.round_words_typed += 1
                self.word_cur_type.append(word)
                msgs.append(self.mention_user(user) + " has picked " + word + "!")
        else:
            msgs.append(word + " does not exist in this round!")
        if self.round_words_typed == len(self.word_cur):
            msgs.extend(self.eliminate_players(player))
            ret = self.win_players()
            msgs.extend(ret)
            if len(ret) == 0:
                msgs.extend(self.leaderboard())
                msgs.append(self.start_round())
        await self.send('\n'.join(msgs))
    
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
