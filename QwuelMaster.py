import random
from discord import *
from pprint import pprint
from collections import namedtuple
import string

bot = Client()

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")

games = {}
packages = {}
packages["programming"] = ["unsigned", "signed", "competitive", "pointer", "reference", "instance", "class", "long", "integer", "floating-point", "fenwick-tree", "segment-tree", "decomposition", "optimizations", "assembly", "pascal", "fermat", "hyperoperation", "exponentiation", "tetration", "pentation", "hexation", "erlang", "turing", "microprocessor", "microcontroller", "typedef", "inheritance", "encapsulation", "programming", "scheduler", "diffie-hellman", "djikstra", "eratosthenes", "segmentation", "line-sweep", "kruskal", "attribute", "variable", "constant", "function", "method", "parameter", "return", "string", "race-condition", "multithreading", "judge", "template", "bit", "nibble", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte", "petabyte", "exabyte", "zettabyte", "yottabyte"]

packages["pokemon"] = ["abomasnow", "abra", "absol", "accelgor", "aegislash", "aerodactyl", "aggron", "aipom", "alakazam", "alomomola", "altaria", "amaura", "ambipom", "amoonguss", "ampharos", "anorith", "arbok", "arcanine", "arceus", "archen", "archeops", "ariados", "armaldo", "aromatisse", "aron", "articuno", "audino", "aurorus", "avalugg", "axew", "azelf", "azumarill", "azurill", "bagon", "baltoy", "banette", "barbaracle", "barboach", "basculin", "bastiodon", "bayleef", "beartic", "beautifly", "beedrill", "beheeyem", "beldum", "bellossom", "bellsprout", "bergmite", "bibarel", "bidoof", "binacle", "bisharp", "blastoise", "blaziken", "blissey", "blitzle", "boldore", "bonsly", "bouffalant", "braixen", "braviary", "breloom", "bronzong", "bronzor", "budew", "buizel", "bulbasaur", "buneary", "bunnelby", "burmy", "butterfree", "cacnea", "cacturne", "camerupt", "carbink", "carnivine", "carracosta", "carvanha", "cascoon", "castform", "caterpie", "celebi", "chandelure", "chansey", "charizard", "charmander", "charmeleon", "chatot", "cherrim", "cherubi", "chesnaught", "chespin", "chikorita", "chimchar", "chimecho", "chinchou", "chingling", "cinccino", "clamperl", "clauncher", "clawitzer", "claydol", "clefable", "clefairy", "cleffa", "cloyster", "cobalion", "cofagrigus", "combee", "combusken", "conkeldurr", "corphish", "corsola", "cottonee", "cradily", "cranidos", "crawdaunt", "cresselia", "croagunk", "crobat", "croconaw", "crustle", "cryogonal", "cubchoo", "cubone", "cyndaquil", "darkrai", "darmanitan", "darumaka", "dedenne", "deerling", "deino", "delcatty", "delibird", "delphox", "deoxys", "dewgong", "dewott", "dialga", "diggersby", "diglett", "ditto", "dodrio", "doduo", "donphan", "doublade", "dragalge", "dragonair", "dragonite", "drapion", "dratini", "drifblim", "drifloon", "drilbur", "drowzee", "druddigon", "ducklett", "dugtrio", "dunsparce", "duosion", "durant", "dusclops", "dusknoir", "duskull", "dustox", "dwebble", "eelektrik", "eelektross", "eevee", "ekans", "electabuzz", "electivire", "electrike", "electrode", "elekid", "elgyem", "emboar", "emolga", "empoleon", "entei", "escavalier", "espeon", "espurr", "excadrill", "exeggcute", "exeggutor", "exploud", "farfetch\"d", "fearow", "feebas", "fennekin", "feraligatr", "ferroseed", "ferrothorn", "finneon", "flaaffy", "flareon", "fletchinder", "fletchling", "floatzel", "floette", "florges", "flygon", "foongus", "forretress", "fraxure", "frillish", "froakie", "frogadier", "froslass", "furfrou", "furret", "gabite", "gallade", "galvantula", "garbodor", "garchomp", "gardevoir", "gastly", "gastrodon", "genesect", "gengar", "geodude", "gible", "gigalith", "girafarig", "giratina", "glaceon", "glalie", "glameow", "gligar", "gliscor", "gloom", "gogoat", "golbat", "goldeen", "golduck", "golem", "golett", "golurk", "goodra", "goomy", "gorebyss", "gothita", "gothitelle", "gothorita", "gourgeist", "granbull", "graveler", "greninja", "grimer", "grotle", "groudon", "grovyle", "growlithe", "grumpig", "gulpin", "gurdurr", "gyarados", "happiny", "hariyama", "haunter", "hawlucha", "haxorus", "heatmor", "heatran", "heliolisk", "helioptile", "heracross", "herdier", "hippopotas", "hippowdon", "hitmonchan", "hitmonlee", "hitmontop", "ho-oh", "honchkrow", "honedge", "hoothoot", "hoppip", "horsea", "houndoom", "houndour", "huntail", "hydreigon", "hypno", "igglybuff", "illumise", "infernape", "inkay", "ivysaur", "jellicent", "jigglypuff", "jirachi", "jolteon", "joltik", "jumpluff", "jynx", "kabuto", "kabutops", "kadabra", "kakuna", "kangaskhan", "karrablast", "kecleon", "keldeo", "kingdra", "kingler", "kirlia", "klang", "klefki", "klink", "klinklang", "koffing", "krabby", "kricketot", "kricketune", "krokorok", "krookodile", "kyogre", "kyurem", "lairon", "lampent", "landorus", "lanturn", "lapras", "larvesta", "larvitar", "latias", "latios", "leafeon", "leavanny", "ledian", "ledyba", "lickilicky", "lickitung", "liepard", "lileep", "lilligant", "lillipup", "linoone", "litleo", "litwick", "lombre", "lopunny", "lotad", "loudred", "lucario", "ludicolo", "lugia", "lumineon", "lunatone", "luvdisc", "luxio", "luxray", "machamp", "machoke", "machop", "magby", "magcargo", "magikarp", "magmar", "magmortar", "magnemite", "magneton", "magnezone", "makuhita", "malamar", "mamoswine", "manaphy", "mandibuzz", "manectric", "mankey", "mantine", "mantyke", "maractus", "mareep", "marill", "marowak", "marshtomp", "masquerain", "mawile", "medicham", "meditite", "meganium", "meloetta", "meowstic", "meowth", "mesprit", "metagross", "metang", "metapod", "mew", "mewtwo", "mienfoo", "mienshao", "mightyena", "milotic", "miltank", "mime jr.", "minccino", "minun", "misdreavus", "mismagius", "moltres", "monferno", "mothim", "mr. mime", "mudkip", "muk", "munchlax", "munna", "murkrow", "musharna", "natu", "nidoking", "nidoqueen", "nidoran♀", "nidoran♂", "nidorina", "nidorino", "nincada", "ninetales", "ninjask", "noctowl", "noibat", "noivern", "nosepass", "numel", "nuzleaf", "octillery", "oddish", "omanyte", "omastar", "onix", "oshawott", "pachirisu", "palkia", "palpitoad", "pancham", "pangoro", "panpour", "pansage", "pansear", "paras", "parasect", "patrat", "pawniard", "pelipper", "persian", "petilil", "phanpy", "phantump", "phione", "pichu", "pidgeot", "pidgeotto", "pidgey", "pidove", "pignite", "pikachu", "piloswine", "pineco", "pinsir", "piplup", "plusle", "politoed", "poliwag", "poliwhirl", "poliwrath", "ponyta", "poochyena", "porygon", "porygon-z", "porygon2", "primeape", "prinplup", "probopass", "psyduck", "pumpkaboo", "pupitar", "purrloin", "purugly", "pyroar", "quagsire", "quilava", "quilladin", "qwilfish", "raichu", "raikou", "ralts", "rampardos", "rapidash", "raticate", "rattata", "rayquaza", "regice", "regigigas", "regirock", "registeel", "relicanth", "remoraid", "reshiram", "reuniclus", "rhydon", "rhyhorn", "rhyperior", "riolu", "roggenrola", "roselia", "roserade", "rotom", "rufflet", "sableye", "salamence", "samurott", "sandile", "sandshrew", "sandslash", "sawk", "sawsbuck", "scatterbug", "sceptile", "scizor", "scolipede", "scrafty", "scraggy", "scyther", "seadra", "seaking", "sealeo", "seedot", "seel", "seismitoad", "sentret", "serperior", "servine", "seviper", "sewaddle", "sharpedo", "shaymin", "shedinja", "shelgon", "shellder", "shellos", "shelmet", "shieldon", "shiftry", "shinx", "shroomish", "shuckle", "shuppet", "sigilyph", "silcoon", "simipour", "simisage", "simisear", "skarmory", "skiddo", "skiploom", "skitty", "skorupi", "skrelp", "skuntank", "slaking", "slakoth", "sliggoo", "slowbro", "slowking", "slowpoke", "slugma", "slurpuff", "smeargle", "smoochum", "sneasel", "snivy", "snorlax", "snorunt", "snover", "snubbull", "solosis", "solrock", "spearow", "spewpa", "spheal", "spinarak", "spinda", "spiritomb", "spoink", "spritzee", "squirtle", "stantler", "staraptor", "staravia", "starly", "starmie", "staryu", "steelix", "stoutland", "stunfisk", "stunky", "sudowoodo", "suicune", "sunflora", "sunkern", "surskit", "swablu", "swadloon", "swalot", "swampert", "swanna", "swellow", "swinub", "swirlix", "swoobat", "sylveon", "taillow", "talonflame", "tangela", "tangrowth", "tauros", "teddiursa", "tentacool", "tentacruel", "tepig", "terrakion", "throh", "thundurus", "timburr", "tirtouga", "togekiss", "togepi", "togetic", "torchic", "torkoal", "tornadus", "torterra", "totodile", "toxicroak", "tranquill", "trapinch", "treecko", "trevenant", "tropius", "trubbish", "turtwig", "tympole", "tynamo", "typhlosion", "tyranitar", "tyrantrum", "tyrogue", "tyrunt", "umbreon", "unfezant", "unown", "ursaring", "uxie", "vanillish", "vanillite", "vanilluxe", "vaporeon", "venipede", "venomoth", "venonat", "venusaur", "vespiquen", "vibrava", "victini", "victreebel", "vigoroth", "vileplume", "virizion", "vivillon", "volbeat", "volcarona", "voltorb", "vullaby", "vulpix", "wailmer", "wailord", "walrein", "wartortle", "watchog", "weavile", "weedle", "weepinbell", "weezing", "whimsicott", "whirlipede", "whiscash", "whismur", "wigglytuff", "wingull", "wobbuffet", "woobat", "wooper", "wormadam", "wurmple", "wynaut", "xatu", "xerneas", "yamask", "yanma", "yanmega", "yveltal", "zangoose", "zapdos", "zebstrika", "zekrom", "zigzagoon", "zoroark", "zorua", "zubat", "zweilous", "zygarde"]

class QwuelMode:
    def __init__(self, mode : str):
        mode = mode.lower()
        self.WORD = "PLAYER_1"
        self.MIN_PLAYER = 1
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
            self.POINT_CONDITION = "FIRST_TYPE_1"
            self.POINT_AWARDED = "ROUND"
            self.ELIMINATE_CONDITION = "NONE"
            self.WIN_CONDITION = "POINT_15"
        elif mode == "duel":
            self.WORD = "ROUND_1"
            self.POINT_CONDITION = "FIRST_TYPE_1"
            self.POINT_AWARDED = "1"
            self.ELIMINATE_CONDITION = "NONE"
            self.WIN_CONDITION = "POINT_5"
        elif mode == "elimination":
            self.MIN_PLAYER = 3
            self.HEALTH = 1
        elif mode == "glory":
            self.MIN_PLAYER = 3
            self.POINT_CONDITION = "FIRST_TYPE_3"
            self.POINT_AWARDED = "PLAYER"
            self.ELIMINATE_CONDITION = "NONE"
            self.WIN_CONDITION = "POINT_15"
        elif mode == "banquet":
            self.WORD = "PLAYER_2"
            self.ELIMINATE_CONDITION = "POINT_LEAST"
            self.POINT_AWARDED = "1"
            self.POINT_CONDITION = "FIRST_TYPE_1"
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
        else:
            raise KeyError

class QwuelPlayer:
    def __init__(self, user, start_health):
        self.health = start_health
        self.points = 0
        self.words_typed = 0
        self.player = user
    def __eq__(self, other_player):
        return self.player == other_player.player

class QwuelGame:
    def __init__(self, send_function, channel):
        self.MENTION = True
        self.cur_round = 0
        self.num_players = 0
        self.mode = QwuelMode("classic")
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
        self.mode = QwuelMode("classic")
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
        return msgs


    def start_game(self):
        if len(self.players) != self.num_players:
            if len(self.players) > self.num_players:
                return ["Too many players! Cannot start game."]
            return []
        elif len(self.word_list) < self.num_players**2 * int(self.mode.WORD.split('_')[1]):
            if len(self.word_list) == 0:
                return ["No packages have been added! Please add a package for the game to begin."]
            else:
                return ["There are not enough words in the current packages selected! Please add more packages for the game to begin."]
        self.in_progress = True
        self.word_avail = set(self.word_list)
        msgs = []
        msgs.append("The game has begun!!")
        msgs.append(self.start_round())
        msgs.append("QWEUL!")
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
            self.mode = QwuelMode(game_mode)
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
        elif QwuelPlayer(user, self.mode.HEALTH) in self.players:
            msgs.append("You are already in the game, " + self.mention_user(user) + "!")
        elif self.num_players == 0:
            msgs.append("There is no game running in this channel! Please start a game")
        elif len(self.players) == self.num_players:
            msgs.append("Cannot join the game! The game is already full.")
        else:
            self.players.append(QwuelPlayer(user, self.mode.HEALTH))
            msgs.append(self.mention_user(user) + " has joined the game! (" + str(len(self.players)) + "/" + str(self.num_players) + ")")
            msgs.extend(self.start_game())
        await self.send('\n'.join(msgs))

    async def leave(self, user):
        msgs = []
        if self.in_progress:
            msgs.append("You cannot leave the game while the game is in progress! Please wait until the game is over.")
        elif not QwuelPlayer(user, self.mode.HEALTH) in self.players:
            msgs.append("You are not in the game, " + self.mention_user(user) + "!")
        else:        
            self.players.remove(QwuelPlayer(user, self.mode.HEALTH))
            msgs.append(self.mention_user(user) + " has left the game! (" + str(len(self.players)) + "/" + str(self.num_players) + ")")
        await self.send('\n'.join(msgs))

    async def pick(self, user, word):
        await self.send('\n'.join(self.win_players()))
    
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
                msgs.append("No packaged named " + package_name)
        await self.send('\n'.join(msgs))

    async def end(self, user):
        if self.num_players == 0:
            await self.send("There is no game running in this channel!")
            return
        if not QwuelPlayer(user, self.mode.HEALTH) in self.players:
            await self.send("You are not in the game, " + self.mention_user(user) + ", and therefore cannot end the game!")
            return
        self.reset()
        await self.send(self.mention_user(user) + " has ended the game!")

    async def show(self, user):
        pass

    async def account(self, user):
        pass


async def process_command(send, message, command):
    try:
        game = games[message.channel]
    except KeyError:
        game = games[message.channel] = QwuelGame(send,message.channel)
    try:
        if command[0] == "start" and len(command) == 3:
            await game.start(message.author, command[1], int(command[2]))
        elif command[0] == "join" and len(command) == 1:
            await game.join(message.author)
        elif command[0] == "leave" and len(command) == 1:
            await game.leave(message.author)
        elif command[0] == "add" and len(command) == 2:
            await game.add(message.author, command[1])
        elif command[0] == "pick" and len(command) == 2:
            await game.pick(message.author, command[1])
        elif command[0] == "end" and len(command) == 1:
            await game.end(message.author)
        elif command[0] == "show" and len(command) == 1:
            pass
        elif command[0] == "account" and len(command) == 1:
            pass
    except:
        pass


COMMAND_PREFIX = "]"

@bot.event
async def on_message(message):
    if message.type == MessageType.default and message.content.startswith(COMMAND_PREFIX):
        command = message.content[len(COMMAND_PREFIX):].strip().split(" ")
        await process_command(bot.send_message,message,command)

bot.run("token")
