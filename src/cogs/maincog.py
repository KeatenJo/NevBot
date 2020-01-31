from discord.ext import commands
import discord
import asyncio
import os
import random

class MainCog(commands.Cog):
    def __init__(self, bot ):
        self.bot = bot
        self.message_cache = []
        self.message_count = 0
        self.same_message_count = 0


    async def on_ready(self):
        print("ScrapBot is Ready.")

    async def on_member_join(self, member):
        await member.send("Welcome to the server " + str(member) + " !")

    @commands.Cog.listener() 
    async def on_message(self, message):

        if message.author == self.bot:
            return
        
        if(self.message_count > 10 ):
            self.message_count = 0 

        self.message_cache.insert(self.message_count, message)
        self.message_count += 1
        
        checkword = self.message_cache[self.message_count-1]
        jinx = False
        if(self.message_count == 1 and len(self.message_cache) >= self.message_count  ):
            if(self.message_cache[len(self.message_cache)-1].content == checkword.content):
                jinx = True
        else:
            if(self.message_cache[self.message_count-1].content == self.message_cache[self.message_count-2].content):
                jinx = True

        if(jinx):
            await message.channel.send("Jinx!")


        



############################# Setup Bot #####################################
def setup(bot):
    bot.add_cog(MainCog(bot))

############################ Helper Functions ###############################

