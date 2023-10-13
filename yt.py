import discord
from discord.ext import commands,tasks
import os
from dotenv import load_dotenv
import youtube_dl


load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = ".", intents = intents)

