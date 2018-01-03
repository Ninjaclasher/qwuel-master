# Stores info for help command
command_info = {
    "add" : ["`]add <pack>`", "Requests to add a pack to the deck."],
    "end" : ["`]end`", "Ends game. Only the game admin can do this."],
    "help" : ["`]help <commandName>`", "Shows syntax and purpose of a command."],
    "join" : ["`]join`", "Joins game queue in text channel."],
    "leave" : ["`]leave`", "Leaves game queue in text channel."],
    "players" : ["`]players`", "Shows status of all players."],
    "pack" : ["`]pack <pack (optional)>`", "Shows all cards in a pack or lists all packs."],
    "start" : ["`]start <players>`", "Starts new game in channel with specified players."]
    }

intro = "Welcome to Qwuel, the PVP typing game! Every round words will appear, use ]pick to pick them before others do! The last player to pick a word loses 1 life, and when you lose all 3 lives you're eliminated. Good luck!"

# Ppl who helped out
creds = {
    "Homieman" : "Pack writer: League1, Polytopia",
    "Trostel" : "Pack writer: Oregairu",
    "Grislan" : "Dev!",
    "root" : "Dev!",
    "Ninjaclasher": "Dev!"
    }

legendary = [
    "YI", "TROSTEL", "HOMIEMAN", "JACKDAW", "PALERPASTELS", "GRISLAN",
    "STARFY", "ZHANG", "TRASHBANDITO", "BLAZEFIRE", "CATH",
    "EMACODO", "URURUNWOLF", "ASHRAFF", "HITORI", "BEAUTIFULTIMES",
    "AYANA", "HEIMERDINGER", "DISCORD", "HUEHUEHUE", "WUMPUS", "APPLEDOOR", "NADEKO"
    ]

packages = {
    "eggz" : [
        "Eggcelent", "Eggstreme", "Eggstremism", "Eggscalating", "Eggscalator",
        "Eggsquisite", "Eggspected", "Uneggspected", "Eggceptional", "Eggcruiciating",
        "Eggscatly", "Eggciting", "Eggstravagant", "Eggsplosive", "Eggscercize",
        "Eggsaggerate", "Eggxorcist", "Eggxorcism"
        ],
    "league1" : [
        "Annie", "Ashe", "Akali", "Aatrox", "Alistar",
        "Bard", "Braum", "Cassiopiea", "Caitlyn", "Kayn",
        "Draven", "Darius", "Evelyn", "Garen", "Hecarim",
        "Irelia", "Ivern", "Jinx", "Kassadin", "Leona",
        "Maokai", "Malphite", "Nami", "Nidalee", "Orianna"
        ],
    "minecraft" : [
        "Creeper", "Skeleton", "Zombie", "Ender", "Nether",
        "Pigmen", "Blaze", "Wither", "Ghast", "Crafting",
        "Diamonds", "Pickaxe", "Enchanting", "Notch", "Redstone",
        "Block", "Sandstone", "Glowstone", "Cobblestone", "Furnace",
        "Chest", "Bed", "Piston", "Obsidian", "Portal"
        ],
    "overwatch" : [
        "Blizzard", "Doomfist", "Genji", "McCree", "Pharah",
        "Reaper", "Soldier76", "Sombra", "Tracer", "Bastion",
        "Hanzo", "Junkrat", "Mei", "Widowmaker", "D.Va",
        "Orisa", "Reinhardt", "Roadhog", "Winston", "Zarya",
        "Ana", "Lucio", "Mercy", "Moira", "Symmetra", "Zenyatta"
        ],    
    "pokemon1" : [
        "Ash", "Misty", "Brock", "Pikachu", "Charmander",
        "Oak", "Pokedex", "Kanto", "Pokeball", "Squirtle",
        "Bulbasaur", "Eevee", "Gengar", "Jigglypuff", "Ghastly",
        "Gyrados", "Magikarp", "Slowpoke", "Rocket", "Meowth"
        ],
    "polytopia" : [
        "Bardur", "Oumaji", "Luxidor", "Vengir", "Imperius",
        "Kickoo", "Hoodrick", "Zebasi", "AiMo", "Aquarion",
        "Quetzali", "Climbing", "Organization", "Hunting",
        "Riding", "Fishing", "Archery", "Smithery", "Farming",
        "Meditation", "Shields", "Whaling", "Navigation", "XinXi"
        ],
    "programming1" : [
        "unsigned", "signed", "competitive", "pointer", "reference",
        "instance", "class", "long", "integer", "floating-point", "fenwick-tree",
        "segment-tree", "decomposition", "optimizations", "assembly", "pascal", "fermat",
        "hyperoperation", "exponentiation", "tetration", "pentation", "hexation", "erlang",
        "turing", "microprocessor", "microcontroller", "typedef", "inheritance", "encapsulation"
        ],
    "programming2" : [
        "programming", "scheduler", "diffie-hellman", "djikstra", "eratosthenes", "segmentation",
        "line-sweep", "kruskal", "attribute", "variable", "constant", "function", "method",
        "parameter", "return", "string", "race-condition", "multithreading", "judge", "template",
        "bit", "nibble", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte", "petabyte",
        "exabyte", "zettabyte", "yottabyte"
        ],
    "rickandmorty" : [
        "Rick", "Morty", "Summer", "Beth", "Jerry",
        "MrPoopybutthole", "Birdperson", "Squanchy", "Smith", "Unity",
        "Gazorpian", "Chirs", "KingFlippyNips", "Snowball",
        "Ethan", "Nancy", "Toby", "Frank", "Meeseeks"
        ],
    "voltron" : [
        "Paladin", "Lion", "Voltron", "Zarkon", "Lotor",
        "Pidge", "Hunk", "Shiro", "Keith", "Lance",
        "Allura", "Coran", "Haggar", "Narti", "Regris",
        "Mormora", "Garrison", "Galra", "Kerberos", "Quintessence"
        ]
    }
