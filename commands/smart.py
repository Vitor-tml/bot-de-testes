from discord.ext import commands


class Smart(commands.Cog):
    """Comando de interação complexa"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="calcular", help="Dá o resultado de uma expressão")
    async def calculate_expression(self, ctx, *expression):
        expression = "".join(expression)
        response = eval(expression)

        await ctx.send("A resposta é: " + str(response))

def setup(bot):
    bot.add_cog(Smart(bot))
