from discord.ext import commands
import discord
import asyncio
import os
import random

class GeneralCog:
    def __init__( self, bot ):
        self.bot = bot

    @commands.command(description="Rolls a dice in NdN format.")
    async def roll(self, ctx, dice: str):
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)\

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong')
    
    @commands.command()
    async def Hello(self, ctx):
        await ctx.send('Hello right back, {0.name}!'.format(ctx.author))

    @commands.command()
    async def test(ctx):
        await ctx.send('I heard you! {0.name}'.format(ctx.author))

    @commands.command(description='For when you wanna settle the score some other way')
    async def choose(self, ctx, *choices: str):
        await ctx.send(random.choice(choices))

    @commands.command()
    async def ohai(self, ctx):
        await ctx.send(":P")

    @commands.command()
    async def awoo(self, ctx):
        await ctx.send("*Awoos Softly*")

    

########################### Setup Bot #######################################
def setup(bot):
    bot.add_cog(GeneralCog(bot))
#############################################################################
