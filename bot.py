# bot.py
# used https://medium.com/bad-programming/making-a-cool-discord-bot-in-python-3-e6773add3c48 as a guide
# deploy info https://medium.com/davao-js/v2-tutorial-deploy-your-discord-bot-to-heroku-part-2-9a37572d5de4
# token = 'Njk1OTIzOTg5MjgwODQ5OTQw.Xoh7ug.oDTXpc2pAJIZuAz-JSpqaqE5aE4'

# bot.py
import discord # For discord
from discord.ext import commands # For discord
import logging # For logging
from pathlib import Path # For paths
import json

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")

# Defining a few things
secret_file = json.load(open(cwd+'/bot_config/secrets.json'))
bot = commands.Bot(command_prefix='-', case_insensitive=True)
client = discord.Client()


@client.event
async def on_ready(*args, **kwargs):
    print("We have logged in as {0.user}".format(client))
    print("Channels", list(client.get_all_channels()))
    print("Members", list(client.get_all_members()))


@client.event
async def on_connect(*args, **kwargs):
    print("Guilds", client.guilds)
    print("Voice Clients", client.voice_clients)
    print("Channels", list(client.get_all_channels()))
    print("Members", list(client.get_all_members()))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

    if message.content.startswith("!ch"):
        await message.channel.send(
            f"Username: {message.author.name}\nID: {message.author.id}"
        )

    if message.content.startswith("!squad"):
        client.VoiceChannel
        await message.channel.send("Calculating Squads")


client.run("Njk1OTIzOTg5MjgwODQ5OTQw.Xoh7ug.oDTXpc2pAJIZuAz-JSpqaqE5aE4")
