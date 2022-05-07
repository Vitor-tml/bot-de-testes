from decouple import config
from discord.ext import commands

bot = commands.Bot(">")

bot.load_extension("manager")
bot.load_extension("commands.talks")
bot.load_extension("tasks.dates")
bot.load_extension("commands.smart")
bot.load_extension("commands.cryptos")
bot.load_extension("commands.reactions")
bot.load_extension("commands.images")

TOKEN = config("TOKEN")
bot.run(TOKEN)

    