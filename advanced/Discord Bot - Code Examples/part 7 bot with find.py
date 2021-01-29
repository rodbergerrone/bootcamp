# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
guild = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    GUILD = discord.utils.find(lambda g: g.name == guild, client.guilds)        
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{GUILD.name}(id: {GUILD.id})'
    )

client.run(token)