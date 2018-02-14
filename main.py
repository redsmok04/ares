# v0.0.1 chat system

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random

Client = discord.Client()
token = "NDEyMjgzNTcxNTU4OTQwNjcy.DWS8Xg.gJGhesk71w2tdM-YsrfNMhePDEM"
client = commands.Bot(command_prefix='Ares')
aresid = '254512019116523522'
@client.event
async def on_ready():
    print('Bot is Ready! v0.0.1')
    print('I am running on ' + client.user.name)
    
@client.event
async def on_message(message):
    if message.content.upper().startswith('I LOVE YOU ARES'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> :heart:" % (userID))
        
    if message.content.lower().startswith ("aresplay") and message.author.id == aresid:
        game = message.content[9:]
        await client.change_presence(game=discord.Game(name=game))
        
    if message.content.upper().startswith('ARES YOU ARE FIRED'):
        await client.send_message(message.channel,"(╯°□°）╯︵ ┻━┻")

    if message.content.startswith('You are a Nazi 卐, my good friend.'):
        await client.send_message(message.channel,"This is out of control!")

    if message.content.startswith('You are a Jew,just like your parents which died painfully in my gas chambers...'):
        await client.send_message(message.channel,"Some one stop this please?")

    if message.content.startswith('You are a fucking Soviet ☭,I hope your race suffers in hell.'):
        await client.send_message(message.channel,"someone need to do something about this!!")
        
    if message.content.upper().startswith('ARES FUCK YOU'):
        await client.delete_message(message)

    if message.content.upper().startswith('ARES YOU ARE IN'):
        await client.send_message(message.channel,"┬─┬ ノ( ゜-゜ノ)")

    if message.content.upper().startswith('GIVE ME THE LIST OF THE SERVER ARES'):
        x = message.server.members
        for member in x:
            await client.send_message(message.channel, member)

    if message.content.upper().startswith('ARESSAY'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))


    if message.content.upper().startswith('ARESREAD'):
        if '413088579019866125' in (role.id for role in message.author.roles):
            args = message.content.split(" ")

            await client.send_message(message.channel, "%s" % (" ".join(args[1:])),tts=True)
        else:
            await client.send_message(message.channel, "No permission :frowning: ")

    if message.content.upper().startswith('ARES AM I ADMIN'):
        if '404272973311115265' in (role.id for role in message.author.roles):
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> You are Admin :poop:" % (userID))

        else:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> You are not Admin :frowning:" % (userID))

    if message.content.upper().startswith('ARES AM I PART OF TOOLKIT FOR YOU'):
        if '404272973311115265' in (role.id for role in message.author.roles):
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> You are :stuck_out_tongue_closed_eyes: " % (userID))

        else:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> You are not :frowning:" % (userID))
    if message.content.upper().startswith('ARESTELLME'):
        await client.send_message(message.channel, random.choice(["It is certain",
                                                                  "It is decidedly so",
                                                                  "Without a doubt",
                                                                  "Yes, definitely",
                                                                  "You may rely on it",
                                                                  "As I see it, yes",
                                                                  "Most likely",
                                                                  "Outlook good",
                                                                  "Yes :8ball:",
                                                                  "Signs point to yes",
                                                                  "Reply hazy try again",
                                                                  "Ask again later",
                                                                  "Better not tell you now",
                                                                  "Cannot predict now",
                                                                  "Concentrate and ask again",
                                                                  "Don't count on it",
                                                                  "My reply is no",
                                                                  "My sources say no",
                                                                  "Outlook not so good",
                                                                  "Very doubtful"]))
    if message.content.upper().startswith('ARESNUKE'):
        tmp = await client.send_message(message.channel, 'Clearing messages...:smiling_imp:')
        async for msg in client.logs_from(message.channel):
            await client.delete_message(msg)

    if message.content.upper().startswith('ARESCOINFLIP'):
        choice = random.randint(1,2)
        if choice == 1:
            await client.send_message(message.channel, 'Heads!')
        if choice == 2:
            await client.send_message(message.channel, 'Tails!')

    if message.content.upper().startswith('ARESROLLADICE'):
        choice1 = random.randint(1,6)
        if choice1 == 1:
            await client.send_message(message.channel, 'You rolled 1!')
        if choice1 == 2:
            await client.send_message(message.channel, 'You rolled 2!')
        if choice1 == 3:
            await client.send_message(message.channel, 'You rolled 3!')
        if choice1 == 4:
            await client.send_message(message.channel, 'You rolled 4!')
        if choice1 == 5:
            await client.send_message(message.channel, 'You rolled 5!')
        if choice1 == 6:
            await client.send_message(message.channel, 'You rolled 6!')
client.run(token)
