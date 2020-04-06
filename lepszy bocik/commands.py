from core import bbot
import asyncio

bot = bbot.bot


@bot.event
async def on_message(msg):
    if msg.content.startswith("-"):
        await msg.delete()
    else:
        await bot.process_commands(msg)

@bot.command()
async def clear(ctx, num):
    num = int(num)
    await ctx.channel.purge(limit=num + 1)