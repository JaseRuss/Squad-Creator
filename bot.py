# bot.py
# used https://medium.com/bad-programming/making-a-cool-discord-bot-in-python-3-e6773add3c48 as a guide
# deploy info https://medium.com/davao-js/v2-tutorial-deploy-your-discord-bot-to-heroku-part-2-9a37572d5de4


# bot.py
import discord # For discord
from discord.ext import commands # For discord
import logging # For logging
from pathlib import Path # For paths
import json
import os
import random

cwd = Path(__file__).parents[0]
cwd = str(cwd)

# Defining a few things
secret_file = json.load(open(cwd+'/bot_config/secrets.json'))
bot = commands.Bot(command_prefix='-', case_insensitive=True)
bot.config_token = secret_file['token'] # Using local token stored in botconfig\secrets.json
#bot.config_token = os.environ['DISCORD_TOKEN'] # Using the token code stored on server

#Simple Echo Command - Just parrots back whatever you pass to it
@bot.command()
async def echo(ctx, *, message=None):
    """
    A simple command that repeats the users input back to them.
    """
    message = message or "Please provide the message to be repeated." # this cactched empty argument message. either message is true or "text"
    await ctx.message.delete() # Deletes the message to the bot - Presumibly to keep it tidy Might delete this
    await ctx.send(message) #Sends message to Discord

@bot.command()
async def VL(ctx, *, message=None): # Voice List
    await ctx.message.delete() # deletes message from user first to keep it a bit tidyer
    count = 0
    VCL = channel_names()
    message = ""

    for x in VCL:
        message =  "\n" + message + "Channel ID : " + str(count) +"\n" +" Channel Name :"+ x.name +"\n" 
        count+=1
    await ctx.send(message) #Sends message to Discord


@bot.command()
#BG - command lets you create a list of squads from a Voice Channel (argument )
async def bg(ctx, *, message=None , squadsize=3 ):
    await ctx.message.delete() # deletes message from user first to keep it a bit tidyer
    Users = []
    if message:
        squadno = 1 # Defines the initial Squad number
        #squadsize = 3 # Defines the number of players in a squad
        count = 0 # counter for loop
        VCL = channel_names() 
        Users = (VCL[int(message)].members)
        if (len(Users) > 0):
            random.shuffle(Users)  # shuffles the user list around to create random teams
            while (len(Users) > 0):
                message = message + "\n Squad "+str(squadno) + "\n"
                
                while (count < squadsize):
                    try:
                        message = message + str(Users[-1].nick) +"\n"
                        Users.pop()
                    except:
                        message = message + '\n'
                    count +=1
                else:
                    squadno +=1
                    count = 0
            message = message + "Assignments Complete, Good hunting - make big AT proud"
        else:
            message = "You got no fans, cried the toothless yokel - Voice channel emtpy"
    else:
        message = "Need a voice channel ID please e.g -bg 0 \n To see all the Voice channels and their ID's use -vl"
    print (message)
    #await ctx.send(message) #Sends message to Discord


@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot)) 
    #VCL = channel_names()
    #Users = (VCL[0].members)
    #print(Users[0].nick)

#Creates a list of all voice channel names \o/
def channel_names ():
    voice_channel_list = []
    for guild in bot.guilds:
        for channel in guild.voice_channels:
         voice_channel_list.append(channel)
    return (voice_channel_list) 

bot.run(bot.config_token)