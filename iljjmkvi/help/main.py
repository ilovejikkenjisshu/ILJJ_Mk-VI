import discord


class Module:
    async def on_message(self, client, message):
        cmds = client.get_all_commands()

        await client.send_message(message.channel, ' '.join(cmds.keys()))

