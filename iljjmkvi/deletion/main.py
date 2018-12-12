import discord


class DeletionModule:
    async def on_message(self, client, message):
        from asyncio import sleep

        await client.delete_message(message)
        message = await client.send_message(message.channel, 'Message is deleted. This message will be deleted in 3 seconds.')
        await sleep(3)
        await client.delete_message(message)



