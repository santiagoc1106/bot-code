import discord
from dotenv import load_dotenv
from discord.ext import commands
import os
import requests
import json

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "$", intents = intents)

@bot.command()
async def joke(ctx):
    await ctx.send("Knock knock")



bot.run(TOKEN)