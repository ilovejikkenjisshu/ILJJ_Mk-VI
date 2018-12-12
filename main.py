# -*- coding: utf-8 -*-

import discord
import os
import datetime
import my_token
import re
import routing

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message,client):
    # 送り主がBotだった場合反応しない
    if client.user != message.author:
        if message.content.startswith('!mkvi'):
            pass

    

client.run(my_token.my_token)