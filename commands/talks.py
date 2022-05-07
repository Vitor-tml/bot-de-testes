from discord.ext import commands
import discord

class Talks(commands.Cog):
    """Conversa com o usuário"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="oi", help="Manda um \"Oi\" para o bot")
    async def send_hello(self, ctx):
        name = ctx.author.name
        resposta = "Olá, " + name
        await ctx.send(resposta)

    @commands.command(name="segredo", help="Te manda uma mensagem secreta!")
    async def secret(self, ctx):
        try:
            await ctx.author.send("Solteirx gatinhx?")
        except discord.errors.Forbidden:
            await ctx.send("Não posso te contar o segredo, habilite as mensagens de servidor!")

def setup(bot):
    bot.add_cog(Talks(bot))
 