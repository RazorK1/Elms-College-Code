# Kyle Harris
# CIT 2100: AI
# Elms Discord Bot

import os
# python -m pip install -U discord.py python-dotenv (my arse)
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Insert AI here:
from openai import OpenAI

# Load environment variables
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

# THIS IS HOW IT INTERACTS WITH THE ACTUAL DISCORD APP
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Discord intents
intents = discord.Intents.default()
intents.message_content = True

# Beep Boop
bot = commands.Bot(command_prefix="!", intents=intents)

##########################################################################
# Bot Ready Event

@bot.event
async def on_ready():
    print(f"✅ {bot.user} is online and ready!")
    await bot.change_presence(activity=discord.Game(name="with Python!"))

##########################################################################
# AI Chat Handler

@bot.event
async def on_message(message):

    # Prevent bot replying to itself?????????????????
    if message.author == bot.user:
        return

    # Allow commands to work
    # (The AI will still respond to the commands as well)
    if message.content.startswith("!"):
        await bot.process_commands(message)
        return

    # The AI isn't supposed to respond to every message, but it does anyway! 
    if bot.user not in message.mentions:
        return

    async with message.channel.typing():

        response = ai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful Discord assistant."},
                {"role": "user", "content": message.content}
            ]
        )

    reply = response.choices[0].message.content

    # Discord message limit
    await message.channel.send(reply[:6000]) # Originally 2000, increase as needed

    await bot.process_commands(message)

##########################################################################
# Commands

@bot.command()
async def hello(ctx):
    """Says hello"""
    await ctx.send(f"Hello {ctx.author.mention}! 👋")

@bot.command()
async def ping(ctx):
    """Check bot latency"""
    await ctx.send(f"Pong! 🏓 Latency: {round(bot.latency * 1000)}ms")

##########################################################################

bot.run(TOKEN)

###################################################################################################################
# Powershell command needed to initialize:
# C:\Users\Karabakh\AppData\Local\Programs\Python\Python313\python.exe bot.py
# 
# python bot.py
