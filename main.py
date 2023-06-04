##############################################
# Botメイン処理
# 詳細はdiscord.pyのリファレンス参照
##############################################

import discord
import os

from keep_alive import keep_alive
from discord_client import BotClient

# 権限関係の設定
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

keep_alive()

client = BotClient(intents=intents)
client.run(os.getenv('TOKEN'))
