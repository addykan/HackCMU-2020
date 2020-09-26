# bot.py
import os

# import discord
# from dotenv import load_dotenv

# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')



# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')

#     for guild in client.guilds:
#         if guild.name == GUILD:
#             break

#     print(
#         f'{client.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})\n'
#     )

#     members = '\n - '.join([member.name for member in guild.members])
#     print(f'Guild Members:\n - {members}')

# client.run(TOKEN)

from discord.ext import commands
from dotenv import load_dotenv
import random
from hackcmu20googlenews import *
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

bot = commands.Bot(command_prefix='!')

@bot.command(name='news')
async def getNews(ctx, arg):
    query = arg
    response = getArticles(query)
    if len(response) == 0:
        await ctx.send('No news found.')
    else:
        await ctx.send(response)

@bot.command(name='pythonbot')
async def python_bot(ctx):
    python_URL = [
        'https://praw.readthedocs.io/en/latest/',
        'https://realpython.com/how-to-make-a-discord-bot-python/',
        (
            'https://www.reddit.com/dev/api/oauth#GET_comments'
        ),
    ]

    response = random.choice(python_URL)
    await ctx.send(response)

# https://stackoverflow.com/questions/52348148/delete-messages-with-python-discord-bot
@bot.command(name='purge')
async def purge(ctx, limit: int = 100, *, matches: str = None):
    """Purge all messages, optionally from ``user``
    or contains ``matches``."""
    # logger.info('purge', extra={'ctx': ctx})
    def check_msg(msg):
        if msg.id == ctx.message.id:
            return True
        # if user is not None:
        #     if msg.author.id != user.id:
        #         return False
        if matches is not None:
            if matches not in msg.content:
                return False
        return True
    deleted = await ctx.channel.purge(limit=limit+1, check=check_msg)
    deletedMessage = f'Purged {len(deleted) - 1} messages!'
    msg = await ctx.send(deletedMessage)
    await a.sleep(2)
    await msg.delete()

@bot.command(name = 'spotify')
async def searchSpotify(ctx, arg):
    artistName = arg
    response = artistSearch(artistName)
    if len(response) == 0:
        await ctx.send('No artists found.')
    else:
        await ctx.send(response)

bot.run(TOKEN)
