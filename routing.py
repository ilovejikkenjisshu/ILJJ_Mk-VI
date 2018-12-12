

def message(message,client):
    #ここにメッセージを解析して処理を呼び出す処理を書こう！！
    # 送り主がBotだった場合反応しない
        if client.user != message.author:
            if message.content.startswith('mkvi'):
                pass
