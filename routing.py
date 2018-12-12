# -*- coding: utf-8 -*-
from hello.main import say_hello

async def message(commandList,client,message):
    #ここにメッセージを解析して処理を呼び出す処理を書こう！！
    if(commandList[1] == 'hello'):
        await say_hello(client,message)
