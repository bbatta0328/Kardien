import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('KardienBot Online.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def ip(ctx):
    await ctx.send('Kardien.Kro.Kr')

access_token = os.environ("BOT_TOKEN")
client.run(access_token)
