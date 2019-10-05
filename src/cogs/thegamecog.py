from discord.ext import commands
import discord
import asyncio
import os
import random


class TheGameCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.times_lost = 0
        self.come_backs = ["Booyah! I lost the game, and so did you!", "Boom Eat it, you all lost!", "Sweet I won-- oh wait...", "-____-", "Come on, why?", "Again, Really?", "This game sucks.", "I'm not very good at this.", "My creator didn't make me just lose your silly games!", "I am ScrapBot, and I have lost this game. :("]

    @commands.command()
    async def ilost(self, ctx, user: discord.Member=None):
        if user: 
            message = "{0.name} ".format(ctx.author) + "made you lose the game " + "{}".format(user.name) + "!"
            self.times_lost += 1
            await ctx.send(message)
        else:
            r = random.randrange(len(self.come_backs)-1)
            message = self.come_backs[r]
            self.times_lost += 1
            await ctx.send(message)

    @commands.command()
    async def stats(self, ctx):
        await ctx.send("I have lost the game " + str(self.times_lost) + " time(s)!")


############################################# Setup Bot ###################################
def setup(bot):
    bot.add_cog(TheGameCog(bot))
