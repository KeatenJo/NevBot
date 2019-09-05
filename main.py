import discord
import asyncio
import os
import random
from keep_alive import keep_alive
from discord.ext import commands


bot = commands.Bot(command_prefix='!', case_insensitive=True)

taught_comands = []
slurrs = ["nigger", "coon", "nigga", "white trash", "yellow skin", "wetback", "spick", "chink", "beaner", "izzy"]

async def checkSlurrs(message):
  lower_message = message.content.lower()
  split = lower_message.split()
  for i in range(len(slurrs)):
    for j in range(len(split)):
      if slurrs[i] == split[j]:
        return True
  return


@bot.event
async def on_ready():
  print("ScrapBot is Ready.")

@bot.event
async def on_member_join(member):
    await member.send("Welcome to the server " + str(member) + " !")


@bot.event
async def on_message(message):
  slurs = False
  slurs = await checkSlurrs(message)
  if slurs:
    await message.delete()
    await message.channel.send(str(message.author) +" is a racist!")
  
  
  if message.author == bot.user:
    return
  
  if message.content.lower() in slurrs:
    await message.delete()
    await message.channel.send(str(message.author) +" is a racist!")
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
@commands.has_role("Streamer friends")
async def shoutout(ctx, url, message):
    """Used to send out announcements about community streams. Context: !shoutout < url > < message > ( Both url and message is optional but only one at a time. )"""

    if url and message:
      string = '@everyone'+ " " + url + " " + message
      for guild in bot.guilds:
          for channel in guild.channels:
              if channel.name == "stream-announcements":
                await channel.send(string)
    elif url and message is None:
      string = '@everyone'+ " " + url
      for guild in bot.guilds:
          for channel in guild.channels:
              if channel.name == "stream-announcements":
                await channel.send(string)
    else:
      string = '@everyone' + ' ' + message
      await ctx.send(string)


@bot.command()
@commands.has_role("Admins")
async def stream(ctx):
  """Used for announcing Neviations Streams Exclusively."""

  embed = discord.Embed(title="Hey Everyone! I'm Going Live!", description="https://www.twitch.tv/neviation", color=0x00ff00)

  embed.set_footer(text="Come hang out!")

  embed.set_image(url="https://static-cdn.jtvnw.net/jtv_user_pictures/e4661b3573a84f0b-profile_image-70x70.jpeg")


  embed.set_thumbnail(url="https://static-cdn.jtvnw.net/jtv_user_pictures/e4661b3573a84f0b-profile_image-70x70.jpeg")
  for guild in bot.guilds:
    for channel in guild.channels:
      if channel.name == 'stream-announcements':
        #await channel.send('@everyone ', embed=embed)
        await channel.send("@everyone ", embed=embed)


@bot.command()
async def testStream(ctx):
  """testing purposes does nothing right now"""
  return
  bot.user.setGame("Nev is Streaming!", "https://www.twitch.tv/neviation")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def Hello(ctx):
  await ctx.send('Hello right back, {0.name}!'.format(ctx.author))

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
