import discord
import os

import motor.motor_asyncio
from discord_components import DiscordComponents

from discord.ext import commands
from configparser import ConfigParser

from botUtils.utils import con
from botUtils.mongo import Document

logs = con()
logs.start()
logs.log("Starting bot...")

intents = discord.Intents.all()
parser = ConfigParser()
parser.read('config.ini')
TOKEN = parser.get('CONFIG', 'token')
try:
    logchannel = int(parser.get('CONFIG', 'log_channel'))
except Exception as e:
    print(f"Couldn't define logchannel: {e}")
    logchannel = None
try:
    connection_url = parser.get('CONFIG', 'mongoDB')
except Exception as e:
    print(f"Couldn't define connection_url: {e}")
    connection_url = None


async def get_prefix(bots, message):
    if not message.guild:
        return commands.when_mentioned_or("+")(bots, message)

    try:
        data = await bot.config.find(message.guild)

        if not data or "prefix" not in data:
            return commands.when_mentioned_or("+")(bots, message)
        return commands.when_mentioned_or(data["prefix"])(bots, message)
    except:
        return commands.when_mentioned_or("+")(bots, message)


bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, intents=intents,
                   owner_ids=[459346559658622976, 525019379872563200])
bot.remove_command('help')
color = 0xB1FBFF

bot.muted_users = {}


@bot.event
async def on_ready():
    logs.log('Successfully logged in as ' + bot.user.name + ' | ' + str(bot.user.id) + '.')
    DiscordComponents(bot)
    bot.mongo = motor.motor_asyncio.AsyncIOMotorClient(str(connection_url))
    bot.db = bot.mongo["Name"]
    bot.config = Document(bot.db, "config")
    bot.mutes = Document(bot.db, "mutes")
    for document in await bot.config.get_all():
        print(document)

    currentMutes = await bot.mutes.get_all()
    for mute in currentMutes:
        bot.muted_users[mute["_id"]] = mute

    print(bot.muted_users)

    logs.log('Successfully initialized MongoDB-Database')

    if logchannel is not None:
        channel = bot.get_channel(logchannel)
        if channel is not None:
            embed = discord.Embed(title=f"Bot Started", description=f"```\nSuccessfully started the bot.\n```",
                                  color=0x00ff00)
            try:
                await channel.send(embed=embed)
            except discord.Forbidden:
                raise ValueError(
                    "The bot does not have permissions to send messages in the logchannel specified in botconfig.ini.")
        else:
            raise ValueError("The logchannel specified in botconfig.ini is not visible to the bot, or does not exist.")
    return


def load_extension(extension):
    ext = extension.replace('/', '.')
    try:
        bot.load_extension(ext)
        logs.log(f"{ext} loaded.")
    except Exception as e:
        logs.log(f"Couldn't load {ext}: {e}")


for dir_name in ["commands", "commands/owner", "commands/user", "commands/moderation", "events", "tasks"]:
    for file in os.listdir(dir_name):
        if file.endswith(".py"):
            load_extension(f"{dir_name}.{file}".replace('.py', ''))

logs.log('Logging In...')
try:
    bot.run(TOKEN, bot=True, reconnect=True)
except Exception as e:
    logs.log(str(e))
