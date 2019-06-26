import discord
from functions.py import discordify, original
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
async def on_message(message):
    msg = message.content
    # Splits message by spaces and characters
    msgChars = list(msg)
    msgList = msg.split()
    
    # Bot flag recognition and subsequent message comprehension if/else tree
    if msgChars[0] == '+':
        if msg.startswith('+fanart'):
            # Fan art options: original or discordify existing image
            if msgList[1] == 'og':
                original('fanart')
            elif msgList[1] == 'discordify':
                img = message.attachments
                img[0].save('image.jpeg')
                discordify('image.jpeg')
        elif msg.startswith('+emoji'):
            original('emoji')
        elif msg.startswith('+merch'):
            original('merch')
        

client.run("TOKEN")
