# Botsche

My personal Discord Bot.

To run this bot, change `<TOKEN>` in `config.ini` to your Discord Bot Token, which can be retrieved from your Discord Developer Portal.     
`<API KEY>` will also need to be changed to your Hypixel API Key, which can be created by connecting to the Minecraft server `mc.hypixel.net` and running the `/api new` command. 

If you wish, you may also change `<LOG CHANNEL ID>` in `config.ini` to a Discord channel ID. Bot events, errors, etc will be sent to the specified channel.

This bot retrieves statistics from the official public [Hypixel API](https://api.hypixel.net). Documentation for the API can be found [here](https://github.com/HypixelDev/PublicAPI/tree/master/Documentation).

# License
[matsivoss/Botschiee](https://github.com/matsivoss/Botschiee) is licensed under the MIT License. This license can be viewed [here](https://github.com/MatsiVoss/Botschiee/blob/main/README.md).

# Disclaimer
This bot is in no way affiliated with or endorsed by [Hypixel, Inc](https://hypixel.net). All logos, brands, trademarks, and registered trademarks are property of their respective owners.

# Requirements
- [mojang](https://pypi.org/project/mojang/)

- [discord.py](https://pypi.org/project/discord.py/)

# Commands

## Restricted Commands
- `h!load <extension>` - Load an extension.

- `h!unload <extension>` - Unload an extension.

- `h!reload <extension>` - Reload an extension.

- `h!stop` - Stop the bot.

- `h!logs` - Uploads the logs to [mystbin](https://mystb.in) and DMs them to you.

- `h!eval <code>` - Evaluates Python code. This can be used with code blocks as well.