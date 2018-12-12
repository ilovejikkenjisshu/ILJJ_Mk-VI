import discord


class ILJJ_Mk_VI(discord.Client):
    def __init__(self, settings):
        from importlib import import_module

        super().__init__()

        # save settings
        self.settings = settings

        # Load commands
        cmds = settings['commands']
        self.commands = { k: import_module('iljjmkvi.' + cmds[k]['module']).Module() for k in cmds }


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

    def get_all_commands(self):
        return self.commands

