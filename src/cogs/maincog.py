from discord.ext import commands
import discord
import asyncio
import os
import random

class MainCog(commands.Cog):
    def __init__(self, bot ):
        self.bot = bot
        self.slurrs = ["nigger", "coon", "nigga", "white trash", "yellow skin", "wetback", "spick", "chink", "beaner", "izzy"]
        self.message_cache = []
        self.message_count = 0
        self.same_message_count = 0


    async def on_ready(self):
        print("ScrapBot is Ready.")

    async def on_member_join(self, member):
        await member.send("Welcome to the server " + str(member) + " !")
    
    async def on_message(self, message):
        if(self.message_count > 20 ):
            self.message_count = 0 
            self.message_cache[self.message_count] = message
        else:
            self.message_cache[self.message_count] = message
            self.message_count += 1
        
        checkword = self.message_cache[0]
        sameword = 0
        for i in range(len(self.message_cache)):
            if(checkword.content == self.message_cache[i].content):
                sameword += 1
            else:
                sameword = 0
                checkword = self.message_cache[i]

            if(sameword == 3):
                await message.channel.send(checkword.content)
        if(sameword == 2):
            await message.channel.send("Jinx!")



############################# Setup Bot #####################################
def setup(bot):
    bot.add_cog(MainCog(bot))

############################ Helper Functions ###############################

