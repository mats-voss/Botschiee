import random
from typing import Optional

import discord
from discord import Member
from discord.ext import commands


class ServerUtils(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(ChannelID)
        if int(member.guild.id) == ChannelID:
            await channel.send(
                f'**{member.name}** ist dem Discord Server beigetreten!\nAktuelle Mitgliederzahl: **{member.guild.member_count}**')

    @commands.command(aliases=['cs'])
    @commands.bot_has_guild_permissions(manage_channels=True)
    async def channelstats(self, ctx):
        channel = ctx.channel
        embed = discord.Embed(title=f"Stats for **{channel.name}**", description=f"{'Category: {}'.format(channel.category.name) if channel.category else 'Der Channel ist in keiner Kategorie'}", color=0xB1FBFF)
        embed.add_field(name="Channel Guild", value=ctx.guild.name, inline=False)
        embed.add_field(name="Channel Id", value=channel.id, inline=False)
        embed.add_field(name="Channel Topic", value=f"{channel.topic if channel.topic else 'No topic.'}", inline=False)
        embed.add_field(name="Channel Position", value=channel.position, inline=False)
        embed.add_field(name="Channel Slowmode Delay", value=channel.slowmode_delay, inline=False)
        embed.add_field(name="Channel is nsfw?", value=channel.is_nsfw(), inline=False)
        embed.add_field(name="Channel is news?", value=channel.is_news(), inline=False)
        embed.add_field(name="Channel Creation Time", value=channel.created_at, inline=False)
        embed.add_field(name="Channel Permissions Synced", value=channel.permissions_synced, inline=False)
        embed.add_field(name="Channel Hash", value=hash(channel), inline=False)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(ServerUtils(bot))
