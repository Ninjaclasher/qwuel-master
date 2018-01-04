#  TODO GAMEMODES
#  HARDCORE
#  TOURNEY

import random
from discord import *
from pprint import pprint
from collections import namedtuple
import string

import QwuelGame as qGame
import QwuelMode as qMode
import QwuelPlayer as qPlayer

bot = Client()

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")

games = {}

async def process_command(send, message, command):
    try:
        game = games[message.channel]
    except KeyError:
        game = games[message.channel] = qGame.QwuelGame(send,message.channel)
    if command[0] == "start":
        if len(command) == 3:
            await game.start(message.author, command[1], int(command[2]))
        elif len(command) == 2:
            await game.start(message.author, 'classic', int(command[1]))
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


COMMAND_PREFIX = "]"

@bot.event
async def on_message(message):
    if message.type == MessageType.default and message.content.startswith(COMMAND_PREFIX):
        command = message.content[len(COMMAND_PREFIX):].strip().split(" ")
        await process_command(bot.send_message,message,command)

bot.run("token")
