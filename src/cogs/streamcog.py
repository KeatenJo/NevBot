class StreamCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="used to send out announcements about community streams.")
    @commands.has_role("Streamer friends")
    async def shoutout(self, ctx, url, message):
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

    @commands.command(description="For use by Neviation for announcing streams")
    @commands.has_role("Admins")
    async def stream(self, ctx):
        embed = discord.Embed(title="Hey Everyone! I'm Going Live!", description="https://www.twitch.tv/neviation", color=0x00ff00)
        
        embed.set_footer(text="Come hang out!")
        
        embed.set_image(url="https://static-cdn.jtvnw.net/jtv_user_pictures/e4661b3573a84f0b-profile_image-70x70.jpeg")
        
        embed.set_thumbnail(url="https://static-cdn.jtvnw.net/jtv_user_pictures/e4661b3573a84f0b-profile_image-70x70.jpeg")
        for guild in bot.guilds:
            for channel in guild.channels:
                if channel.name == 'stream-announcements':
                    await channel.send("@everyone ", embed=embed)

############################# Setup bot #########################################
def setup(bot):
    bot.add_cog(StreamCog(bot))

#################################################################################
