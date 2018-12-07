# -*- coding: utf-8 -*-

import discord
import os
import datetime
import my_token
import re

client = discord.Client()
reminder = []

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith("MK-VI"):
            await client.send_message(message.channel,'hello^_^ \n 管理AI権限くださいな')

    if message.content.startswith("$MK-VI.リマインド:") or message.content.startswith("$MK-VI.remind:"):
        # Botだった場合反応しない
        if client.user != message.author:
            #メッセージ内容を取得
            ms = message.content
                
            #：でメッセージを分割
            ms_list = ms.split(":",1)

            reminder.append(ms_list[1])           

            # メッセージ作成
            m = "@"+message.author.name + " リマインドしました"

            # メッセージが送られてきたチャンネルへメッセージ送信
            await client.send_message(message.channel, m)

    if message.content.startswith("$MK-VI.リマインドリスト") or message.content.startswith("$MK-VI.remind_list"):
        # Botだった場合反応しない
        if client.user != message.author:
            ms = ""
            for data in reminder:
                ms += data + "\n"
            # メッセージが送られてきたチャンネルへメッセージ送信
            await client.send_message(message.channel, ms)

    if message.content.startswith("$MK-VI.リマインド削除") or message.content.startswith("$MK-VI.remind_clear"):
        # Botだった場合反応しない
        if client.user != message.author:
            ms = "リマインドをすべて削除しました"
            reminder.clear()
            await client.send_message(message.channel, ms)
    

client.run(my_token.my_token)