import discord
from discord.ext import commands
import os

TOKEN = os.getenv('token')
GUILD_NAME = os.getenv('guild_name')
ROLE_NAME = os.getenv('role_name')

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD_NAME)
    role = discord.utils.get(guild.roles, name=ROLE_NAME)
    
    if guild is None:
        print(f'Guild "{GUILD_NAME}" not found.')
        await bot.close()
        return
    elif role is None:
        print(f'Role "{ROLE_NAME}" not found in guild "{GUILD_NAME}".')
        await bot.close()
        return

    for member in guild.members:
        if role not in member.roles:
            try:
                await member.add_roles(role)
                print(f'Assigned role to {member.display_name}')
            except Exception as e:
                print(f'Failed to assign role to {member.display_name}: {e}')
    
    await bot.close()
bot.run(TOKEN)

    