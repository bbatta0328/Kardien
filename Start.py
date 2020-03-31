import discord
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

bot.run('Njk0NDkxMDQ5OTMzOTMwNjA3.XoMcBg.-CE89bvk4O_eUhHTzkzjHkO2D9Y')
