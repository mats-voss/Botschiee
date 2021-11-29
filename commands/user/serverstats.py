import discord
from discord.ext import commands
from botUtils.utils import hypixel, utils
from botUtils.embeds import Embeds
import datetime


class ServerStats(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['lb'])
    async def leaderboard(self, ctx, game: str = None, *, typevar: str = None):
        if ctx.guild is not None:
            me = ctx.guild.get_member(self.bot.user.id)
            perms = ctx.channel.permissions_for(me)
            if perms.send_messages:
                if not perms.embed_links:
                    await ctx.send(
                        "Error: Cannot send embeds in this channel. Please contact a server administrator to fix this issue.")
                    return
                if perms.embed_links:
                    pass
            if not perms.send_messages:
                return
        if game is None:
            embed = discord.Embed(title="Error", description="""Please provide a game.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        if typevar is None:
            embed = discord.Embed(title="Error", description="""Please provide a leaderboard.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        if not typevar.lower().startswith('overall') and not typevar.lower().startswith(
                'monthly') and not typevar.lower().startswith('weekly') and not typevar.lower().startswith('daily'):
            t = "Overall " + typevar
            typevar = t
        if typevar.lower() == 'overall level':
            typevar = "Current Level"
        # send request
        data = await hypixel.leaderboards()
        # errors
        if data['success'] == False:
            embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        # it worked!
        elif data['success'] == True:
            game = game.upper()
            typevar = typevar.lower()
            leaders = None
            title = None
            for lb in data['leaderboards']:
                if lb == game.upper():
                    for reekid in data['leaderboards'][lb]:
                        titl = reekid['prefix'] + " " + reekid['title']
                        if titl.lower() == typevar:
                            title = reekid['prefix'] + " " + reekid['title']
                            leaders = reekid['leaders']
                            break
            if leaders is None:
                embed = discord.Embed(title='Error', description='Invalid leaderboard.', color=0xff0000)
                await ctx.send(embed=embed)
                return
            msg = ''
            num = 0
            async with ctx.channel.typing():
                for uid in leaders:
                    uid = uid.replace('-', '')
                    name = await hypixel.getname(uid)
                    if name is None:
                        name = 'N/A'
                    num += 1
                    msg += f"{num}: {name}\n"
                color = 0xB1FBFF
                embed = discord.Embed(title=f'{game.lower().capitalize()}: {title} leaderboard', description=msg,
                                      color=color)
                embed.set_footer(text='Unofficial Hypixel Discord Bot')
                await ctx.send(embed=embed)

    @commands.command(aliases=['players', 'count', 'pc'])
    async def playercount(self, ctx):
        perms = None
        if ctx.guild is not None:
            me = ctx.guild.get_member(self.bot.user.id)
            perms = ctx.channel.permissions_for(me)
            if perms.send_messages:
                if not perms.embed_links:
                    await ctx.send(
                        "Error: Cannot send embeds in this channel. Please contact a server administrator to fix this issue.")
                    return
                if perms.embed_links:
                    if not perms.add_reactions:
                        embed = discord.Embed(title="Error",
                                              description="Cannot add reactions in this channel. Please contact a server administrator to fix this issue.",
                                              color=0xff0000)
                        await ctx.send(embed=embed)
                        return
                    if perms.add_reactions:
                        pass
            if not perms.send_messages:
                return
        data = await hypixel.counts()
        if data['success'] == True:
            embeds, paginator = await Embeds().PlayerCount().generate(ctx, data, perms,
                                                                      await self.bot.fetch_user(834762194629034035))
            await paginator.run(embeds)
        else:
            embed = discord.Embed(title="Error",
                                  description="""Couldn't retrieve Hypixel player counts. Please try again later.""",
                                  color=0xff0000)
            await ctx.send(embed=embed)
            return

    @commands.command(aliases=['g'])
    async def guild(self, ctx, *, guildname: str = None):
        if ctx.guild is not None:
            me = ctx.guild.get_member(self.bot.user.id)
            perms = ctx.channel.permissions_for(me)
            if perms.send_messages:
                if not perms.embed_links:
                    await ctx.send(
                        "Error: Cannot send embeds in this channel. Please contact a server administrator to fix this issue.")
                    return
                if perms.embed_links:
                    pass
            if not perms.send_messages:
                return
        if guildname is None:
            embed = discord.Embed(title="Error", description='Please provide a guild to search for.', color=0xff0000)
            await ctx.send(embed=embed)
            return
        gnamesearch = guildname.replace(' ', '%20')
        try:
            data = await hypixel.guild(gnamesearch)
        except ValueError:
            embed = discord.Embed(title="Error", description="""The guild """ + guildname + ' does not exist.',
                                  color=0xff0000)
            await ctx.send(embed=embed)
            return
        try:
            glevel = utils.guildlevel(xp=data['guild']['exp'])
        except:
            glevel = 'N/A'
        try:
            gname = data['guild']['name']
        except:
            gname = 'N/A'
        try:
            time = datetime.fromtimestamp(data['guild']['created'] / 1000.0)
            date = time.strftime("%m/%d/%Y")
            minute = time.strftime("%M")
            if int(time.strftime('%H')) == 12:
                ampm = 'PM'
                hour = time.strftime('%H')
            elif int(time.strftime('%H')) > 12:
                hour = int(time.strftime('%H')) - 12
                ampm = 'PM'
            elif int(time.strftime('%H')) < 12:
                ampm = 'AM'
                hour = time.strftime('%H')
            else:  # this should never happen
                hour = None
                ampm = None
            created = str(date) + ' at ' + str(hour) + ':' + str(minute) + ' ' + ampm + ', EST'
        except:
            created = 'N/A'
        try:
            desc = data['guild']['description']
        except:
            desc = 'N/A'
        try:
            tag = data['guild']['tag']
        except:
            tag = 'N/A'
        try:
            mbrs = len(data['guild']['members'])
        except:
            mbrs = 'N/A'
        try:
            gmuuid = data['guild']['members'][0]['uuid']
            gm = await hypixel.getname(gmuuid)
            if gm is None:
                gm = 'N/A'
        except:
            gm = 'N/A'
        color = 0xB1FBFF
        embed = discord.Embed(title='Guild Info', color=color)
        embed.add_field(name="Guild Name", value=str(gname), inline=True)
        embed.add_field(name="Guild Manager", value=str(gm), inline=True)
        embed.add_field(name="Members", value=str(utils.comma(mbrs)), inline=True)
        embed.add_field(name="Created On", value=str(created), inline=True)
        embed.add_field(name="Guild Level", value=str(utils.comma(glevel)), inline=True)
        embed.add_field(name="Guild Description", value=str(desc), inline=True)
        embed.add_field(name="Guild Tag", value=str(tag), inline=True)
        embed.set_footer(text='Unofficial Hypixel Discord Bot')
        await ctx.send(embed=embed)

    @commands.command(aliases=['wd'])
    async def watchdog(self, ctx):
        perms = None
        if ctx.guild is not None:
            me = ctx.guild.get_member(self.bot.user.id)
            perms = ctx.channel.permissions_for(me)
            if perms.send_messages:
                if not perms.embed_links:
                    await ctx.send(
                        "Error: Cannot send embeds in this channel. Please contact a server administrator to fix this issue.")
                    return
                if perms.embed_links:
                    pass
            if not perms.send_messages:
                return
        data = await hypixel.watchdog()
        if data['success'] == True:
            try:
                wdtotal = data['watchdog_total']
            except:
                wdtotal = 'N/A'
            try:
                stafftotal = data['staff_total']
            except:
                stafftotal = 'N/A'
            color = 0xB1FBFF
            embed = discord.Embed(title="Hypixel Watchdog Statistics", color=color)
            embed.add_field(name="Watchdog Bans", value=str(utils.comma(wdtotal)))
            embed.add_field(name="Staff Bans", value=str(utils.comma(stafftotal)))
            try:
                embed.add_field(name="Total Bans", value=str(utils.comma(wdtotal + stafftotal)))
            except:
                embed.add_field(name="Total Bans", value='N/A')
            embed.set_footer(text='Unofficial Hypixel Discord Bot')
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(ServerStats(bot))
