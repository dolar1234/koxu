import discord
from discord.ext import commands

prefix = "!"
main_color = 0x43e86f
log_channel = 695170174021795881 

class bbot:
    bot = commands.Bot(command_prefix=prefix)
    def __init__(self, token):
        print("Starting bot...")
        bbot.bot.run(token)


    @bot.event
    async def on_ready():
        import commands
        print(f"\nLogged in as: {bbot.bot.user.name} - {bbot.bot.user.id}\nVersion: {discord.__version__}\n")
        await bbot.log(f"**{bbot.bot.user.name}** has been initialized | Version: **{discord.__version__}**")

    async def log(message):
        embed = discord.Embed(
            color = main_color,
            description = message
        )
        ch = bbot.bot.get_channel(log_channel)
        await ch.send(embed=embed)

