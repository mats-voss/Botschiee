from typing import Optional

import DiscordUtils
import discord
from discord.ext import commands

from botUtils.utils import *


class UserInfo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def generalInfo(self, user: Optional[Member]):
        embed = discord.Embed(title=f'General Information',
                              description=f'''
                              Mention: {user.mention}
                              User-ID: `{user.id}`
                              User-Tag: `{user.name}#{user.discriminator}`
                              Online Status: `{await utils.getuserstatus(user)}`
                              Highest Role: `{user.top_role}`
                              Joined: `{user.joined_at.strftime('%d/%m/%Y, %H:%M:%S')}`
                              Createt: `{user.created_at.strftime('%d/%m/%Y, %H:%M:%S')}`''',
                              color=user.color, timestamp=datetime.utcnow())
        embed.set_author(name=f'Discord User Info - {user}', icon_url=user.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(text=f'{self.bot.user.name} - Page 1/2',
                         icon_url=self.bot.user.avatar_url)
        return embed

    async def extraInfo(self, user: Optional[Member]):
        embed = discord.Embed(title=f'Activity Information', color=user.color, timestamp=datetime.utcnow())
        listeningURL = None
        custom = False
        listening = False
        streaming = False
        playing = False
        for activity in user.activities:
            if str(activity.type) == 'ActivityType.custom':
                try:
                    try:
                        if str(activity.name) == 'None':
                            name = 'N/A'
                        else:
                            name = activity.name
                    except:
                        name = 'N/A'
                    try:
                        if str(activity.emoji) == 'None':
                            emoji = 'N/A'
                        else:
                            emoji = activity.emoji
                    except:
                        emoji = 'N/A'
                    embed.add_field(name='Custom Activity',
                                    value=f'''
                                    Text: `{name}`
                                    Emoji: `{emoji}`
                                    ''', inline=False)
                    custom = True
                except Exception as error:
                    print(f'ERROR in UserInfo/ExtraInfo: {error}')
            elif str(activity.type) == 'ActivityType.listening':
                try:
                    try:
                        titel = activity.title
                    except:
                        titel = 'N/A'
                    try:
                        artist = activity.artist
                    except:
                        artist = 'N/A'
                    try:
                        album = activity.album
                    except:
                        album = 'N/A'
                    embed.add_field(name='Spotify Activity', value=f'''
                                    Titel: `{titel}`
                                    Artist: `{artist}`
                                    Album: `{album}`
                                    ''', inline=False)
                    listening = True
                    try:
                        listeningURL = str(activity.album_cover_url)
                    except:
                        listeningURL = None
                except Exception as error:
                    print(f'ERROR in UserInfo/ExtraInfo: {error}')
            elif str(activity.type) == 'ActivityType.streaming':
                try:
                    try:
                        titel = activity.name
                    except:
                        titel = 'N/A'
                    try:
                        if str(activity.details) == 'None':
                            details = 'N/A'
                        else:
                            details = activity.details
                    except:
                        details = 'N/A'
                    try:
                        username = activity.twitch_name
                    except:
                        username = 'N/A'
                    try:
                        url = f'[Klick Hier]({activity.url})'
                    except:
                        url = 'N/A'
                    embed.add_field(name='Straming Activity', value=f'''
                                    Titel: `{titel}`
                                    Details: `{details}`
                                    UserName: `{username}`
                                    URL: {url}
                                    ''', inline=False)
                    streaming = True
                except Exception as error:
                    print(f'ERROR in UserInfo/ExtraInfo: {error}')
            elif str(activity.type) == 'ActivityType.playing':
                try:
                    try:
                        name = activity.name
                    except:
                        name = 'N/A'
                    try:
                        details = activity.details
                    except:
                        details = 'N/A'
                    try:
                        start = activity.start.strftime('%d/%m/%Y, %H:%M:%S')
                    except:
                        start = 'N/A'
                    try:
                        largeImage = f'`{activity.large_image_text}` [Picture]({activity.large_image_url})'
                    except:
                        largeImage = 'N/A'
                    try:
                        smallImage = f'`{activity.small_image_text}` [Picture]({activity.small_image_url})'
                    except:
                        smallImage = 'N/A'
                    embed.add_field(name='Game Activity', value=f'''
                                    Name: `{name}`
                                    Detail: `{details}`
                                    Start: `{start}`
                                    LargeImage: {largeImage}
                                    SmallImage: {smallImage}
                                    ''', inline=False)
                    playing = True
                except Exception as error:
                    print(f'ERROR in UserInfo/ExtraInfo: {error}')
        if listeningURL is not None:
            embed.set_thumbnail(url=listeningURL)
        embed.set_author(name=f'Discord User Info - {user}', icon_url=user.avatar_url)
        embed.set_footer(text=f'{self.bot.user.name} - Page 2/2',
                         icon_url=self.bot.user.avatar_url)
        if custom is False & listening is False & streaming is False & playing is False:
            embed.add_field(name='Keine Activity', value='Der User hat keine aktuellen Aktivitäten!')
        else:
            pass
        return embed

    async def generate(self, ctx, perms, user):
        color = 0xB1FBFF
        one = await self.generalInfo(user)
        two = await self.extraInfo(user)
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=False)
        if perms is not None:
            if perms.manage_messages:
                paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=True)
        paginator.add_reaction('⏮️', "first")
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('⏹', "lock")
        paginator.add_reaction('⏩', "next")
        paginator.add_reaction('⏭️', "last")
        embeds = [one, two]
        return embeds, paginator

    @commands.has_permissions(kick_members=True)
    @commands.command(aliases=['ui', 'user'])
    async def userInfo(self, ctx, user: Optional[Member]):
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
        embeds, paginator = await self.generate(ctx, perms, user)
        await paginator.run(embeds)


def setup(bot):
    bot.add_cog(UserInfo(bot))
