import discord


class Module:
    async def on_message(self, client, message):
        # メッセージ作成
        m = message.author.name + " : hello"
        # メッセージが送られてきたチャンネルへメッセージを送ります
        await client.send_message(message.channel, m)

