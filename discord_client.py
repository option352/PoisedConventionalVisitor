##############################################
# discord.Clientを使ってBotを作る
##############################################

import discord
import commands


class BotClient(discord.Client):

  async def on_ready(self):
    """
      BOTが利用可能になった時の処理
    """
    print("{0.user}としてログインしました".format(self))

  async def on_message(self, message: discord.Message):
    """
      メッセージが書き込まれた時の処理
      discord.Intent.messagesが必要
    """
    # 自分自身の発言に反応しないように
    if message.author == self.user:
      return

    if message.content.startswith('!hello'):
      await message.channel.send('Hello!')

    if any(u for u in message.mentions if u.id == self.user.id):
      print("{0}からメンションが飛ばされました".format(message.author.name))
      await message.channel.send(commands.roll_dice(6, 3))

    if message.content.startswith('!こんにちは'):
      await message.channel.send("{0}さんこんにちは！".format(message.author.name))
