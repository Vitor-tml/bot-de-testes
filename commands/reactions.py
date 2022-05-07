from discord.ext import commands


class Reactions(commands.Cog):
    """Trabalha com reações"""
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == "❤️":
            role = user.guild.get_role(972175305638821969)
            await user.add_roles(role)
        elif reaction.emoji == "👍":
            role = user.guild.get_role(972175408302796842)
            await user.add_roles(role)


def setup(bot):
    bot.add_cog(Reactions(bot))
