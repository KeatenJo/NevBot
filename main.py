import discord
import asyncio
import os
import random
from keep_alive import keep_alive
from discord.ext import commands


bot = commands.Bot(command_prefix='!', case_insensitive=True)

@bot.event
async def on_ready():
  print("Bot is Ready.")

@bot.command()
async def bob(ctx):
  await ctx.send('You\'re not Bob!')

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def Hello(ctx):
  await ctx.send('Hello right back! {0.name}'.format(ctx.author))

@bot.command()
async def test(ctx):
  await ctx.send('I heard you! {0.name}'.format(ctx.author))

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))




keep_alive()
token = os.environ.get("BOT_SECRET")
bot.run(token)
