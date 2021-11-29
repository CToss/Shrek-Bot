# Discord package install
import discord
from discord import voice_client
from discord import channel
from discord.channel import VoiceChannel
import Definitions
import os
import dotenv
from discord.ext import tasks, commands
import youtube_dl


# env request

dotenv.load_dotenv()

# Client setup

# Command prefix for any commands running
#client = commands.Bot(command_prefix='!')
client = discord.Client()
pfix = '!'


# Client async function

# time check status


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    time_check.start()


# message tester

@client.event
async def on_message(message):

    lower = message.content.lower()
    s = lower.lstrip(pfix)

    if message.author == client.user:
        return
    # !ping = message.content
    if message.content.startswith(pfix) and s == 'ping':
        await message.channel.send('Pong!')

# Voice Channel joiner

# @client.event
# async def on_message(message):

#     lower = message.content.lower()
#     s = lower.lstrip(pfix)

#     if message.author == client.user:
#         return
#     if message.content.startswith(pfix) and s == 'connect':
#         if
#             await message.channel.send('Pong!')


# check ping on server


# @client.command()
# async def ping(ctx):
#     await ctx.send(f"Pong! {round(client.latency * 1000)}ms.")


# Check time async


@tasks.loop(minutes=10)
async def time_check():
    gen2 = Definitions.gen2_channel(client)
    pdt = Definitions.PDT()
    #print('I am looping')
    # Check PDT Time
    if (pdt >= (1900) or pdt <= (600)) and gen2.name == '「🔊」General│#2':
        await gen2.edit(name='「👺」Swamp')
        print('Changed to Swamp')
        print(pdt)
    elif (pdt > 600 and pdt < 1900) and gen2.name == '「👺」Swamp':
        await gen2.edit(name='「🔊」General│#2')
        print('Changed to Gen2')
        print(pdt)


@time_check.before_loop
async def before_task():
    await client.wait_until_ready()


client.run(os.getenv(key='TOKEN'))
