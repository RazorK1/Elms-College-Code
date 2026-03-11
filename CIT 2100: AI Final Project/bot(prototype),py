# Kyle Harris
# CIT 2100: AI
# dis is a the prototype for the Elms Discord Bot.
# THIS IS NOT THE FINAL CODE!!!!!!

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Insert AI here:
from openai import OpenAI


intents = discord.Intents.default()
intents.message_content = True  # Needed if your bot reads message text

# Not needed apparently
#client = discord.Client(intents=intents) 

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

bot = commands.Bot(command_prefix='!', intents=intents)

##########################################################################
# "A Client is an object that represents a connection to Discord. A Client handles events, tracks state, and generally interacts with Discord APIs."
# "https://realpython.com/how-to-make-a-discord-bot-python/"
#
#client = discord.Client(intents=intents)
#
#@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
##########################################################################

@bot.event
async def on_ready():
    print(f'✅ {bot.user} is online and ready!')
    # Optional: change status

    await bot.change_presence(activity=discord.Game(name="with Python!"))

# Add that Microslop (AI) here.
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":message.content}]
    )

    await message.channel.send(response.choices[0].message.content)
    await bot.process_commands(message)


#Insert Commands below here:
@bot.command()
async def hello(ctx):
    """Says hello!"""
    await ctx.send(f'Hello {ctx.author.mention}! 👋')

@bot.command()
async def ping(ctx):
    """Check bot latency"""
    await ctx.send(f'Pong! 🏓 Latency: {round(bot.latency * 1000)}ms')

bot.run(TOKEN)

###################################################################################################################
# Powershell command needed to initialize:
# C:\Users\Karabakh\AppData\Local\Programs\Python\Python313\python.exe bot.py
# 
# python bot.py


###################################################################################################################
# Misc Code:
#
#user_input = input("Enter something: ")
#print("You entered: " + user_input)
#
#
