import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up intents so the bot can read messages
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ {bot.user} is online and ready!')
    # Optional: change status
    await bot.change_presence(activity=discord.Game(name="with Python!"))

@bot.command()
async def hello(ctx):
    """Says hello!"""
    await ctx.send(f'Hello {ctx.author.mention}! 👋')

@bot.command()
async def ping(ctx):
    """Check bot latency"""
    await ctx.send(f'Pong! 🏓 Latency: {round(bot.latency * 1000)}ms')

# Add more commands here later!

bot.run(TOKEN)
