import discord
import asyncio
import os
import random
from keep_alive import keep_alive
from discord.ext import commands


bot = commands.Bot(command_prefix='!', case_insensitive=True)

taught_comands = []


@bot.event
async def on_ready():
  print("Bot is Ready.")

@bot.event
async def on_member_join(member):
    await member.send("Welcome to the server " + str(member) + " !")

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  if "bob" in message.content.lower():
    await message.delete()
    await message.channel.send("You're not Bob!")
  await bot.process_commands(message)

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

@bot.command()
async def ohai(ctx):
  await ctx.send(":P")

@bot.command()
async def awoo(ctx):
  await ctx.send("*Awoos Softly*")

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
