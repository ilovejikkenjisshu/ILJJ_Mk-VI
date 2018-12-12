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
async def on_message(message):
    # 送り主がBotだった場合反応しない
    if client.user != message.author:
        #コマンド判定
        if message.content.startswith('!mkvi'):
            command = message.content
            commandlist = command.split()
            await routing.message(commandlist,client,message)

    

client.run(my_token.my_token)
