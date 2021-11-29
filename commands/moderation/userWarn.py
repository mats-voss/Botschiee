import asyncio.exceptions
import random
from datetime import datetime
from typing import Optional
import json

import discord
from discord import Member
from discord.ext import commands
from discord_components import *


class UserWarns(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['warn', 'w'])
    @commands.has_permissions(kick_members=True)
    async def addWarn(self, ctx, user: discord.Member, reason, proof: str = None):
        RunningID = random.randrange(1000000000000, 9999999999999)
        with open('json/UserWarns.json', 'r') as file:
            warnFile = json.loads(file.read())
        # Create Warn entry in JSON
        try:
            warnFile[str(ctx.message.guild.id)][str(user.id)][
                f'Warn-{str(warnFile[str(ctx.message.guild.id)][str(user.id)]["count"]).zfill(3)}'] = {
                'UID': RunningID,
                'Reason': reason,
                'Proof': proof,
                'WarnedBy-ID': ctx.author.id,
                'DateTime': datetime.utcnow().strftime('%d/%m/%Y - %H:%M:%S'),
                'TimeStamp': f'<t:{str(datetime.timestamp(datetime.utcnow())).split(".", 1)[0]}:d>'
            }
            warnFile[str(ctx.message.guild.id)][str(user.id)]["count"] += 1
        except:
            try:
                warnFile[str(ctx.message.guild.id)][str(user.id)] = {
                    'count': 2,
                    f'Warn-001': {
                        'UID': RunningID,
                        'Reason': reason,
                        'Proof': proof,
                        'WarnedBy-ID': ctx.author.id,
                        'DateTime': datetime.utcnow().strftime('%d/%m/%Y - %H:%M:%S'),
                        'TimeStamp': f'<t:{str(datetime.timestamp(datetime.utcnow())).split(".", 1)[0]}:d>'
                    }
                }
            except:
                warnFile[str(ctx.message.guild.id)] = {
                    str(user.id): {
                        'count': 2,
                        f'Warn-001': {
                            'UID': RunningID,
                            'Reason': reason,
                            'Proof': proof,
                            'WarnedBy-ID': ctx.author.id,
                            'DateTime': datetime.utcnow().strftime('%d/%m/%Y - %H:%M:%S'),
                            'TimeStamp': f'<t:{str(datetime.timestamp(datetime.utcnow())).split(".", 1)[0]}:d>'
                        }
                    }
                }
        with open('json/UserWarns.json', 'w') as file:
            file.write(json.dumps(warnFile, indent=4))
        # send Embed with info's as confirmation
        embed = discord.Embed(title=f'Moderation-Warning', description=f'''
                                Warn-UID: `{RunningID}`
                                Warned User: {user.mention}
                                Reason: `{reason}`
                                Proof: `{proof}`
                                Warned by: [**{user.top_role}**]{ctx.author.mention}
                                Time: <t:{str(datetime.timestamp(datetime.utcnow())).split(".", 1)[0]}:d>
                                ''', color=0xB1FBFF, timestamp=datetime.utcnow())
        embed.set_author(name=f'UserWarning - {user.name}#{user.discriminator}', icon_url=user.avatar_url)
        embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=['listwarn', 'lw'])
    @commands.has_permissions(kick_members=True)
    async def listWarns(self, ctx, user: discord.Member):
        with open('json/UserWarns.json', 'r') as file:
            warnFile = json.loads(file.read())
        warnCount = 0
        embed = discord.Embed(color=0xB1FBFF, timestamp=datetime.utcnow())

        try:
            for warns in warnFile[str(ctx.guild.id)][str(user.id)]:
                if warns != 'count':
                    sup_user = await self.bot.fetch_user(
                        warnFile[str(ctx.guild.id)][str(user.id)][warns]['WarnedBy-ID'])
                    embed.add_field(name=f"Moderation-Warning",
                                    value=f"""__Warn-UID__: `{warnFile[str(ctx.guild.id)][str(user.id)][warns]['UID']}`
                                                                __Reason__: `{warnFile[str(ctx.guild.id)][str(user.id)][warns]['Reason']}`
                                                                __Proof__: `{warnFile[str(ctx.guild.id)][str(user.id)][warns]['Proof']}`
                                                                __Warned by__: [**{user.top_role}**]{sup_user.mention}
                                                                __Time__: {warnFile[str(ctx.guild.id)][str(user.id)][warns]['TimeStamp']}
                                                                """)
                    warnCount += 1
        except KeyError as e:
            if str(e) == "'" + str(user.id) + "'":
                await ctx.send(f'> Der User "{user.name}#{user.discriminator}" hat aktuell keine Warnings!')
                return
            elif str(e) == "'" + str(ctx.guild.id) + "'":
                await ctx.send(f'> In der Guilde "{ctx.guild.name}" wurden noch keine Warns vergeben!')
                return
        except Exception as e:
            print(f'Error in userWarn, listWarn: {e}')
            await ctx.send('> Der User hat keine Warns!')
            return

        if warnCount != 0:
            embed.set_author(
                name=f"{user.display_name}#{user.discriminator} hat {warnCount} {'Warn' if warnCount == 1 else 'Warns'}",
                icon_url=user.avatar_url)
            embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)
        else:
            await ctx.send(f'> Der User "{user.name}#{user.discriminator}" hat keine Warns!')

    @commands.command(aliases=['dw'])
    @commands.has_permissions(kick_members=True)
    async def delwarn(self, ctx, user: discord.Member, warnUID):
        with open('json/UserWarns.json', 'r') as file:
            warnFile = json.loads(file.read())
        erfolg = False
        try:
            for warns in warnFile[str(ctx.guild.id)][str(user.id)]:
                if warns != 'count':
                    if warnFile[str(ctx.guild.id)][str(user.id)][warns]['UID'] == int(warnUID):
                        sup_user = await self.bot.fetch_user(
                            warnFile[str(ctx.guild.id)][str(user.id)][warns]['WarnedBy-ID'])
                        embed = discord.Embed(color=0xB1FBFF, timestamp=datetime.utcnow())
                        embed.add_field(name=f"Moderation-Warning",
                                        value=f"""__Warn-UID__: `{warnFile[str(ctx.guild.id)][str(user.id)][warns]['UID']}`
                                                                                        __Reason__: `{warnFile[str(ctx.guild.id)][str(user.id)][warns]['Reason']}`
                                                                                        __Proof__: `{warnFile[str(ctx.guild.id)][str(user.id)][warns]['Proof']}`
                                                                                        __Warned by__: [**{user.top_role}**]{sup_user.mention}
                                                                                        __Time__: {warnFile[str(ctx.guild.id)][str(user.id)][warns]['TimeStamp']}
                                                                                        """)
                        embed.set_author(name=f'UserWarning - {user.name}#{user.discriminator}',
                                         icon_url=user.avatar_url)
                        embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                        msg = await ctx.send(embed=embed, components=[
                            [
                                Button(style=ButtonStyle.green, label='Confirm', emoji="✅"),
                                Button(style=ButtonStyle.red, label='Decline', emoji='❌')
                            ],
                        ],
                                             )
                        try:
                            res = await self.bot.wait_for("button_click", timeout=20)
                        except asyncio.exceptions.TimeoutError:
                            tembed = discord.Embed(
                                description='Du hast dich nicht rechtzeitig endschieden!\nDer Warn wurde **nicht** gelöscht!',
                                color=0xB1FBFF, timestamp=datetime.utcnow())
                            tembed.set_author(name=f'Timeout! - {user.name}#{user.discriminator}',
                                              icon_url=user.avatar_url)
                            tembed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                            await msg.edit(
                                embed=tembed,
                                components=[
                                ],
                            )
                            await asyncio.sleep(5)
                            await ctx.message.delete()
                            await msg.delete()
                            return
                        if res.component.label == 'Confirm':
                            if ctx.author == res.user:
                                del warnFile[str(ctx.guild.id)][str(user.id)][warns]
                                warnFile[str(ctx.guild.id)][str(user.id)]['count'] -= 1
                                with open('json/UserWarns.json', 'w') as file:
                                    file.write(json.dumps(warnFile, indent=4))
                                tembed = discord.Embed(
                                    description='Du hast den Löschvorgang **bestätigt**!\nDer Warn wurde **erfolgreich** gelöscht!',
                                    color=0xB1FBFF, timestamp=datetime.utcnow())
                                tembed.set_author(name=f'Confirmed! - {user.name}#{user.discriminator}',
                                                  icon_url=user.avatar_url)
                                tembed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                                await msg.edit(
                                    embed=tembed,
                                    components=[
                                    ],
                                )
                                await asyncio.sleep(5)
                                await ctx.message.delete()
                                await msg.delete()
                                return
                        elif res.component.label == 'Decline':
                            if ctx.author == res.user:
                                tembed = discord.Embed(description='Du hast den Löschvorgang **abgebrochen**!\nDer Warn wurde **nicht** gelöscht!',
                                                       color=0xB1FBFF, timestamp=datetime.utcnow())
                                tembed.set_author(name=f'Declined! - {user.name}#{user.discriminator}',
                                                  icon_url=user.avatar_url)
                                tembed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                                await msg.edit(
                                    embed=tembed,
                                    components=[
                                    ],
                                )
                                await asyncio.sleep(5)
                                await ctx.message.delete()
                                await msg.delete()
                                return
                else:
                    continue
        except ValueError:
            if warnUID == 'all' or warnUID == 'All':
                for warns in warnFile[str(ctx.guild.id)][str(user.id)]:
                    if warns != 'count':
                        try:
                            sup_user = await self.bot.fetch_user(
                                warnFile[str(ctx.guild.id)][str(user.id)][warns]['WarnedBy-ID'])
                            embed = discord.Embed(description='Confirm to delete all Warnings!', color=0xB1FBFF, timestamp=datetime.utcnow())
                            embed.set_author(name=f'Delete All Warnings - {user.name}#{user.discriminator}',
                                             icon_url=user.avatar_url)
                            embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                            msg = await ctx.send(embed=embed, components=[
                                [
                                    Button(style=ButtonStyle.green, label='Confirm', emoji="✅"),
                                    Button(style=ButtonStyle.red, label='Decline', emoji='❌')
                                ],
                            ],
                                                 )
                            try:
                                res = await self.bot.wait_for("button_click", timeout=20)
                            except asyncio.exceptions.TimeoutError:
                                tembed = discord.Embed(
                                    description='Du hast dich nicht rechtzeitig endschieden!\nDie Warns wurde **nicht** gelöscht!',
                                    color=0xB1FBFF, timestamp=datetime.utcnow())
                                tembed.set_author(name=f'Timeout! - {user.name}#{user.discriminator}',
                                                  icon_url=user.avatar_url)
                                tembed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                                await msg.edit(
                                    embed=tembed,
                                    components=[
                                    ],
                                )
                                await asyncio.sleep(5)
                                await ctx.message.delete()
                                await msg.delete()
                                return
                            if res.component.label == 'Confirm':
                                if ctx.author == res.user:
                                    del warnFile[str(ctx.guild.id)][str(user.id)]
                                    with open('json/UserWarns.json', 'w') as file:
                                        file.write(json.dumps(warnFile, indent=4))
                                    tembed = discord.Embed(
                                        description='Du hast den Löschvorgang **bestätigt**!\nDie Warns wurde **erfolgreich** gelöscht!',
                                        color=0xB1FBFF, timestamp=datetime.utcnow())
                                    tembed.set_author(name=f'Confirmed! - {user.name}#{user.discriminator}',
                                                      icon_url=user.avatar_url)
                                    tembed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                                    await msg.edit(
                                        embed=tembed,
                                        components=[
                                        ],
                                    )
                                    await asyncio.sleep(5)
                                    await ctx.message.delete()
                                    await msg.delete()
                                    return
                            elif res.component.label == 'Decline':
                                if ctx.author == res.user:
                                    tembed = discord.Embed(
                                        description='Du hast den Löschvorgang **abgebrochen**!\nDie Warns wurde **nicht** gelöscht!',
                                        color=0xB1FBFF, timestamp=datetime.utcnow())
                                    tembed.set_author(name=f'Declined! - {user.name}#{user.discriminator}',
                                                      icon_url=user.avatar_url)
                                    tembed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                                    await msg.edit(
                                        embed=tembed,
                                        components=[
                                        ],
                                    )
                                    await asyncio.sleep(5)
                                    await ctx.message.delete()
                                    await msg.delete()
                                    return
                        except:
                            erfolg = False
                            await ctx.send(
                                f'> ERROR: Die Warn-UID konnte bei dem angegebenen User nicht gefunden werden!')
                    else:
                        continue
            else:
                erfolg = False
                await ctx.send(f'> ERROR: Die Warn-UID konnte bei dem angegebenen User nicht gefunden werden!')
        except KeyError as e:
            if str(warnUID) == 'all' or str(warnUID) == 'All':
                await ctx.send(f'> Der User "{user.name}#{user.discriminator}" hat aktuell keine Warnings!')
                return
            elif str(e) == "'" + str(user.id) + "'":
                await ctx.send(f'> Der User "{user.name}#{user.discriminator}" hat aktuell keine Warnings!')
                return
            elif str(e) == "'" + str(ctx.guild.id) + "'":
                await ctx.send(f'> In der Guilde "{ctx.guild.name}" wurden noch keine Warns vergeben!')
                return
        except Exception as e:
            print(e)
            print(type(e))
            return
        await ctx.send(f'> Der User "{user.name}#{user.discriminator}" hat keinen Warn mit der angegebenen WarnUID!')


def setup(bot):
    bot.add_cog(UserWarns(bot))
