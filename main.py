# Discord package install
import asyncio
from asyncio.tasks import wait
import discord
from discord.channel import VoiceChannel
import Definitions
import os
import dotenv
from discord.ext import tasks

# env request

dotenv.load_dotenv()

# Client setup

client = discord.Client()

# var defines


# Client async function


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    time_check.start()

# User input time check


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if '!time' in message.content.lower():
        await message.channel.send(Definitions.PDT())

# Check time async


@tasks.loop(minutes=10)
async def time_check():
    gen2 = Definitions.gen2_channel(client)
    pdt = Definitions.PDT()
    #print('I am looping')
    # Check PDT Time
    if (pdt >= (2000) or pdt <= (600)) and gen2.name == '「🔊」General│#2':
        await gen2.edit(name='「👿」Swamp')
        print('Changed to Swamp')
        print(pdt)
    else:
        await gen2.edit(name='「🔊」General│#2')
        print('Changed to Gen2')
        print(pdt)


@time_check.before_loop
async def before_task():
    await client.wait_until_ready()

client.run(os.getenv(key='TOKEN'))
