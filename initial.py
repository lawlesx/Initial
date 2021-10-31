import discord
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


client = discord.Client()


@client.event
async def on_ready():
    print('Online')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'hello':
        await message.channel.send('Hi I am Initial')


client.run(os.getenv('DISCORD_API'))
