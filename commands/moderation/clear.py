import asyncio
import textwrap
from configparser import ConfigParser
from datetime import datetime
import json

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


def is_not_pinned(mess):
    return not mess.pinned


class clear(commands.Cog, name='clear command'):
    def __init__(self, bot):
        self.bot = bot

    async def clearMethod(self, channel: discord.TextChannel, num):
        try:
            on_start = datetime.now()
            count = int(num)
            deleted = await channel.purge(limit=count, check=is_not_pinned)
            on_end = datetime.now()
            usedTime = on_end - on_start
            return deleted, usedTime
        except:
            if num == 'all':
                on_start = datetime.now()
                deleted = await channel.purge(limit=500, check=is_not_pinned)
                on_end = datetime.now()
                usedTime = on_end - on_start
                return deleted, usedTime

    @commands.group()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, num, channel: discord.TextChannel = 'help'):
        if logchannel is not None:
            logc = self.bot.get_channel(logchannel)
        else:
            logc = None
        if channel == ctx.channel:
            await ctx.message.delete()
            await ctx.send(f"> ERROR: Bitte gebe einen anderen Channel als den an, in dem du den Command ausführst!")
            return
        elif str(channel) == 'help' or str(channel) == 'Help':
            await ctx.send(
                f'> Nutze: `+clear <anzahl/"all"> <#channelName>`\n> Wenn du "all" nutzt, werden 500 Nachrichten gelöscht!')
            return
        else:
            try:
                count = int(num)
                if count >= 300:
                    await ctx.message.delete()
                    await ctx.send(
                        '> ERROR: Du kannst nicht mehr als 300 Nachrichten aufeinmal löschen. Nutze "all" um 500 auf einmal zu löschen!')
                    return
            except:
                count = 'alle'
            tembed = discord.Embed(
                description=f'Mödchtest du wirklich **{500 if count == "alle" else count}** Nachrichten im channel {channel.mention} unwiederruflich löschen?',
                color=0xB1FBFF, timestamp=datetime.utcnow())
            tembed.set_author(name=f'ClearCommand - Confirming', icon_url='https://i.ibb.co/2WQdHqj/Warning.png')
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
                    description='Du hast dich nicht rechtzeitig endschieden!\nDie Nachrichten wurden **nicht** gelöscht!',
                    color=0xB1FBFF, timestamp=datetime.utcnow())
                tembed.set_author(name=f'ClearCommand - Timeout!', icon_url='https://i.ibb.co/xDWBGW3/Error.png')
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
                    deleted, usedTime = await clear.clearMethod(self, channel, num)
                    tembed = discord.Embed(
                        description=f'**»** Du hast den Löschvorgang **bestätigt**!\n**«**\n**»** Gelöschte Nachrichten: `{len(deleted)}`\n**»** Channel: {channel.mention}\n**»** Ausgeführt von: {ctx.author.mention}\n**»** Ausgeführt am/um: <t:{str(datetime.timestamp(datetime.utcnow())).split(".", 1)[0]}>\n**»** UsedTime: **{str(usedTime)[:10] + "** - Hour:Minutes:Seconds:Milliseconds" if len(str(usedTime)) > 10 else str(usedTime)}',
                        color=0xB1FBFF, timestamp=datetime.utcnow())
                    tembed.set_author(name=f'ClearCommand - Confirmed', icon_url='https://i.ibb.co/104kpLk/Confrim.png')
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
                        description='Du hast den Löschvorgang **abgebrochen**!\nDie Nachrichten wurden **nicht** gelöscht!',
                        color=0xB1FBFF, timestamp=datetime.utcnow())
                    tembed.set_author(name=f'ClearCommand - Canceled', icon_url='https://i.ibb.co/xDWBGW3/Error.png')
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
    bot.add_cog(clear(bot))
