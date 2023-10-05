import discord 
from dotenv import load_dotenv
from discord.ext import commands
import os
import json

#loading token
load_dotenv()
TOKEN = os.getenv('TOKEN')

#creating our bots
intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix = '!', intents = intents)

with open("num.json", "r") as f:
        data = json.load(f)

data["num"] = None

with open("num.json", "w") as f:
     json.dump(data, f, indent = 2)

cool_num = 0

@bot.command()
async def num_store(ctx, num):
    cool_num = num
    await ctx.send("NUM IS SAVED")

@bot.command()
async def print_num(ctx):
    await ctx.send(f"The num is {cool_num}")

bot.run(TOKEN)