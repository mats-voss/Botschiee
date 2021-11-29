import json
import pathlib
import sys

import discord
from discord.ext import commands
from botUtils.embeds import Embeds


class BotInfo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
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
        color = 0xB1FBFF
        embed = discord.Embed(title='Ping', description='Pong!', color=color)
        msg = await ctx.send(embed=embed)
        ms = (msg.created_at - ctx.message.created_at).total_seconds() * 1000
        try:
            embed = discord.Embed(title='Ping', description=f'Pong! `{int(ms)}ms`', color=color)
            await msg.edit(embed=embed)
        except discord.NotFound:
            pass

    @commands.command()
    async def help(self, ctx):
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
        embeds, paginator = await Embeds().Help().generate(ctx, perms, await self.bot.fetch_user(834762194629034035))
        await paginator.run(embeds)

    @commands.command()
    async def info(self, ctx):
        version = sys.version_info

        def line_count():
            files = classes = funcs = comments = lines = letters = 0
            p = pathlib.Path('/')
            for f in p.rglob("*.py"):
                if str(f) == f'D:\Entwicklung\Python\Botschiee\\venv\Lib\site-packages\six.py':
                    continue
                if str(f) == f'D:\Entwicklung\Python\Botschiee\\venv\Lib\site-packages\\typing_extensions.py':
                    break
                files += 1
                with f.open(encoding='utf-8') as of:
                    letters += len(f.open(encoding='utf-8').read())
                    for line in of.readlines():
                        line = line.strip()
                        if line.startswith("class"):
                            classes += 1
                        if line.startswith("def"):
                            funcs += 1
                        if line.startswith("async def"):
                            funcs += 1
                        if "#" in line:
                            comments += 1
                        lines += 1
            return files, classes, funcs, comments, lines, letters

        files, classes, funcs, comments, lines, letters = await self.bot.loop.run_in_executor(None, line_count)
        # Embed
        with open('json/bot_stats.json', 'r', encoding='utf-8') as file:
            count = json.loads(file.read())
        owner = self.bot.get_user(self.bot.owner_id)
        em = discord.Embed(color=0xB1FBFF)
        em.add_field(name="Bot", value=f"""
            **»**  Guilds: `{len(self.bot.guilds)}`
            **»**  Users: `{len(self.bot.users)}`
            **»**  Commands: `{len([cmd for cmd in list(self.bot.walk_commands()) if not cmd.hidden])}`
            **»**  Commands Executed: `{count['botStats']["commandsExecutedAll"]}`""", inline=False)
        em.add_field(name="File Statistics", value=f"""
            **»**  Letters: `{letters}`
            **»**  Files: `{files}`
            **»**  Lines: `{lines}`
            **»**  Classes: `{classes}`
            **»**  Funktions: `{funcs}`
            **»**  Comments: `{comments}`""", inline=False)
        em.add_field(name="Links", value=f"""
            **»** [Developer](https://github.com/MatsiVoss) | Mats#2840
            **»** [Source](https://xboxmedia.de/wp-content/uploads/coming-soon.jpg)
            **»** [Invite](https://xboxmedia.de/wp-content/uploads/coming-soon.jpg)""", inline=False)
        em.set_thumbnail(url=self.bot.user.avatar_url)
        em.set_footer(text=f"Python {version[0]}.{version[1]}.{version[2]} • discord.py {discord.__version__}")
        em.set_author(name=f'{self.bot.user.name} - Bot Info', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=em)

    @commands.is_owner()
    @commands.command()
    async def invite(self, ctx):
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
        embed = discord.Embed(title="Invite the Bot",
                              description="You can invite the bot at https://plun1331.github.io/hypixelbot/add.")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(BotInfo(bot))
