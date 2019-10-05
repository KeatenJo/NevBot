import discord
import asyncio
import os
import random
from keep_alive import keep_alive
from discord.ext import commands


bot = commands.Bot(command_prefix='!', case_insensitive=True)

bot.load_extension("cogs.maincog")
bot.load_extension("cogs.streamcog")
bot.load_extension("cogs.generalcog")
bot.load_extension("cogs.thegamecog")

#@bot.command(description="Teach me a command!")
#async def teach(ctx, *args: str):
#   try:
#        name, function = map(int, args.split(''))
#    except Exception:
#        await ctx.send('Format has to be in Name Function!')
#        return
  
keep_alive()
token = os.environ.get("BOT_SECRET")
bot.run(token)
