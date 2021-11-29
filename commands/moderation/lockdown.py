import asyncio
from configparser import ConfigParser
from datetime import datetime

import discord
from discord.ext import commands
from discord_components import *

parser = ConfigParser()
parser.read('config.ini')
try:
    logchannel = int(parser.get('CONFIG', 'log_channel'))
except Exception as e:
    print(f"Couldn't define logchannel: {e}")
    logchannel = None


class lockChannels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    async def lockdown(self, ctx, channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        memberRole = ctx.guild.get_role(904652471350222888)
        if logchannel is not None:
            logc = self.bot.get_channel(logchannel)
        else:
           logc = None

        if channel.overwrites[ctx.guild.default_role].send_messages is True or \
                channel.overwrites[ctx.guild.default_role].send_messages is None or \
                channel.overwrites[memberRole].send_messages is None or \
                channel.overwrites[memberRole].send_messages is True or \
                ctx.guild.default_role not in channel.overwrites or \
                memberRole not in channel.overwrites:
            tembed = discord.Embed(
                description=f'Mödchtest du wirklich {channel.mention} für User sperren?',
                color=0xB1FBFF, timestamp=datetime.utcnow())
            tembed.set_author(name=f'ChannelLockDown - Confirming', icon_url='https://i.ibb.co/2WQdHqj/Warning.png')
            tembed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            msg = await ctx.send(embed=tembed, components=[
                [
                    Button(style=ButtonStyle.green, label='Confirm', emoji="✅"),
                    Button(style=ButtonStyle.red, label='Cancel', emoji='❌')
                ],
            ],
                                 )
            try:
                res = await self.bot.wait_for("button_click", timeout=20)
            except asyncio.exceptions.TimeoutError:
                tembed = discord.Embed(
                    description='Du hast dich nicht rechtzeitig endschieden!\nDer Channel wurde **nicht** gesperrt!',
                    color=0xB1FBFF, timestamp=datetime.utcnow())
                tembed.set_author(name=f'ChannelLockDown - Timeout!', icon_url='https://i.ibb.co/xDWBGW3/Error.png')
                tembed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                await msg.edit(
                    embed=tembed,
                    components=[
                    ],
                )
                await asyncio.sleep(8)
                await ctx.message.delete()
                await msg.delete()
                return
            if res.component.label == 'Confirm':
                if ctx.author == res.user:
                    overwritesDefault = channel.overwrites[ctx.guild.default_role]
                    overwritesDefault.send_messages = False
                    overwritesMember = channel.overwrites[memberRole]
                    overwritesMember.send_messages = False
                    await channel.set_permissions(ctx.guild.default_role, overwrite=overwritesDefault)
                    await channel.set_permissions(memberRole, overwrite=overwritesMember)
                    if str(ctx.channel.id) != str(channel.id):
                        await channel.send(
                            "> Dieser Channel wurde von der **Adminstration** vorübergehend **gesperrt**!")
                    tembed = discord.Embed(
                        description=f'Du ({ctx.author.mention}) hast den Channel {channel.mention} für user gesperrt!',
                        color=0xB1FBFF, timestamp=datetime.utcnow())
                    tembed.set_author(name=f'ChannelLockDown - Confirmed', icon_url='https://i.ibb.co/104kpLk/Confrim.png')
                    tembed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                    await msg.edit(
                        embed=tembed,
                        components=[
                        ],
                    )
                    if logc is not None:
                        await logc.send(embed=tembed)
                    await asyncio.sleep(10)
                    await ctx.message.delete()
                    await msg.delete()
                    return
            elif res.component.label == 'Cancel':
                if ctx.author == res.user:
                    tembed = discord.Embed(
                        description='Du hast den sperr vorgang **abgebrochen**!\nDer Channel wurde **nicht** gesperrt!',
                        color=0xB1FBFF, timestamp=datetime.utcnow())
                    tembed.set_author(name=f'ChannelLockDown - Canceled', icon_url='https://i.ibb.co/xDWBGW3/Error.png')
                    tembed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                    await msg.edit(
                        embed=tembed,
                        components=[
                        ],
                    )
                    await asyncio.sleep(8)
                    await ctx.message.delete()
                    await msg.delete()
                    return
        else:
            tembed = discord.Embed(
                description=f'Mödchtest du wirklich {channel.mention} für User wieder **freigeben**?',
                color=0xB1FBFF, timestamp=datetime.utcnow())
            tembed.set_author(name=f'ChannelUnLock - Confirming', icon_url='https://i.ibb.co/2WQdHqj/Warning.png')
            tembed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            msg = await ctx.send(embed=tembed, components=[
                [
                    Button(style=ButtonStyle.green, label='Confirm', emoji="✅"),
                    Button(style=ButtonStyle.red, label='Cancel', emoji='❌')
                ],
            ],
                                 )
            try:
                res = await self.bot.wait_for("button_click", timeout=20)
            except asyncio.exceptions.TimeoutError:
                tembed = discord.Embed(
                    description='Du hast dich nicht rechtzeitig endschieden!\nDer Channel wurde **nicht** entsperrt!',
                    color=0xB1FBFF, timestamp=datetime.utcnow())
                tembed.set_author(name=f'ChannelUnLock - Timeout!', icon_url='https://i.ibb.co/xDWBGW3/Error.png')
                tembed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                await msg.edit(
                    embed=tembed,
                    components=[
                    ],
                )
                await asyncio.sleep(8)
                await ctx.message.delete()
                await msg.delete()
                return
            if res.component.label == 'Confirm':
                if ctx.author == res.user:
                    overwritesDefault = channel.overwrites[ctx.guild.default_role]
                    overwritesDefault.send_messages = None
                    overwritesMember = channel.overwrites[memberRole]
                    overwritesMember.send_messages = None
                    await channel.set_permissions(ctx.guild.default_role, overwrite=overwritesDefault)
                    await channel.set_permissions(memberRole, overwrite=overwritesMember)
                    if str(ctx.channel.id) != str(channel.id):
                        await channel.send(
                            "> Dieser Channel wurde von der **Adminstration** wieder **entsperrt**!")
                    tembed = discord.Embed(
                        description=f'Du ({ctx.author.mention}) hast den Channel {channel.mention} für user **freigegeben**!',
                        color=0xB1FBFF, timestamp=datetime.utcnow())
                    tembed.set_author(name=f'ChannelUnLock - Confirmed', icon_url='https://i.ibb.co/104kpLk/Confrim.png')
                    tembed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                    await msg.edit(
                        embed=tembed,
                        components=[
                        ],
                    )
                    if logc is not None:
                        await logc.send(embed=tembed)
                    await asyncio.sleep(10)
                    await ctx.message.delete()
                    await msg.delete()
                    return
            elif res.component.label == 'Cancel':
                if ctx.author == res.user:
                    tembed = discord.Embed(
                        description='Du hast den entsperr vorgang **abgebrochen**!\nDer Channel wurde **nicht** entsperrt!',
                        color=0xB1FBFF, timestamp=datetime.utcnow())
                    tembed.set_author(name=f'ChannelUnLock - Canceled', icon_url='https://i.ibb.co/xDWBGW3/Error.png')
                    tembed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                    await msg.edit(
                        embed=tembed,
                        components=[
                        ],
                    )
                    await asyncio.sleep(8)
                    await ctx.message.delete()
                    await msg.delete()
                    return


def setup(bot):
    bot.add_cog(lockChannels(bot))
