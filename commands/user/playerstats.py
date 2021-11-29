import discord
from discord.ext import commands
from mojang import MojangAPI
from botUtils.utils import utils, hypixel
from botUtils.embeds import Embeds
import random


class PlayerStats(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['p'])
    async def player(self, ctx, username: str = None):
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
        if username is None:
            embed = discord.Embed(title="Error", description="""Please provide a username.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        uuid = MojangAPI.get_uuid(str(username))
        if uuid == '5d1f7b0fdceb472d9769b4e37f65db9f':
            embed = discord.Embed(title="Error", description="""That user does not exist.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        elif not uuid:
            embed = discord.Embed(title="Error", description="""That user does not exist.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        # send request
        data = await hypixel.player(uuid)
        # errors
        if not data['success']:
            embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        # it worked!
        elif data['success']:
            if data['player'] is None:
                embed = discord.Embed(title="Error",
                                      description="""That player has never joined the Hypixel Network.""",
                                      color=0xff0000)
                await ctx.send(embed=embed)
                return
        name = await hypixel.getname(uuid)
        embeds, paginator = await Embeds().Player().generate(ctx, name, data, perms, await self.bot.fetch_user(834762194629034035))
        await paginator.run(embeds)

    @commands.command(aliases=['bw'])
    async def bedwars(self, ctx, username: str = None):
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
        # verify if player exists
        if username is None:
            embed = discord.Embed(title="Error", description="""Please provide a username.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        try:
            uuid = MojangAPI.get_uuid(str(username))
        except:
            embed = discord.Embed(title="Error", description="""That user does not exist.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        if uuid == '5d1f7b0fdceb472d9769b4e37f65db9f':
            embed = discord.Embed(title="Error", description="""That user does not exist.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        elif not uuid:
            embed = discord.Embed(title="Error", description="""That user does not exist.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        # send request
        data = await hypixel.player(uuid)
        # errors
        if not data['success']:
            if data['cause'] == 'Malformed UUID':
                embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
            else:
                embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
        elif data['success']:
            if data['player'] is None:
                embed = discord.Embed(title="Error", description="""That user has never joined the Hypixel Network.""",
                                      color=0xff0000)
                await ctx.send(embed=embed)
                return
        name = await hypixel.getname(uuid)
        embeds, paginator = await Embeds().Bedwars().generate(ctx, name, data, perms, await self.bot.fetch_user(834762194629034035))
        await paginator.run(embeds)

    @commands.command(aliases=['sw'])
    async def skywars(self, ctx, username: str = None):
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
        if username is None:
            embed = discord.Embed(title="Error", description="""Please provide a username.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        uuid = MojangAPI.get_uuid(str(username))
        if uuid == '5d1f7b0fdceb472d9769b4e37f65db9f':
            embed = discord.Embed(title="Error", description="""That user does not exist.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        elif not uuid:
            embed = discord.Embed(title="Error", description="""That user does not exist.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        # send request
        data = await hypixel.player(uuid)
        # errors
        if not data['success']:
            embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
            await ctx.send(embed=embed)
            return
        # it worked!
        elif data['success']:
            if data['player'] is None:
                embed = discord.Embed(title="Error",
                                      description="""That player has never joined the Hypixel Network.""",
                                      color=0xff0000)
                await ctx.send(embed=embed)
                return
        name = await hypixel.getname(uuid)
        embeds, paginator = await Embeds().Skywars().generate(ctx, name, data, perms, await self.bot.fetch_user(834762194629034035))
        await paginator.run(embeds)


def setup(bot):
    bot.add_cog(PlayerStats(bot))
