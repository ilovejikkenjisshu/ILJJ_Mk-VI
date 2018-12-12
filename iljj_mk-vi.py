# -*- coding: utf-8 -*-

import discord
import os
import datetime
import my_token
import re
import routing

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
    message(message)

    

client.run(my_token.my_token)