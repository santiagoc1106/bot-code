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

#class for joke
class JokeCaller(discord.ui.View):

    async def disable_all_items(self):
        for item in self.children:
            item.disabled = True

        await self.message.edit(view = self)

    async def on_timeout(self) -> None:
        await self.message.channel.send('Timeout')
        await self.disable_all_items()
    joke = None
    @discord.ui.button(label = "get joke", style = discord.ButtonStyle.success)
    async def jokijng(self, interaction: discord.Interaction, button : discord.ui.Button):
        await interaction.response.send_message("making joke...")

        joke_response = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt&type=single")
        joke = joke_response.text

        with open ("joke.json", "r") as f:
            data = json.load(f)

        data["joke"] = joke

        with open("joke.json", "w") as f:
            json.dump(data, f, indents = 2)

        self.stop 


@bot.command()
async def joke(ctx):
    view = JokeCaller(timeout = 30)
    message = await ctx.send("click button for joke", view = view)
    view.message = message

    await view.wait()
    await view.disable_all_items()

    with open("joke.json", "r") as f:
        data = json.load(f)

    await ctx.send("the joke is: ")
    await ctx.send(data["joke"])


bot.run(TOKEN)