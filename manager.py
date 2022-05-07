from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound

class Manager(commands.Cog):
    """Gerencia o bot"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Online!")


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if "teste" in message.content:
            await message.channel.send("Tudo certo!")


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Favor mandar todos os argumentos. Digite >help para visualizar os comandos!")
        elif isinstance(error, CommandNotFound):
            await ctx.send("O comando não existe. Digite >help para visualizar os comandos!")
        else:
            raise error

def setup(bot):
    bot.add_cog(Manager(bot))