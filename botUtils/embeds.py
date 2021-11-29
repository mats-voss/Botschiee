from typing import Optional

import discord
import DiscordUtils
import random

from discord import Member

from botUtils.utils import *

other = """

Wenn Sie weitere Hilfe benötigen, treten sie dem [Support-Server](https://discord.gg/gxB8mRC) bei."""

botinfo = """`h!help` - Gibt die Liste von Befehlen zurück.
`+info` - Zeigt einige Informationen und Statistiken über den Bot.
`+ping` - Zeigt die Latenz des Bots.
`+invite` - Returns the bot's invite link."""

playerstats = """`h!player <player>` - Zeigt einige allgemeine Statistiken für den angegebenen Spieler.
`+bedwars <player>` - Zeigt die Bedwars-Statistiken des angegebenen Spielers.
`+skywars <player>` - Zeigt die Skywars-Statistiken des angegebenen Spielers."""

hypixelstats = """`+leaderboard <game> <type>` - Zeigt die Leader auf der angegebenen Bestenliste.
`+guild <guild name>` - Zeigt Informationen zur angegebenen Gilde.
`+playercount` - Zeigt die aktuelle Anzahl der Hypixel-Spieler.
`+watchdog` - Zeigt die Hypixel Watchdog-Statistiken."""

moderation = """`+clear <amount/all> <#channel>` - Löschte eine angegebene Zahl an nachrichten.
`+lockdown <#channel>` - Sperrt einen Channel für alle User.
`+userinfo <user>` - Zeigt informationen für den User."""

minecraft = """`+skin <player>` - Zeigt den Skin des Spielers."""

class Embeds:
    class Bedwars:
        async def main(self, name, color, data, bot):
            try:
                level = str(utils.comma(int(data['player']['achievements']['bedwars_level']))) + ' ⭐'
            except:
                level = 'N/A'
            try:
                games_played = data['player']['stats']['Bedwars']['games_played_bedwars']
            except:
                games_played = 'N/A'
            try:
                exp = data['player']['stats']['Bedwars']['Experience']
            except:
                exp = 'N/A'
            try:
                final_deaths = data['player']['stats']['Bedwars']['final_deaths_bedwars']
            except:
                final_deaths = 'N/A'
            try:
                normal_deaths = data['player']['stats']['Bedwars']['deaths_bedwars']
            except:
                normal_deaths = 'N/A'
            try:
                total_deaths = final_deaths+normal_deaths
                if total_deaths == 'N/AN/A':
                    raise ValueError
            except:
                total_deaths = 'N/A'
            try:
                beds_lost = data['player']['stats']['Bedwars']['beds_lost_bedwars']
            except:
                beds_lost = 'N/A'
            try:
                beds_broken = data['player']['stats']['Bedwars']['beds_broken_bedwars']
            except:
                beds_broken = 'N/A'
            try:
                normal_kills = data['player']['stats']['Bedwars']['kills_bedwars']
            except:
                normal_kills = 'N/A'
            try:
                final_kills = data['player']['stats']['Bedwars']['final_kills_bedwars']
            except:
                final_kills = 'N/A'
            try:
                total_kills = final_kills+normal_kills
                if total_kills == 'N/AN/A':
                    raise ValueError
            except:
                total_kills = 'N/A'
            try:
                wins = data['player']['stats']['Bedwars']['wins_bedwars']
            except:
                wins = 'N/A'
            try:
                losses = data['player']['stats']['Bedwars']['losses_bedwars']
            except:
                losses = 'N/A'
            try:
                winstreak = data['player']['stats']['Bedwars']['winstreak']
            except:
                winstreak = 'N/A'
            embed = discord.Embed(title=name + "'s Bedwars Stats - Overall", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            embed.add_field(name="Bedwars Level", value=str(level), inline=True)
            try:
                embed.add_field(name="Bedwars Experience", value=str(utils.comma(round(exp, 0))), inline=True)
            except:
                embed.add_field(name="Bedwars Experience", value=str('N/A'), inline=True)
            embed.add_field(name="Games Played", value=str(utils.comma(games_played)), inline=True)
            embed.add_field(name="Normal Deaths", value=str(utils.comma(normal_deaths)), inline=True)
            embed.add_field(name="Final Deaths", value=str(utils.comma(final_deaths)), inline=True)
            embed.add_field(name="Total Deaths", value=str(utils.comma(total_deaths)), inline=True)
            embed.add_field(name="Normal Kills", value=str(utils.comma(normal_kills)), inline=True)
            embed.add_field(name="Final Kills", value=str(utils.comma(final_kills)), inline=True)
            embed.add_field(name="Total Kills", value=str(utils.comma(total_kills)), inline=True)
            try:
                embed.add_field(name="Normal K/D Ratio", value=str(utils.comma(round(normal_kills/normal_deaths, 2))), inline=True)
            except:
                embed.add_field(name="Normal K/D Ratio", value=str('N/A'), inline=True)
            try:
                embed.add_field(name="Final K/D Ratio", value=str(utils.comma(round(final_kills/final_deaths, 2))), inline=True)
            except:
                embed.add_field(name="Final K/D Ratio", value=str('N/A'), inline=True)
            try:
                embed.add_field(name="K/D Ratio", value=str(utils.comma(round(total_kills/total_deaths, 2))), inline=True)
            except:
                embed.add_field(name="K/D Ratio", value=str('N/A'), inline=True)
            embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
            embed.add_field(name="Losses", value=str(utils.comma(losses)), inline=True)
            try:
                embed.add_field(name="W/L Ratio", value=str(utils.comma(round(wins/losses, 2))), inline=True)
            except:
                embed.add_field(name="W/L Ratio", value=str('N/A'), inline=True)
            embed.add_field(name="Beds Lost", value=str(utils.comma(beds_lost)), inline=True)
            embed.add_field(name="Beds Broken", value=str(utils.comma(beds_broken)), inline=True)
            embed.add_field(name="Winstreak", value=str(utils.comma(winstreak)), inline=True)
            embed.set_footer(text=f'{bot.name} - Page 1/6', icon_url=bot.avatar_url)
            return embed
        
        async def solo(self, name, color, data, bot):
            try:
                level = str(utils.comma(int(data['player']['achievements']['bedwars_level']))) + ' ⭐'
            except:
                level = 'N/A'
            try:
                games_played = data['player']['stats']['Bedwars']['eight_one_games_played_bedwars']
            except:
                games_played = 'N/A'
            try:
                exp = data['player']['stats']['Bedwars']['Experience']
            except:
                exp = 'N/A'
            try:
                final_deaths = data['player']['stats']['Bedwars']['eight_one_final_deaths_bedwars']
            except:
                final_deaths = 'N/A'
            try:
                normal_deaths = data['player']['stats']['Bedwars']['eight_one_deaths_bedwars']
            except:
                normal_deaths = 'N/A'
            try:
                total_deaths = final_deaths+normal_deaths
                if total_deaths == 'N/AN/A':
                    raise ValueError
            except:
                total_deaths = 'N/A'
            try:
                beds_lost = data['player']['stats']['Bedwars']['eight_one_beds_lost_bedwars']
            except:
                beds_lost = 'N/A'
            try:
                beds_broken = data['player']['stats']['Bedwars']['eight_one_beds_broken_bedwars']
            except:
                beds_broken = 'N/A'
            try:
                normal_kills = data['player']['stats']['Bedwars']['eight_one_kills_bedwars']
            except:
                normal_kills = 'N/A'
            try:
                final_kills = data['player']['stats']['Bedwars']['eight_one_final_kills_bedwars']
            except:
                final_kills = 'N/A'
            try:
                total_kills = final_kills+normal_kills
                if total_kills == 'N/AN/A':
                    raise ValueError
            except:
                total_kills = 'N/A'
            try:
                wins = data['player']['stats']['Bedwars']['eight_one_wins_bedwars']
            except:
                wins = 'N/A'
            try:
                losses = data['player']['stats']['Bedwars']['eight_one_losses_bedwars']
            except:
                losses = 'N/A'
            try:
                winstreak = data['player']['stats']['Bedwars']['eight_one_winstreak']
            except:
                winstreak = 'N/A'
            embed = discord.Embed(title=name + "'s Bedwars Stats - Solo", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            embed.add_field(name="Bedwars Level", value=str(level), inline=True)
            try:
                embed.add_field(name="Bedwars Experience", value=str(utils.comma(round(exp, 0))), inline=True)
            except:
                embed.add_field(name="Bedwars Experience", value=str('N/A'), inline=True)
            embed.add_field(name="Games Played", value=str(utils.comma(games_played)), inline=True)
            embed.add_field(name="Normal Deaths", value=str(utils.comma(normal_deaths)), inline=True)
            embed.add_field(name="Final Deaths", value=str(utils.comma(final_deaths)), inline=True)
            embed.add_field(name="Total Deaths", value=str(utils.comma(total_deaths)), inline=True)
            embed.add_field(name="Normal Kills", value=str(utils.comma(normal_kills)), inline=True)
            embed.add_field(name="Final Kills", value=str(utils.comma(final_kills)), inline=True)
            embed.add_field(name="Total Kills", value=str(utils.comma(total_kills)), inline=True)
            try:
                embed.add_field(name="Normal K/D Ratio", value=str(utils.comma(round(normal_kills/normal_deaths, 2))), inline=True)
            except:
                embed.add_field(name="Normal K/D Ratio", value=str('N/A'), inline=True)
            try:
                embed.add_field(name="Final K/D Ratio", value=str(utils.comma(round(final_kills/final_deaths, 2))), inline=True)
            except:
                embed.add_field(name="Final K/D Ratio", value=str('N/A'), inline=True)
            try:
                embed.add_field(name="K/D Ratio", value=str(utils.comma(round(total_kills/total_deaths, 2))), inline=True)
            except:
                embed.add_field(name="K/D Ratio", value=str('N/A'), inline=True)
            embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
            embed.add_field(name="Losses", value=str(utils.comma(losses)), inline=True)
            try:
                embed.add_field(name="W/L Ratio", value=str(utils.comma(round(wins/losses, 2))), inline=True)
            except:
                embed.add_field(name="W/L Ratio", value=str('N/A'), inline=True)
            embed.add_field(name="Beds Lost", value=str(utils.comma(beds_lost)), inline=True)
            embed.add_field(name="Beds Broken", value=str(utils.comma(beds_broken)), inline=True)
            embed.add_field(name="Winstreak", value=str(utils.comma(winstreak)), inline=True)
            embed.set_footer(text=f'{bot.name} - Page 2/6', icon_url=bot.avatar_url)
            return embed

        async def doubles(self, name, color, data, bot):
            try:
                level = str(utils.comma(int(data['player']['achievements']['bedwars_level']))) + ' ⭐'
            except:
                level = 'N/A'
            try:
                games_played = data['player']['stats']['Bedwars']['eight_two_games_played_bedwars']
            except:
                games_played = 'N/A'
            try:
                exp = data['player']['stats']['Bedwars']['Experience']
            except:
                exp = 'N/A'
            try:
                final_deaths = data['player']['stats']['Bedwars']['eight_two_final_deaths_bedwars']
            except:
                final_deaths = 'N/A'
            try:
                normal_deaths = data['player']['stats']['Bedwars']['eight_two_deaths_bedwars']
            except:
                normal_deaths = 'N/A'
            try:
                total_deaths = final_deaths+normal_deaths
                if total_deaths == 'N/AN/A':
                    raise ValueError
            except:
                total_deaths = 'N/A'
            try:
                beds_lost = data['player']['stats']['Bedwars']['eight_two_beds_lost_bedwars']
            except:
                beds_lost = 'N/A'
            try:
                beds_broken = data['player']['stats']['Bedwars']['eight_two_beds_broken_bedwars']
            except:
                beds_broken = 'N/A'
            try:
                normal_kills = data['player']['stats']['Bedwars']['eight_two_kills_bedwars']
            except:
                normal_kills = 'N/A'
            try:
                final_kills = data['player']['stats']['Bedwars']['eight_two_final_kills_bedwars']
            except:
                final_kills = 'N/A'
            try:
                total_kills = final_kills+normal_kills
                if total_kills == 'N/AN/A':
                    raise ValueError
            except:
                total_kills = 'N/A'
            try:
                wins = data['player']['stats']['Bedwars']['eight_two_wins_bedwars']
            except:
                wins = 'N/A'
            try:
                losses = data['player']['stats']['Bedwars']['eight_two_losses_bedwars']
            except:
                losses = 'N/A'
            try:
                winstreak = data['player']['stats']['Bedwars']['eight_two_winstreak']
            except:
                winstreak = 'N/A'
            embed = discord.Embed(title=name + "'s Bedwars Stats - Doubles", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            embed.add_field(name="Bedwars Level", value=str(level), inline=True)
            try:
                embed.add_field(name="Bedwars Experience", value=str(utils.comma(round(exp, 0))), inline=True)
            except:
                embed.add_field(name="Bedwars Experience", value=str('N/A'), inline=True)
            embed.add_field(name="Games Played", value=str(utils.comma(games_played)), inline=True)
            embed.add_field(name="Normal Deaths", value=str(utils.comma(normal_deaths)), inline=True)
            embed.add_field(name="Final Deaths", value=str(utils.comma(final_deaths)), inline=True)
            embed.add_field(name="Total Deaths", value=str(utils.comma(total_deaths)), inline=True)
            embed.add_field(name="Normal Kills", value=str(utils.comma(normal_kills)), inline=True)
            embed.add_field(name="Final Kills", value=str(utils.comma(final_kills)), inline=True)
            embed.add_field(name="Total Kills", value=str(utils.comma(total_kills)), inline=True)
            try:
                embed.add_field(name="Normal K/D Ratio", value=str(utils.comma(round(normal_kills/normal_deaths, 2))), inline=True)
            except:
                embed.add_field(name="Normal K/D Ratio", value=str('N/A'), inline=True)
            try:
                embed.add_field(name="Final K/D Ratio", value=str(utils.comma(round(final_kills/final_deaths, 2))), inline=True)
            except:
                embed.add_field(name="Final K/D Ratio", value=str('N/A'), inline=True)
            try:
                embed.add_field(name="K/D Ratio", value=str(utils.comma(round(total_kills/total_deaths, 2))), inline=True)
            except:
                embed.add_field(name="K/D Ratio", value=str('N/A'), inline=True)
            embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
            embed.add_field(name="Losses", value=str(utils.comma(losses)), inline=True)
            try:
                embed.add_field(name="W/L Ratio", value=str(utils.comma(round(wins/losses, 2))), inline=True)
            except:
                embed.add_field(name="W/L Ratio", value=str('N/A'), inline=True)
            embed.add_field(name="Beds Lost", value=str(utils.comma(beds_lost)), inline=True)
            embed.add_field(name="Beds Broken", value=str(utils.comma(beds_broken)), inline=True)
            embed.add_field(name="Winstreak", value=str(utils.comma(winstreak)), inline=True)
            embed.set_footer(text=f'{bot.name} - Page 3/6', icon_url=bot.avatar_url)
            return embed

        async def threes(self, name, color, data, bot):
            try:
                level = str(utils.comma(int(data['player']['achievements']['bedwars_level']))) + ' ⭐'
            except:
                level = 'N/A'
            try:
                games_played = data['player']['stats']['Bedwars']['four_three_games_played_bedwars']
            except:
                games_played = 'N/A'
            try:
                exp = data['player']['stats']['Bedwars']['Experience']
            except:
                exp = 'N/A'
            try:
                final_deaths = data['player']['stats']['Bedwars']['four_three_final_deaths_bedwars']
            except:
                final_deaths = 'N/A'
            try:
                normal_deaths = data['player']['stats']['Bedwars']['four_three_deaths_bedwars']
            except:
                normal_deaths = 'N/A'
            try:
                total_deaths = final_deaths+normal_deaths
                if total_deaths == 'N/AN/A':
                    raise ValueError
            except:
                total_deaths = 'N/A'
            try:
                beds_lost = data['player']['stats']['Bedwars']['four_three_beds_lost_bedwars']
            except:
                beds_lost = 'N/A'
            try:
                beds_broken = data['player']['stats']['Bedwars']['four_three_beds_broken_bedwars']
            except:
                beds_broken = 'N/A'
            try:
                normal_kills = data['player']['stats']['Bedwars']['four_three_kills_bedwars']
            except:
                normal_kills = 'N/A'
            try:
                final_kills = data['player']['stats']['Bedwars']['four_three_final_kills_bedwars']
            except:
                final_kills = 'N/A'
            try:
                total_kills = final_kills+normal_kills
                if total_kills == 'N/AN/A':
                    raise ValueError
            except:
                total_kills = 'N/A'
            try:
                wins = data['player']['stats']['Bedwars']['four_three_wins_bedwars']
            except:
                wins = 'N/A'
            try:
                losses = data['player']['stats']['Bedwars']['four_three_losses_bedwars']
            except:
                losses = 'N/A'
            try:
                winstreak = data['player']['stats']['Bedwars']['four_three_winstreak']
            except:
                winstreak = 'N/A'
            embed = discord.Embed(title=name + "'s Bedwars Stats - 3v3v3v3", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            embed.add_field(name="Bedwars Level", value=str(level), inline=True)
            try:
                embed.add_field(name="Bedwars Experience", value=str(utils.comma(round(exp, 0))), inline=True)
            except:
                embed.add_field(name="Bedwars Experience", value=str('N/A'), inline=True)
            embed.add_field(name="Games Played", value=str(utils.comma(games_played)), inline=True)
            embed.add_field(name="Normal Deaths", value=str(utils.comma(normal_deaths)), inline=True)
            embed.add_field(name="Final Deaths", value=str(utils.comma(final_deaths)), inline=True)
            embed.add_field(name="Total Deaths", value=str(utils.comma(total_deaths)), inline=True)
            embed.add_field(name="Normal Kills", value=str(utils.comma(normal_kills)), inline=True)
            embed.add_field(name="Final Kills", value=str(utils.comma(final_kills)), inline=True)
            embed.add_field(name="Total Kills", value=str(utils.comma(total_kills)), inline=True)
            try:
                embed.add_field(name="Normal K/D Ratio", value=str(utils.comma(round(normal_kills/normal_deaths, 2))), inline=True)
            except:
                embed.add_field(name="Normal K/D Ratio", value=str('N/A'), inline=True)
            try:
                embed.add_field(name="Final K/D Ratio", value=str(utils.comma(round(final_kills/final_deaths, 2))), inline=True)
            except:
                embed.add_field(name="Final K/D Ratio", value=str('N/A'), inline=True)
            try:
                embed.add_field(name="K/D Ratio", value=str(utils.comma(round(total_kills/total_deaths, 2))), inline=True)
            except:
                embed.add_field(name="K/D Ratio", value=str('N/A'), inline=True)
            embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
            embed.add_field(name="Losses", value=str(utils.comma(losses)), inline=True)
            try:
                embed.add_field(name="W/L Ratio", value=str(utils.comma(round(wins/losses, 2))), inline=True)
            except:
                embed.add_field(name="W/L Ratio", value=str('N/A'), inline=True)
            embed.add_field(name="Beds Lost", value=str(utils.comma(beds_lost)), inline=True)
            embed.add_field(name="Beds Broken", value=str(utils.comma(beds_broken)), inline=True)
            embed.add_field(name="Winstreak", value=str(utils.comma(winstreak)), inline=True)
            embed.set_footer(text=f'{bot.name} - Page 4/6', icon_url=bot.avatar_url)
            return embed

        async def fours(self, name, color, data, bot):
            try:
                level = str(utils.comma(int(data['player']['achievements']['bedwars_level']))) + ' ⭐'
            except:
                level = 'N/A'
            try:
                games_played = data['player']['stats']['Bedwars']['four_four_games_played_bedwars']
            except:
                games_played = 'N/A'
            try:
                exp = data['player']['stats']['Bedwars']['Experience']
            except:
                exp = 'N/A'
            try:
                final_deaths = data['player']['stats']['Bedwars']['four_four_final_deaths_bedwars']
            except:
                final_deaths = 'N/A'
            try:
                normal_deaths = data['player']['stats']['Bedwars']['four_four_deaths_bedwars']
            except:
                normal_deaths = 'N/A'
            try:
                total_deaths = final_deaths+normal_deaths
                if total_deaths == 'N/AN/A':
                    raise ValueError
            except:
                total_deaths = 'N/A'
            try:
                beds_lost = data['player']['stats']['Bedwars']['four_four_beds_lost_bedwars']
            except:
                beds_lost = 'N/A'
            try:
                beds_broken = data['player']['stats']['Bedwars']['four_four_beds_broken_bedwars']
            except:
                beds_broken = 'N/A'
            try:
                normal_kills = data['player']['stats']['Bedwars']['four_four_kills_bedwars']
            except:
                normal_kills = 'N/A'
            try:
                final_kills = data['player']['stats']['Bedwars']['four_four_final_kills_bedwars']
            except:
                final_kills = 'N/A'
            try:
                total_kills = final_kills+normal_kills
                if total_kills == 'N/AN/A':
                    raise ValueError
            except:
                total_kills = 'N/A'
            try:
                wins = data['player']['stats']['Bedwars']['four_four_wins_bedwars']
            except:
                wins = 'N/A'
            try:
                losses = data['player']['stats']['Bedwars']['four_four_losses_bedwars']
            except:
                losses = 'N/A'
            try:
                winstreak = data['player']['stats']['Bedwars']['four_four_winstreak']
            except:
                winstreak = 'N/A'
            embed = discord.Embed(title=name + "'s Bedwars Stats - 4v4v4v4", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            embed.add_field(name="Bedwars Level", value=str(level), inline=True)
            try:
                embed.add_field(name="Bedwars Experience", value=str(utils.comma(round(exp, 0))), inline=True)
            except:
                embed.add_field(name="Bedwars Experience", value=str('N/A'), inline=True)
            embed.add_field(name="Games Played", value=str(utils.comma(games_played)), inline=True)
            embed.add_field(name="Normal Deaths", value=str(utils.comma(normal_deaths)), inline=True)
            embed.add_field(name="Final Deaths", value=str(utils.comma(final_deaths)), inline=True)
            embed.add_field(name="Total Deaths", value=str(utils.comma(total_deaths)), inline=True)
            embed.add_field(name="Normal Kills", value=str(utils.comma(normal_kills)), inline=True)
            embed.add_field(name="Final Kills", value=str(utils.comma(final_kills)), inline=True)
            embed.add_field(name="Total Kills", value=str(utils.comma(total_kills)), inline=True)
            try:
                embed.add_field(name="Normal K/D Ratio", value=str(utils.comma(round(normal_kills/normal_deaths, 2))), inline=True)
            except:
                embed.add_field(name="Normal K/D Ratio", value=str('N/A'), inline=True)
            try:
                embed.add_field(name="Final K/D Ratio", value=str(utils.comma(round(final_kills/final_deaths, 2))), inline=True)
            except:
                embed.add_field(name="Final K/D Ratio", value=str('N/A'), inline=True)
            try:
                embed.add_field(name="K/D Ratio", value=str(utils.comma(round(total_kills/total_deaths, 2))), inline=True)
            except:
                embed.add_field(name="K/D Ratio", value=str('N/A'), inline=True)
            embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
            embed.add_field(name="Losses", value=str(utils.comma(losses)), inline=True)
            try:
                embed.add_field(name="W/L Ratio", value=str(utils.comma(round(wins/losses, 2))), inline=True)
            except:
                embed.add_field(name="W/L Ratio", value=str('N/A'), inline=True)
            embed.add_field(name="Beds Lost", value=str(utils.comma(beds_lost)), inline=True)
            embed.add_field(name="Beds Broken", value=str(utils.comma(beds_broken)), inline=True)
            embed.add_field(name="Winstreak", value=str(utils.comma(winstreak)), inline=True)
            embed.set_footer(text=f'{bot.name} - Page 5/6', icon_url=bot.avatar_url)
            return embed

        async def fourfour(self, name, color, data, bot):
            try:
                level = str(utils.comma(int(data['player']['achievements']['bedwars_level']))) + ' ⭐'
            except:
                level = 'N/A'
            try:
                games_played = data['player']['stats']['Bedwars']['two_four_games_played_bedwars']
            except:
                games_played = 'N/A'
            try:
                exp = data['player']['stats']['Bedwars']['Experience']
            except:
                exp = 'N/A'
            try:
                final_deaths = data['player']['stats']['Bedwars']['two_four_final_deaths_bedwars']
            except:
                final_deaths = 'N/A'
            try:
                normal_deaths = data['player']['stats']['Bedwars']['two_four_deaths_bedwars']
            except:
                normal_deaths = 'N/A'
            try:
                total_deaths = final_deaths+normal_deaths
                if total_deaths == 'N/AN/A':
                    raise ValueError
            except:
                total_deaths = 'N/A'
            try:
                beds_lost = data['player']['stats']['Bedwars']['two_four_beds_lost_bedwars']
            except:
                beds_lost = 'N/A'
            try:
                beds_broken = data['player']['stats']['Bedwars']['two_four_beds_broken_bedwars']
            except:
                beds_broken = 'N/A'
            try:
                normal_kills = data['player']['stats']['Bedwars']['two_four_kills_bedwars']
            except:
                normal_kills = 'N/A'
            try:
                final_kills = data['player']['stats']['Bedwars']['two_four_final_kills_bedwars']
            except:
                final_kills = 'N/A'
            try:
                total_kills = final_kills+normal_kills
                if total_kills == 'N/AN/A':
                    raise ValueError
            except:
                total_kills = 'N/A'
            try:
                wins = data['player']['stats']['Bedwars']['two_four_wins_bedwars']
            except:
                wins = 'N/A'
            try:
                losses = data['player']['stats']['Bedwars']['two_four_losses_bedwars']
            except:
                losses = 'N/A'
            try:
                winstreak = data['player']['stats']['Bedwars']['two_four_winstreak']
            except:
                winstreak = 'N/A'
            embed = discord.Embed(title=name + "'s Bedwars Stats - 4v4", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            embed.add_field(name="Bedwars Level", value=str(level), inline=True)
            try:
                embed.add_field(name="Bedwars Experience", value=str(utils.comma(round(exp, 0))), inline=True)
            except:
                embed.add_field(name="Bedwars Experience", value=str('N/A'), inline=True)
            embed.add_field(name="Games Played", value=str(utils.comma(games_played)), inline=True)
            embed.add_field(name="Normal Deaths", value=str(utils.comma(normal_deaths)), inline=True)
            embed.add_field(name="Final Deaths", value=str(utils.comma(final_deaths)), inline=True)
            embed.add_field(name="Total Deaths", value=str(utils.comma(total_deaths)), inline=True)
            embed.add_field(name="Normal Kills", value=str(utils.comma(normal_kills)), inline=True)
            embed.add_field(name="Final Kills", value=str(utils.comma(final_kills)), inline=True)
            embed.add_field(name="Total Kills", value=str(utils.comma(total_kills)), inline=True)
            try:
                embed.add_field(name="Normal K/D Ratio", value=str(utils.comma(round(normal_kills/normal_deaths, 2))), inline=True)
            except:
                embed.add_field(name="Normal K/D Ratio", value=str('N/A'), inline=True)
            try:
                embed.add_field(name="Final K/D Ratio", value=str(utils.comma(round(final_kills/final_deaths, 2))), inline=True)
            except:
                embed.add_field(name="Final K/D Ratio", value=str('N/A'), inline=True)
            try:
                embed.add_field(name="K/D Ratio", value=str(utils.comma(round(total_kills/total_deaths, 2))), inline=True)
            except:
                embed.add_field(name="K/D Ratio", value=str('N/A'), inline=True)
            embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
            embed.add_field(name="Losses", value=str(utils.comma(losses)), inline=True)
            try:
                embed.add_field(name="W/L Ratio", value=str(utils.comma(round(wins/losses, 2))), inline=True)
            except:
                embed.add_field(name="W/L Ratio", value=str('N/A'), inline=True)
            embed.add_field(name="Beds Lost", value=str(utils.comma(beds_lost)), inline=True)
            embed.add_field(name="Beds Broken", value=str(utils.comma(beds_broken)), inline=True)
            embed.add_field(name="Winstreak", value=str(utils.comma(winstreak)), inline=True)
            embed.set_footer(text=f'{bot.name} - Page 6/6', icon_url=bot.avatar_url)
            return embed

        async def generate(self, ctx, name, data, perms, bot: Optional[Member]):
            color = 0xB1FBFF
            main = await self.main(name, color, data, bot)
            solo = await self.solo(name, color, data, bot)
            doubles = await self.doubles(name, color, data, bot)
            threes = await self.threes(name, color, data, bot)
            fours = await self.fours(name, color, data, bot)
            fourfour = await self.fourfour(name, color, data, bot)
            paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=False)
            if perms is not None:
                if perms.manage_messages:
                    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=True)
            paginator.add_reaction('⏮️', "first")
            paginator.add_reaction('⏪', "back")
            paginator.add_reaction('⏹', "lock")
            paginator.add_reaction('⏩', "next")
            paginator.add_reaction('⏭️', "last")
            embeds = [main, solo, doubles, threes, fours, fourfour]
            return embeds, paginator

    class Skywars:
        async def main(self, name, color, data, bot):
            try:
                level = 'N/A'
                xp = data['player']['stats']['SkyWars']['skywars_experience']
                xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
                if xp >= 15000:
                    level = (xp - 15000) / 10000. + 12
                else:
                    for i in range(len(xps)):
                        if xp < xps[i]:
                            level = str(utils.comma(int(round(int(1 + i + float(xp - xps[i-1]) / (xps[i] - xps[i-1], 0)))))) + ' ⭐'
            except:
                level = 'N/A'
            try:
                games_played = data['player']['stats']['SkyWars']['games_played_skywars']
            except:
                games_played = 'N/A'
            try:
                winstreak = data['player']['stats']['SkyWars']['win_streak']
            except:
                winstreak = 'N/A'
            try:
                kills = data['player']['stats']['SkyWars']['kills']
            except:
                kills = 'N/A'
            try:
                deaths = data['player']['stats']['SkyWars']['deaths']
            except:
                deaths = 'N/A'
            try:
                top_winstreak = data['player']['stats']['SkyWars']['highestWinstreak']
            except:
                top_winstreak = 'N/A'
            try:
                coins = int(data['player']['stats']['SkyWars']['coins'])
            except:
                coins = 'N/A'
            try:
                souls = data['player']['stats']['SkyWars']['souls']
            except:
                souls = 'N/A'
            try:
                wins = data['player']['stats']['SkyWars']['wins']
            except:
                wins = 'N/A'
            try:
                losses = data['player']['stats']['SkyWars']['losses']
            except:
                losses = 'N/A'
            embed = discord.Embed(title=name + "'s Skywars Stats - Overall", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            try:
                embed.add_field(name="Skywars Level", value=str(int(level))+' ⭐', inline=True)
            except:
                embed.add_field(name="Skywars Level", value='N/A', inline=True)
            embed.add_field(name="Skywars Coins", value=str(utils.comma(coins)), inline=True)
            embed.add_field(name="Skywars Souls", value=str(utils.comma(souls)), inline=True)
            embed.add_field(name="Skywars Games Played", value=str(utils.comma(round(games_played, 0))), inline=True)
            embed.add_field(name="Skywars Winstreak", value=str(utils.comma(winstreak)), inline=True)
            embed.add_field(name="Skywars Highest Winstreak", value=str(utils.comma(top_winstreak)), inline=True)
            embed.add_field(name="Kills", value=str(utils.comma(kills)), inline=True)
            embed.add_field(name="Deaths", value=str(utils.comma(deaths)), inline=True)
            try:
                embed.add_field(name="K/D Ratio", value=str(utils.comma(round(int(kills)/int(deaths), 2))), inline=True)
            except:
                embed.add_field(name="K/D Ratio", value='N/A', inline=True)
            embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
            embed.add_field(name="Losses", value=str(utils.comma(losses)), inline=True)
            try:
                embed.add_field(name="W/L Ratio", value=str(utils.comma(round(int(wins)/int(losses), 2))), inline=True)
            except:
                embed.add_field(name="W/L Ratio", value='N/A', inline=True)
            embed.set_footer(text=f'{bot.name} - Page 1/6', icon_url=bot.avatar_url)
            return embed

        async def solon(self, name, color, data, bot):
            try:
                level = 'N/A'
                xp = data['player']['stats']['SkyWars']['skywars_experience']
                xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
                if xp >= 15000:
                    level = (xp - 15000) / 10000. + 12
                else:
                    for i in range(len(xps)):
                        if xp < xps[i]:
                            level = str(utils.comma(int(round(int(1 + i + float(xp - xps[i-1]) / (xps[i] - xps[i-1], 0)))))) + ' ⭐'
            except:
                level = 'N/A'
            try:
                games_played = data['player']['stats']['SkyWars']['games_played_skywars']
            except:
                games_played = 'N/A'
            try:
                winstreak = data['player']['stats']['SkyWars']['win_streak']
            except:
                winstreak = 'N/A'
            try:
                kills = data['player']['stats']['SkyWars']['kills_solo_normal']
            except:
                kills = 'N/A'
            try:
                deaths = data['player']['stats']['SkyWars']['deaths_solo_normal']
            except:
                deaths = 'N/A'
            try:
                top_winstreak = data['player']['stats']['SkyWars']['highestWinstreak']
            except:
                top_winstreak = 'N/A'
            try:
                coins = int(data['player']['stats']['SkyWars']['coins'])
            except:
                coins = 'N/A'
            try:
                souls = data['player']['stats']['SkyWars']['souls']
            except:
                souls = 'N/A'
            try:
                wins = data['player']['stats']['SkyWars']['wins_solo_normal']
            except:
                wins = 'N/A'
            try:
                losses = data['player']['stats']['SkyWars']['losses_solo_normal']
            except:
                losses = 'N/A'
            embed = discord.Embed(title=name + "'s Skywars Stats - Solo Normal", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            try:
                embed.add_field(name="Skywars Level", value=str(int(level))+' ⭐', inline=True)
            except:
                embed.add_field(name="Skywars Level", value='N/A', inline=True)
            embed.add_field(name="Skywars Coins", value=str(utils.comma(coins)), inline=True)
            embed.add_field(name="Skywars Souls", value=str(utils.comma(souls)), inline=True)
            embed.add_field(name="Skywars Games Played", value=str(utils.comma(games_played)), inline=True)
            embed.add_field(name="Skywars Winstreak", value=str(utils.comma(winstreak)), inline=True)
            embed.add_field(name="Skywars Highest Winstreak", value=str(utils.comma(top_winstreak)), inline=True)
            embed.add_field(name="Kills", value=str(utils.comma(kills)), inline=True)
            embed.add_field(name="Deaths", value=str(utils.comma(deaths)), inline=True)
            try:
                embed.add_field(name="K/D Ratio", value=str(utils.comma(round(int(kills)/int(deaths), 2))), inline=True)
            except:
                embed.add_field(name="K/D Ratio", value='N/A', inline=True)
            embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
            embed.add_field(name="Losses", value=str(utils.comma(losses)), inline=True)
            try:
                embed.add_field(name="W/L Ratio", value=str(utils.comma(round(int(wins)/int(losses), 2))), inline=True)
            except:
                embed.add_field(name="W/L Ratio", value='N/A', inline=True)
            embed.set_footer(text=f'{bot.name} - Page 2/6', icon_url=bot.avatar_url)
            return embed

        async def soloi(self, name, color, data, bot):
            try:
                level = 'N/A'
                xp = data['player']['stats']['SkyWars']['skywars_experience']
                xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
                if xp >= 15000:
                    level = (xp - 15000) / 10000. + 12
                else:
                    for i in range(len(xps)):
                        if xp < xps[i]:
                            level = str(utils.comma(int(round(int(1 + i + float(xp - xps[i-1]) / (xps[i] - xps[i-1], 0)))))) + ' ⭐'
            except:
                level = 'N/A'
            try:
                games_played = data['player']['stats']['SkyWars']['games_played_skywars']
            except:
                games_played = 'N/A'
            try:
                winstreak = data['player']['stats']['SkyWars']['win_streak']
            except:
                winstreak = 'N/A'
            try:
                kills = data['player']['stats']['SkyWars']['kills_solo_insane']
            except:
                kills = 'N/A'
            try:
                deaths = data['player']['stats']['SkyWars']['deaths_solo_insane']
            except:
                deaths = 'N/A'
            try:
                top_winstreak = data['player']['stats']['SkyWars']['highestWinstreak']
            except:
                top_winstreak = 'N/A'
            try:
                coins = int(data['player']['stats']['SkyWars']['coins'])
            except:
                coins = 'N/A'
            try:
                souls = data['player']['stats']['SkyWars']['souls']
            except:
                souls = 'N/A'
            try:
                wins = data['player']['stats']['SkyWars']['wins_solo_insane']
            except:
                wins = 'N/A'
            try:
                losses = data['player']['stats']['SkyWars']['losses_solo_insane']
            except:
                losses = 'N/A'
            embed = discord.Embed(title=name + "'s Skywars Stats - Solo Insane", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            try:
                embed.add_field(name="Skywars Level", value=str(int(level))+' ⭐', inline=True)
            except:
                embed.add_field(name="Skywars Level", value='N/A', inline=True)
            embed.add_field(name="Skywars Coins", value=str(utils.comma(coins)), inline=True)
            embed.add_field(name="Skywars Souls", value=str(utils.comma(souls)), inline=True)
            embed.add_field(name="Skywars Games Played", value=str(utils.comma(games_played)), inline=True)
            embed.add_field(name="Skywars Winstreak", value=str(utils.comma(winstreak)), inline=True)
            embed.add_field(name="Skywars Highest Winstreak", value=str(utils.comma(top_winstreak)), inline=True)
            embed.add_field(name="Kills", value=str(utils.comma(kills)), inline=True)
            embed.add_field(name="Deaths", value=str(utils.comma(deaths)), inline=True)
            try:
                embed.add_field(name="K/D Ratio", value=str(utils.comma(round(int(kills)/int(deaths), 2))), inline=True)
            except:
                embed.add_field(name="K/D Ratio", value='N/A', inline=True)
            embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
            embed.add_field(name="Losses", value=str(utils.comma(losses)), inline=True)
            try:
                embed.add_field(name="W/L Ratio", value=str(utils.comma(round(int(wins)/int(losses), 2))), inline=True)
            except:
                embed.add_field(name="W/L Ratio", value='N/A', inline=True)
            embed.set_footer(text=f'{bot.name} - Page 3/6', icon_url=bot.avatar_url)
            return embed

        async def doublesn(self, name, color, data, bot):
            try:
                level = 'N/A'
                xp = data['player']['stats']['SkyWars']['skywars_experience']
                xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
                if xp >= 15000:
                    level = (xp - 15000) / 10000. + 12
                else:
                    for i in range(len(xps)):
                        if xp < xps[i]:
                            level = str(utils.comma(int(round(int(1 + i + float(xp - xps[i-1]) / (xps[i] - xps[i-1], 0)))))) + ' ⭐'
            except:
                level = 'N/A'
            try:
                games_played = data['player']['stats']['SkyWars']['games_played_skywars']
            except:
                games_played = 'N/A'
            try:
                winstreak = data['player']['stats']['SkyWars']['win_streak']
            except:
                winstreak = 'N/A'
            try:
                kills = data['player']['stats']['SkyWars']['kills_team_normal']
            except:
                kills = 'N/A'
            try:
                deaths = data['player']['stats']['SkyWars']['deaths_team_normal']
            except:
                deaths = 'N/A'
            try:
                top_winstreak = data['player']['stats']['SkyWars']['highestWinstreak']
            except:
                top_winstreak = 'N/A'
            try:
                coins = int(data['player']['stats']['SkyWars']['coins'])
            except:
                coins = 'N/A'
            try:
                souls = data['player']['stats']['SkyWars']['souls']
            except:
                souls = 'N/A'
            try:
                wins = data['player']['stats']['SkyWars']['wins_team_normal']
            except:
                wins = 'N/A'
            try:
                losses = data['player']['stats']['SkyWars']['losses_team_normal']
            except:
                losses = 'N/A'
            embed = discord.Embed(title=name + "'s Skywars Stats - Doubles Normal", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            try:
                embed.add_field(name="Skywars Level", value=str(int(level))+' ⭐', inline=True)
            except:
                embed.add_field(name="Skywars Level", value='N/A', inline=True)
            embed.add_field(name="Skywars Coins", value=str(utils.comma(coins)), inline=True)
            embed.add_field(name="Skywars Souls", value=str(utils.comma(souls)), inline=True)
            embed.add_field(name="Skywars Games Played", value=str(utils.comma(games_played)), inline=True)
            embed.add_field(name="Skywars Winstreak", value=str(utils.comma(winstreak)), inline=True)
            embed.add_field(name="Skywars Highest Winstreak", value=str(utils.comma(top_winstreak)), inline=True)
            embed.add_field(name="Kills", value=str(utils.comma(kills)), inline=True)
            embed.add_field(name="Deaths", value=str(utils.comma(deaths)), inline=True)
            try:
                embed.add_field(name="K/D Ratio", value=str(utils.comma(round(int(kills)/int(deaths), 2))), inline=True)
            except:
                embed.add_field(name="K/D Ratio", value='N/A', inline=True)
            embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
            embed.add_field(name="Losses", value=str(utils.comma(losses)), inline=True)
            try:
                embed.add_field(name="W/L Ratio", value=str(utils.comma(round(int(wins)/int(losses), 2))), inline=True)
            except:
                embed.add_field(name="W/L Ratio", value='N/A', inline=True)
            embed.set_footer(text=f'{bot.name} - Page 4/6', icon_url=bot.avatar_url)
            return embed

        async def doublesi(self, name, color, data, bot):
            try:
                level = 'N/A'
                xp = data['player']['stats']['SkyWars']['skywars_experience']
                xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
                if xp >= 15000:
                    level = (xp - 15000) / 10000. + 12
                else:
                    for i in range(len(xps)):
                        if xp < xps[i]:
                            level = str(utils.comma(int(round(int(1 + i + float(xp - xps[i-1]) / (xps[i] - xps[i-1])), 0)))) + ' ⭐'
            except:
                level = 'N/A'
            try:
                games_played = data['player']['stats']['SkyWars']['games_played_skywars']
            except:
                games_played = 'N/A'
            try:
                winstreak = data['player']['stats']['SkyWars']['win_streak']
            except:
                winstreak = 'N/A'
            try:
                kills = data['player']['stats']['SkyWars']['kills_team_insane']
            except:
                kills = 'N/A'
            try:
                deaths = data['player']['stats']['SkyWars']['deaths_team_insane']
            except:
                deaths = 'N/A'
            try:
                top_winstreak = data['player']['stats']['SkyWars']['highestWinstreak']
            except:
                top_winstreak = 'N/A'
            try:
                coins = int(data['player']['stats']['SkyWars']['coins'])
            except:
                coins = 'N/A'
            try:
                souls = data['player']['stats']['SkyWars']['souls']
            except:
                souls = 'N/A'
            try:
                wins = data['player']['stats']['SkyWars']['wins_team_insane']
            except:
                wins = 'N/A'
            try:
                losses = data['player']['stats']['SkyWars']['losses_team_insane']
            except:
                losses = 'N/A'
            embed = discord.Embed(title=name + "'s Skywars Stats - Doubles Insane", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            try:
                embed.add_field(name="Skywars Level", value=str(int(level))+' ⭐', inline=True)
            except:
                embed.add_field(name="Skywars Level", value='N/A', inline=True)
            embed.add_field(name="Skywars Coins", value=str(utils.comma(coins)), inline=True)
            embed.add_field(name="Skywars Souls", value=str(utils.comma(souls)), inline=True)
            embed.add_field(name="Skywars Games Played", value=str(utils.comma(games_played)), inline=True)
            embed.add_field(name="Skywars Winstreak", value=str(utils.comma(winstreak)), inline=True)
            embed.add_field(name="Skywars Highest Winstreak", value=str(utils.comma(top_winstreak)), inline=True)
            embed.add_field(name="Kills", value=str(utils.comma(kills)), inline=True)
            embed.add_field(name="Deaths", value=str(utils.comma(deaths)), inline=True)
            try:
                embed.add_field(name="K/D Ratio", value=str(utils.comma(round(int(kills)/int(deaths), 2))), inline=True)
            except:
                embed.add_field(name="K/D Ratio", value='N/A', inline=True)
            embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
            embed.add_field(name="Losses", value=str(utils.comma(losses)), inline=True)
            try:
                embed.add_field(name="W/L Ratio", value=str(utils.comma(round(int(wins)/int(losses), 2))), inline=True)
            except:
                embed.add_field(name="W/L Ratio", value='N/A', inline=True)
            embed.set_footer(text=f'{bot.name} - Page 5/6', icon_url=bot.avatar_url)
            return embed

        async def lab(self, name, color, data, bot):
            try:
                level = 'N/A'
                xp = data['player']['stats']['SkyWars']['skywars_experience']
                xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
                if xp >= 15000:
                    level = (xp - 15000) / 10000. + 12
                else:
                    for i in range(len(xps)):
                        if xp < xps[i]:
                            level = str(utils.comma(int(round(int(1 + i + float(xp - xps[i-1]) / (xps[i] - xps[i-1], 0)))))) + ' ⭐'
            except:
                level = 'N/A'
            try:
                games_played = data['player']['stats']['SkyWars']['games_played_skywars']
            except:
                games_played = 'N/A'
            try:
                winstreak = data['player']['stats']['SkyWars']['win_streak']
            except:
                winstreak = 'N/A'
            try:
                kills = data['player']['stats']['SkyWars']['kills_lab']
            except:
                kills = 'N/A'
            try:
                deaths = data['player']['stats']['SkyWars']['deaths_lab']
            except:
                deaths = 'N/A'
            try:
                top_winstreak = data['player']['stats']['SkyWars']['highestWinstreak']
            except:
                top_winstreak = 'N/A'
            try:
                coins = int(data['player']['stats']['SkyWars']['coins'])
            except:
                coins = 'N/A'
            try:
                souls = data['player']['stats']['SkyWars']['souls']
            except:
                souls = 'N/A'
            try:
                wins = data['player']['stats']['SkyWars']['wins_lab']
            except:
                wins = 'N/A'
            try:
                losses = data['player']['stats']['SkyWars']['losses_lab']
            except:
                losses = 'N/A'
            embed = discord.Embed(title=name + "'s Skywars Stats - Laboratory", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            try:
                embed.add_field(name="Skywars Level", value=str(int(level))+' ⭐', inline=True)
            except:
                embed.add_field(name="Skywars Level", value='N/A', inline=True)
            embed.add_field(name="Skywars Coins", value=str(utils.comma(coins)), inline=True)
            embed.add_field(name="Skywars Souls", value=str(utils.comma(souls)), inline=True)
            embed.add_field(name="Skywars Games Played", value=str(utils.comma(games_played)), inline=True)
            embed.add_field(name="Skywars Winstreak", value=str(utils.comma(winstreak)), inline=True)
            embed.add_field(name="Skywars Highest Winstreak", value=str(utils.comma(top_winstreak)), inline=True)
            embed.add_field(name="Kills", value=str(utils.comma(kills)), inline=True)
            embed.add_field(name="Deaths", value=str(utils.comma(deaths)), inline=True)
            try:
                embed.add_field(name="K/D Ratio", value=str(utils.comma(round(int(kills)/int(deaths), 2))), inline=True)
            except:
                embed.add_field(name="K/D Ratio", value='N/A', inline=True)
            embed.add_field(name="Wins", value=str(utils.comma(wins)), inline=True)
            embed.add_field(name="Losses", value=str(utils.comma(losses)), inline=True)
            try:
                embed.add_field(name="W/L Ratio", value=str(utils.comma(round(int(wins)/int(losses), 2))), inline=True)
            except:
                embed.add_field(name="W/L Ratio", value='N/A', inline=True)
            embed.set_footer(text=f'{bot.name} - Page 6/6', icon_url=bot.avatar_url)
            return embed

        async def generate(self, ctx, name, data, perms, bot: Optional[Member]):
            color=0xB1FBFF
            main = await self.main(name, color, data, bot)
            solon = await self.solon(name, color, data, bot)
            soloi = await self.soloi(name, color, data, bot)
            doublesn = await self.doublesn(name, color, data, bot)
            doublesi = await self.doublesi(name, color, data, bot)
            lab = await self.lab(name, color, data, bot)
            paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=False)
            if perms is not None:
                if perms.manage_messages:
                    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=True)
            paginator.add_reaction('⏮️', "first")
            paginator.add_reaction('⏪', "back")
            paginator.add_reaction('⏹', "lock")
            paginator.add_reaction('⏩', "next")
            paginator.add_reaction('⏭️', "last")
            embeds = [main, solon, soloi, doublesn, doublesi, lab]
            return embeds, paginator

    class Help:
        async def botinfo(self, color, bot, ctx):
            role = discord.utils.find(lambda r: r.name == 'Admin', ctx.message.guild.roles)
            embed = discord.Embed(title='Help - Bot Info', description=botinfo + other, color=color)
            embed.set_footer(text=f'{bot.name} - Page 1/{"5" if role in ctx.author.roles else "4"}', icon_url=bot.avatar_url)
            return embed
        
        async def playerstats(self, color, bot, ctx):
            role = discord.utils.find(lambda r: r.name == 'Admin', ctx.message.guild.roles)
            embed = discord.Embed(title='Help - Player Stats', description=playerstats + other, color=color)
            embed.set_footer(text=f'{bot.name} - Page 2/{"5" if role in ctx.author.roles else "4"}', icon_url=bot.avatar_url)
            return embed

        async def hypixelstats(self, color, bot, ctx):
            role = discord.utils.find(lambda r: r.name == 'Admin', ctx.message.guild.roles)
            embed = discord.Embed(title='Help - Hypixel Stats', description=hypixelstats + other, color=color)
            embed.set_footer(text=f'{bot.name} - Page 3/{"5" if role in ctx.author.roles else "4"}', icon_url=bot.avatar_url)
            return embed

        async def mc(self, color, bot, ctx):
            role = discord.utils.find(lambda r: r.name == 'Admin', ctx.message.guild.roles)
            embed = discord.Embed(title='Help - Minecraft', description=minecraft + other, color=color)
            embed.set_footer(text=f'{bot.name} - Page 4/{"5" if role in ctx.author.roles else "4"}', icon_url=bot.avatar_url)
            return embed

        async def moderation(self, color, bot, ctx):
            role = discord.utils.find(lambda r: r.name == 'Admin', ctx.message.guild.roles)
            embed = discord.Embed(title='Help - Moderation', description=moderation + other, color=color)
            embed.set_footer(text=f'{bot.name} - Page 5/{"5" if role in ctx.author.roles else "4"}', icon_url=bot.avatar_url)
            return embed

        async def generate(self, ctx, perms, bot: Optional[Member]):
            role = discord.utils.find(lambda r: r.name == 'Admin', ctx.message.guild.roles)
            color = 0xB1FBFF
            one = await self.botinfo(color, bot, ctx)
            two = await self.playerstats(color, bot, ctx)
            three = await self.hypixelstats(color, bot, ctx)
            four = await self.mc(color, bot, ctx)
            if role in ctx.author.roles:
                five = await self.moderation(color, bot, ctx)
            paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=False)
            if perms is not None:
                if perms.manage_messages:
                    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=True)
            paginator.add_reaction('⏮️', "first")
            paginator.add_reaction('⏪', "back")
            paginator.add_reaction('⏹', "lock")
            paginator.add_reaction('⏩', "next")
            paginator.add_reaction('⏭️', "last")
            embeds = [one, two, three, four, five if role in ctx.author.roles else None]
            return embeds, paginator

    class PlayerCount:
        async def pages(self, color, data, bot):
            try:
                lobby = data['games']['MAIN_LOBBY']['players']
            except:
                lobby = 'N/A'
            try:
                tournament_lobby = data['games']['TOURNAMENT_LOBBY']['players']
            except:
                tournament_lobby = 'N/A'
            try:
                arcade = data['games']['ARCADE']['players']
            except:
                arcade = 'N/A'
            try:
                tnt_games = data['games']['TNTGAMES']['players']
            except:
                tnt_games = 'N/A'
            try:
                classic_games = data['games']['LEGACY']['players']
            except:
                classic_games = 'N/A'
            try:
                duels = data['games']['DUELS']['players']
            except:
                duels = 'N/A'
            try:
                uhc = data['games']['UHC']['players']
            except:
                uhc = 'N/A'
            try:
                warlords = data['games']['BATTLEGROUND']['players']
            except:
                warlords = 'N/A'
            try:
                housing = data['games']['HOUSING']['players']
            except:
                housing = 'N/A'
            try:
                bedwars = data['games']['BEDWARS']['players']
            except:
                bedwars = 'N/A'
            try:
                smash_heroes = data['games']['SUPER_SMASH']['players']
            except:
                smash_heroes = 'N/A'
            try:
                skyblock = data['games']['SKYBLOCK']['players']
            except:
                skyblock = 'N/A'
            try:
                blitz_survival_games = data['games']['SURVIVAL_GAMES']['players']
            except:
                blitz_survival_games = 'N/A'
            try:
                speed_uhc = data['games']['SPEED_UHC']['players']
            except:
                speed_uhc = 'N/A'
            try:
                build_battle = data['games']['BUILD_BATTLE']['players']
            except:
                build_battle = 'N/A'
            try:
                mega_walls = data['games']['WALLS3']['players']
            except:
                mega_walls = 'N/A'
            try:
                murder_mystery = data['games']['MURDER_MYSTERY']['players']
            except:
                murder_mystery = 'N/A'
            try:
                the_pit = data['games']['PIT']['players']
            except:
                the_pit = 'N/A'
            try:
                skywars = data['games']['SKYWARS']['players']
            except:
                skywars = 'N/A'
            try:
                replay = data['games']['REPLAY']['players']
            except:
                replay = 'N/A'
            try:
                cops_and_crims = data['games']['MCGO']['players']
            except:
                cops_and_crims = 'N/A'
            try:
                prototype = data['games']['PROTOTYPE']['players']
            except:
                prototype = 'N/A'
            try:
                limbo = data['games']['LIMBO']['players']
            except:
                limbo = 'N/A'
            try:
                idle = data['games']['IDLE']['players']
            except:
                idle = 'N/A'
            try:
                queue = data['games']['QUEUE']['players']
            except:
                queue = 'N/A'
            try:
                network = data['playerCount']
            except:
                network = 'N/A'
            embeds = []
            embed = discord.Embed(title="Hypixel Player Counts", color = color)
            embed.add_field(name='Total', value=str(utils.comma(network)))
            embed.add_field(name='Main Lobby', value=str(utils.comma(lobby)))
            embed.add_field(name='Tournament Lobby', value=str(utils.comma(tournament_lobby)))
            embed.set_footer(text=f'{bot.name} - Page 1/9', icon_url=bot.avatar_url)
            embeds.append(embed)

            embed = discord.Embed(title="Hypixel Player Counts", color = color)
            embed.add_field(name='Bedwars', value=str(utils.comma(bedwars)))
            embed.add_field(name='Skywars', value=str(utils.comma(skywars)))
            embed.add_field(name='Skyblock', value=str(utils.comma(skyblock)))
            embed.set_footer(text=f'{bot.name} - Page 2/9', icon_url=bot.avatar_url)
            embeds.append(embed)

            embed = discord.Embed(title="Hypixel Player Counts", color = color)
            embed.add_field(name='Arcade', value=str(utils.comma(arcade)))
            embed.add_field(name='Duels', value=str(utils.comma(duels)))
            embed.add_field(name='UHC', value=str(utils.comma(uhc)))
            embed.set_footer(text=f'{bot.name} - Page 3/9', icon_url=bot.avatar_url)
            embeds.append(embed)

            embed = discord.Embed(title="Hypixel Player Counts", color = color)
            embed.add_field(name='TNT Games', value=str(utils.comma(tnt_games)))
            embed.add_field(name='Classic Games', value=str(utils.comma(classic_games)))
            embed.add_field(name='Blitz Survival Games', value=str(utils.comma(blitz_survival_games)))
            embed.set_footer(text=f'{bot.name} - Page 4/9', icon_url=bot.avatar_url)
            embeds.append(embed)
            
            embed = discord.Embed(title="Hypixel Player Counts", color = color)
            embed.add_field(name='Build Battle', value=str(utils.comma(build_battle)))
            embed.add_field(name='Murder Mystery', value=str(utils.comma(murder_mystery)))
            embed.add_field(name='Housing', value=str(utils.comma(housing)))
            embed.set_footer(text=f'{bot.name} - Page 5/9', icon_url=bot.avatar_url)
            embeds.append(embed)

            embed = discord.Embed(title="Hypixel Player Counts", color = color)
            embed.add_field(name='Smash Heroes', value=str(utils.comma(smash_heroes)))
            embed.add_field(name='Speed UHC', value=str(utils.comma(speed_uhc)))
            embed.add_field(name='Mega Walls', value=str(utils.comma(mega_walls)))
            embed.set_footer(text=f'{bot.name} - Page 6/9', icon_url=bot.avatar_url)
            embeds.append(embed)

            embed = discord.Embed(title="Hypixel Player Counts", color = color)
            embed.add_field(name='The Pit', value=str(utils.comma(the_pit)))
            embed.add_field(name='Cops and Crims', value=str(utils.comma(cops_and_crims)))
            embed.add_field(name='Warlords', value=str(utils.comma(warlords)))
            embed.set_footer(text=f'{bot.name} - Page 7/9', icon_url=bot.avatar_url)
            embeds.append(embed)

            embed = discord.Embed(title="Hypixel Player Counts", color = color)
            embed.add_field(name='Prototype', value=str(utils.comma(prototype)))
            embed.add_field(name='Limbo', value=str(utils.comma(limbo)))
            embed.add_field(name='Replay', value=str(utils.comma(replay)))
            embed.set_footer(text=f'{bot.name} - Page 8/9', icon_url=bot.avatar_url)
            embeds.append(embed)

            embed = discord.Embed(title="Hypixel Player Counts", color = color)
            embed.add_field(name='Idle', value=str(utils.comma(idle)))
            embed.add_field(name='Queue', value=str(utils.comma(queue)))
            embed.set_footer(text=f'{bot.name} - Page 9/9', icon_url=bot.avatar_url)
            embeds.append(embed)
            return embeds

        async def generate(self, ctx, data, perms, bot: Optional[Member]):
            color=0xB1FBFF
            embeds = await self.pages(color, data, bot)
            paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=False)
            if perms is not None:
                if perms.manage_messages:
                    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=True)
            paginator.add_reaction('⏮️', "first")
            paginator.add_reaction('⏪', "back")
            paginator.add_reaction('⏹', "lock")
            paginator.add_reaction('⏩', "next")
            paginator.add_reaction('⏭️', "last")
            return embeds, paginator

    class Player:
        async def general(self, name, color, data, bot):
            try:
                #set rank to players rank
                rank = 'N/A'
                if "rank" in data["player"] and data["player"]["rank"] != "NORMAL":
                    rank = data["player"]["rank"]
                elif "monthlyPackageRank" in data["player"]:
                    if data['player']['monthlyPackageRank'] == "SUPERSTAR":
                        rank = "MVP++"
                elif "newPackageRank" in data["player"]:
                    rank = data["player"]["newPackageRank"]
                elif "packageRank" in data["player"]:
                    rank = data["player"]["packageRank"]
                else:
                    rank = "Default"
                if rank == "VIP_PLUS":
                    rank = "VIP+"
                elif rank == "MVP_PLUS":
                    rank = "MVP+"
                elif rank == "YOUTUBER":
                    rank = "YouTube"
                elif rank == "ADMIN":
                    rank = "Administrator"
                elif rank == "MODERATOR":
                    rank = "Moderator"
                elif rank == "HELPER":
                    rank = "Helper"
                else:
                    rank = 'N/A'
            except:
                rank = 'N/A'
            try:
                recent = utils.gameconverter(data['player']['mostRecentGameType'])
            except:
                recent = 'N/A'
            try:
                karma = data["player"]["karma"] if "karma" in data["player"] else 0
            except:
                karma = 'N/A'
            try:
                lastlogin = data['player']['lastLogin']
                lastlogout = data['player']['lastLogout']
                status = utils.timeconverter(lastlogin, lastlogout)
                if status is None:
                    status = 'N/A'
            except:
                status = 'N/A'
            try:
                level = utils.networklevel(data['player']['networkExp'])
            except:
                level = 'N/A'
            try:
                guild = await hypixel.playerguild(data['player']['_id'])
            except:
                guild = 'N/A'
            embed = discord.Embed(title=name + "'s Profile - General Info", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            embed.add_field(name="Rank", value=str(rank), inline=True)
            embed.add_field(name="Karma", value=str(utils.comma(karma)), inline=True)
            embed.add_field(name="Guild", value=str(utils.comma(guild)), inline=True)
            embed.add_field(name="Level", value=str(utils.comma(level)), inline=True)
            embed.add_field(name="Recently Played", value=str(recent), inline=True)
            embed.add_field(name="Status", value=str(status), inline=True)
            embed.set_footer(text=f'{bot.name} - Page 1/3', icon_url=bot.avatar_url)
            return embed

        async def social(self, name, color, data, bot):
            try:
                forums = data['player']['socialMedia']['links']['HYPIXEL']
            except:
                forums = 'None'
            try:
                discorda = data['player']['socialMedia']['links']['DISCORD']
            except:
                discorda = 'None'
            try:
                twitch = data['player']['socialMedia']['links']['TWITCH']
            except:
                twitch = 'None'
            try:
                ig = data['player']['socialMedia']['links']['INSTAGRAM']
            except:
                ig = 'None'
            try:
                youtube = data['player']['socialMedia']['links']['YOUTUBE']
            except:
                youtube = 'None'
            try:
                twitter = data['player']['socialMedia']['links']['TWITTER']
            except:
                twitter = 'None'
            embed = discord.Embed(title=name + "'s Profile - Social", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            embed.add_field(name="Hypixel Forums", value=str(forums), inline=False)
            embed.add_field(name="Discord", value=str(discorda), inline=False)
            embed.add_field(name="YouTube", value=str(youtube), inline=False)
            embed.add_field(name="Twitch", value=str(twitch), inline=False)
            embed.add_field(name="Twitter", value=str(twitter), inline=False)
            embed.add_field(name="Instagram", value=str(ig), inline=False)
            embed.set_footer(text=f'{bot.name} - Page 2/3', icon_url=bot.avatar_url)
            return embed

        async def other(self, name, color, data, bot):
            try:
                version = data['player']['mcVersionRp']
            except:
                version = 'N/A'
            try:
                achievementpoints = data['player']['achievementPoints']
            except:
                achievementpoints = 'N/A'
            try:
                pet = ''
                e = data['player']['currentPet'].lower().split('_')
                for i in e:
                    y = i.capitalize()
                    pet += f'{y} '
            except:
                pet = 'N/A'
            try:
                time = datetime.fromtimestamp(data['player']['firstLogin']/1000.0)
                first = time.strftime("%m/%d/%Y")
            except:
                first = 'N/A'
            try:
                aliases = ''
                for alias in data['player']['knownAliases']:
                    aliases += f"{alias}\n"
            except:
                aliases = 'N/A'
            try:
                uuid = data['player']['_id']
            except:
                uuid = 'N/A'
            embed = discord.Embed(title=name + "'s Profile - Social", color=color)
            embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{data['player']['_id']}")
            embed.add_field(name="First Joined", value=str(first), inline=True)
            embed.add_field(name="UUID", value=str(uuid), inline=True)
            embed.add_field(name="Recently Played Version", value=str(version), inline=True)
            embed.add_field(name="Achievement Points", value=str(utils.comma(achievementpoints)), inline=True)
            embed.add_field(name="Current Pet", value=str(pet), inline=True)
            embed.add_field(name="Known Aliases", value=str(aliases), inline=True)
            embed.set_footer(text=f'{bot.name} - Page 3/3', icon_url=bot.avatar_url)
            return embed

        async def generate(self, ctx, name, data, perms, bot: Optional[Member]):
            color = 0xB1FBFF
            general = await self.general(name, color, data, bot)
            social = await self.social(name, color, data, bot)
            other = await self.other(name, color, data, bot)
            paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=False)
            if perms is not None:
                if perms.manage_messages:
                    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, timeout=60, remove_reactions=True)
            paginator.add_reaction('⏮️', "first")
            paginator.add_reaction('⏪', "back")
            paginator.add_reaction('⏹', "lock")
            paginator.add_reaction('⏩', "next")
            paginator.add_reaction('⏭️', "last")
            embeds = [general, social, other]
            return embeds, paginator