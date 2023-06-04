import discord
import os

from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print('We have loggd in as {0.user}'.format(client))


@client.event
async def on_message(message: discord.Message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')


keep_alive()
client.run(os.getenv('TOKEN'))
