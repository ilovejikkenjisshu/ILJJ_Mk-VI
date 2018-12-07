# -*- coding: utf-8 -*-

import discord
import os
import datetime
import my_token
import re

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    ms = message.content
    if re.match('.*:quit_internet:.*',ms):
        message.delete()     
        await message.channel.send(':dlyfmcuo:')

client.run(my_token)