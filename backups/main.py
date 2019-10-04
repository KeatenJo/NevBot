import discord
import asyncio
import os
import random
from keep_alive import keep_alive
from discord.ext import commands


bot = commands.Bot(command_prefix='!', case_insensitive=True)

bot.load_extension("cogs.maincog")






@bot.command(description="Rolls a dice in NdN format.")
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description="used to send out announcements about community streams.")
@commands.has_role("Streamer friends")
async def shoutout(ctx, url, message):
    if url and message:
      string = '@everyone'+ " " + url + " " + message
      for guild in bot.guilds:
          for channel in guild.channels:
              if channel.name == "community-streams-and-youtube-channels":
                await channel.send(string)
    elif url and message is None :
      string = '@everyone'+ " " + url
      for guild in bot.guilds:
          for channel in guild.channels:
              if channel.name == "community-streams-and-youtube-channels":
                await channel.send(string)
    else:
      string = '@everyone' + ' ' + message
      await ctx.send(string)


@bot.command(description="For use by Neviation for announcing streams")
@commands.has_role("Admins")
async def stream(ctx):

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
  return
  #bot.user.setGame("Nev is Streaming!", "https://www.twitch.tv/neviation")

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
    await ctx.send(random.choice(choices))

@bot.command()
async def ohai(ctx):
  await ctx.send(":P")

@bot.command()
async def awoo(ctx):
  await ctx.send("*Awoos Softly*")

@bot.command()
async def ilost(ctx):
  await ctx.send("Booyah! I lost the game, and so did you!")

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
