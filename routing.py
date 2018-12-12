# -*- coding: utf-8 -*-
from hello.main import say_hello

def message(commandList,client,message):
    #ここにメッセージを解析して処理を呼び出す処理を書こう！！
    if(commandList[1] == 'hello'):
        say_hello(client,message)
