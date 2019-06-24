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

client.run("NTkyNTIwODE3NTc3ODIwMTcw.XRAilA.qCcBBuhJlpDgMWAtYwZe_a2T5bg")