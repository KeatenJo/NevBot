import discord
import asyncio
import os
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    print("The bot is ready!")

@client.event
async def on_message(message):
  author = message.author
  if message.content.startswith('!test'):
    print('on_message !test')
    await test(author, message)
  
  if message.content.startswith('!Hello'):
    print('on_message !hello')
    await hello(author, message)

async def hello(author, message):
  await message.channel.send('Hello right back! {0.name}'.format(author))

async def test(author, message):
  await message.channel.send('I heard you! {0.name}'.format(author))

keep_alive()
token = os.environ.get("BOT_SECRET")
client.run(token)