import discord
from discord.ext import commands
from botUtils.utils import con

log = con()

class ReloadCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(cog)
            log.log(f' Unloaded extension {cog}.')
            self.bot.load_extension(cog)
            log.log(f' Loaded extension {cog}.')
            log.log(f'Successfully reloaded extension {cog}.')
        except Exception as e:
            embed = discord.Embed(title='Error', description=str(e), color=0xff0000)
            await ctx.send(embed=embed)
            log.log(f"Couldn't reload extension {cog}: {e}")
        else:
            color=0xB1FBFF
            embed = discord.Embed(title='Success', description=f'Successfully reloaded extension {cog}', color=color)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ReloadCMD(bot))