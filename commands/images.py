from discord.ext import commands
import discord
import random

class Images(commands.Cog):
    """Comandos com imagens"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="foto", help="Chama o Faustão para de dar uma foto.")
    async def get_random_image(self, ctx):
        url_image = "https://picsum.photos/" + str(random.randrange(100, 500)) + "/" + str(random.randrange(250, 650))

        embeddd = discord.Embed(
            title = "Imagem: ",
            description = "Imagem Aleatória",
            color = 0x0000FF
        )

        embeddd.set_author(name="Faustão", icon_url="https://observatoriodatv.uol.com.br/wp-content/uploads/2022/01/Faustao.jpg")
        embeddd.set_footer(text="Eu mesmo", icon_url=self.bot.user.avatar_url)
        embeddd.set_image(url=url_image)
        embeddd.add_field(name="API", value="Api de imagens")
        embeddd.add_field(name="API", value="Api de imagens")
        embeddd.add_field(name="Não inline", value="Sozinho", inline=False)

        await ctx.send(embed=embeddd)

def setup(bot):
    bot.add_cog(Images(bot))
