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

    if message.content == 'cool':
        await message.add_reaction('\U0001F603')


@client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author} edit a message.\n'
        f'Before: {before.content}\n'
        f'After: {after.content}'
    )


@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')


client.run(os.getenv('DISCORD_API'))
