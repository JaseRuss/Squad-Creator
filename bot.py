# bot.py
# used https://medium.com/bad-programming/making-a-cool-discord-bot-in-python-3-e6773add3c48 as a guide
# deploy info https://medium.com/davao-js/v2-tutorial-deploy-your-discord-bot-to-heroku-part-2-9a37572d5de4
# token = 'Njk1OTIzOTg5MjgwODQ5OTQw.Xoh7ug.oDTXpc2pAJIZuAz-JSpqaqE5aE4'

# bot.py
import discord

client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    print(message)
    print(message.author)
    print(client.user)
    print(message.content)
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

    if message.content.startswith("!squad"):
        await message.channel.send("Calculating Squads")

client.run("Njk1OTIzOTg5MjgwODQ5OTQw.Xoh7ug.oDTXpc2pAJIZuAz-JSpqaqE5aE4")
