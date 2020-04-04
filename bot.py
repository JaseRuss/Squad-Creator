# bot.py 
# used https://medium.com/bad-programming/making-a-cool-discord-bot-in-python-3-e6773add3c48 as a guide
import discord


# command handler class

class CommandHandler:

    # constructor
    def __init__(self, client):
        self.client = client
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def command_handler(self, message):
        for command in self.commands:
            if message.content.startswith(command['trigger']):
                args = message.content.split(' ')
                if args[0] == command['trigger']:
                    args.pop(0)
                    if command['args_num'] == 0:
                        return self.client.send_message(message.channel,str(command['function'](message, self.client, args)))
                        break
                    else:
                        if len(args) >= command['args_num']:
                            return self.client.send_message(message.channel,str(command['function'](message, self.client, args)))
                            break
                        else:
                            return self.client.send_message(message.channel, 'command "{}" requires {} argument(s) "{}"'.format(command['trigger'], command['args_num'], ', '.join(command['args_name'])))
                            break
                else:
                    break


# create discord client
client = discord.Client()
token = 'Njk1OTIzOTg5MjgwODQ5OTQw.Xohm0Q.W7Hvla1J0gxJtBGrsphBeu4mPco'

# create the CommandHandler object and pass it the client
ch = CommandHandler(client)


# command's functions
## start commands command
def commands_command(message, client, args):
    try:
        count = 1
        coms = '**Commands List**\n'
        for command in ch.commands:
            coms += '{}.) {} : {}\n'.format(count, command['trigger'], command['description'])
            count += 1
        return coms
    except Exception as e:
        print(e)
ch.add_command({
    'trigger': '!commands',
    'function': commands_command,
    'args_num': 0,
    'args_name': [],
    'description': 'Prints a list of all the commands!'
})
## end commands command

## start Squad command
def Squad_function(message, client, args):
    try:
        return 'Hello {}, Argument One: {}'.format(message.author, args[0])
    except Exception as e:
        return e
ch.add_command({
    'trigger': '!Squad',
    'function': Squad_function,
    'args_num': 1,
    'args_name': ['Integer'],
    'description': 'Will output a Squad Size based on Argument from a defined Voice Chat Channel'
})
## end Squad command

#Start JoinChannel command#
def connect_(self, ctx, *, channel: discord.VoiceChannel = None):
        """Connect to voice.

        Parameters
        ------------
        channel: discord.VoiceChannel [Optional]
            The channel to connect to. If a channel is not specified, an attempt to join the voice channel you are in
            will be made.
        """
        try:
            await ctx.message.delete()
        except discord.HTTPException:
            pass

        if not channel:
            try:
                channel = ctx.author.voice.channel
            except AttributeError:
                raise NoChannel('No channel to join. Please either specify a valid channel or join one.')

        player = self.bot.wavelink.get_player(ctx.guild.id, cls=Player)

        if player.is_connected:
            if ctx.author.voice.channel == ctx.guild.me.voice.channel:
                return

        await player.connect(channel.id) 

		ch.add_command({
    'trigger': '!Join',
    'function': connect_,
    'args_num': 1,
    'args_name': ['String'],
    'description': 'Will make join the voice channel you are in'
})
#End Join Channel command


# bot is ready
@client.event
async def on_ready():
    try:
        print(client.user.name)
        print(client.user.id)

    except Exception as e:
        print(e)


# on new message
@client.event
async def on_message(message):
    
    # if the message is from the bot itself ignore it
    if message.author == client.user:
        pass
    else:
        
        # try to evaluate with the command handler
        try:
            await ch.command_handler(message)
            
        # message doesn't contain a command trigger
        except TypeError as e:
            pass
        
        # generic python error
        except Exception as e:
            print(e)


# start bot
client.run(token)
