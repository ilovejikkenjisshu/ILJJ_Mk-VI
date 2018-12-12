import discord


async def say_hello(client, message):
    # メッセージ作成
    m = message.author.name + " : hello"
    # メッセージが送られてきたチャンネルへメッセージを送ります
    await client.send_message(message.channel, m)
