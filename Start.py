import discord


@bot.event
async def on_ready():
    print('Kardien Start')


access_token = os.environ["BOT_TOKEN"]    
bot.run(access_token)
