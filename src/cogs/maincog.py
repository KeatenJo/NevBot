from discord.ext import commands
import discord
import asyncio
import os
import random

class MainCog(commands.Cog):
    def __init__(self, bot ):
        self.bot = bot
        self.slurrs = ["nigger", "coon", "nigga", "white trash", "yellow skin", "wetback", "spick", "chink", "beaner", "izzy"]

    async def on_ready(self):
        print("ScrapBot is Ready.")

    async def on_member_join(self, member):
        await member.send("Welcome to the server " + str(member) + " !")
    
    async def on_message(self, message):
        slurs = False
        slurs = await checkSlurrs(message, self.slurrs)
        if slurs:
            await message.delete()
            await message.channel.send(str(message.author) +" is a racist!")
        if message.author == bot.user:
            return
        if message.content.lower() in slurrs:
            await message.delete()
            await message.channel.send(str(message.author) +" is a racist!")


############################# Setup Bot #####################################
def setup(bot):
    bot.add_cog(MainCog(bot))

############################ Helper Functions ###############################
async def checkSlurrs(message, slurrs):
    lower_message = message.content.lower()
    split = lower_message.split()
    for i in range(len(slurrs)):
        for j in range(len(split)):
            if slurrs[i] == split[j]:
                return True
    return

