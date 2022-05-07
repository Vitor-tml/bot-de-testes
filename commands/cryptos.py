from discord.ext import commands
import requests

class Crypto(commands.Cog):
    """Trabalhando com moedas"""
    def __init__(self, bot):
        self.bot = bot
        
    ## https://api.binance.com/api/v3/ticker/price?symbol=BNBBTC
    @commands.command(name="binance", help="Retorna o valor do par. >binance \"moeda 1\" \"moeda 2\"")
    async def binance(self, ctx, coin, base):
        try:
            response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")

            data = response.json()
            price = data.get("price")

            if price:
                await ctx.send(f"O valor do par {coin}/{base} é {price}")
            else:
                await ctx.send(f"O par {coin}/{base} é inválido")
        except Exception as error:
            await ctx.sendo("Erro!")
            print("ERRO AQUI -> " + error)
            
def setup(bot):
    bot.add_cog(Crypto(bot))
