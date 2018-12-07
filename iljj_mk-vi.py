# -*- coding: utf-8 -*-

import discord
import os
import datetime
import my_token

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    pass

# token にデベロッパサイトで取得したトークンを入れる
client.run(my_token)