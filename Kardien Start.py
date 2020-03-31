import discord
import os
import asyncio
from discord.ext import commands
from discord.ext.commands import bot

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Kardien Start')

@bot.command()
async def ip(ctx):
    await ctx.send('Kardien.kro.kr')

access_token = os.environ["BOT_TOKEN"]    
bot.run(access_token)
