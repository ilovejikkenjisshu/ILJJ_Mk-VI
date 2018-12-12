# -*- coding: utf-8 -*-

import discord


class ILJJ_Mk_VI(discord.Client):
    def __init__(self, settings):
        super().__init__()

        from importlib import import_module

        self.commands = { k: import_module(v).Module() for k, v in settings.items() }


    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')


    async def on_message(self, message):
        # 送り主がBotだった場合反応しない
        if self.user != message.author:
            #コマンド判定
            if message.content.startswith('!mkvi'):
                argv = message.content.split()
                await self.commands[argv[1]].on_message(self, message)


def main():
    client = ILJJ_Mk_VI({'hello': 'hello'})
    client.run(my_token.my_token)

if __name__ == '__main__':
    main()


