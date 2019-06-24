import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ".")

global tasks
tasks = []

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_connect():
    print("Bot has connected to Discord servers!")

@client.event
async def on_disconnect():
    print("Bot has lost connection to Discord servers!")

@client.event
async def on_message(msg):
    msgList = list(msg)
    if msgList[0] == '+':
        if msg.startswith('+fanart'):
            pass
        elif msg.startswith('+emoji'):
            pass
        elif msg.startswith('+merch'):
            pass
        elif msg.startswith('+story'):
            pass
        

client.run("TOKEN")
