
# DiscordChannels.py
 
import discord
import datetime
client = discord.Client()
 
# 起動時処理
@client.event
async def on_ready():
    for channel in client.get_all_channels():
        print("----------")
        print("チャンネル名：" + str(channel.name))
        print("チャンネルID：" + str(channel.id))
        print("----------")

# チャンネル入退室時の通知処理
@client.event
async def on_voice_state_update(member, before, after):
 
    # チャンネルへの入室ステータスが変更されたとき（ミュートON、OFFに反応しないように分岐）
    if before.channel != after.channel:
        # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
        botRoom = client.get_channel(get_file_text('text_channel'))
 
        # 入退室を監視する対象のボイスチャンネル（チャンネルIDを指定）
        announceChannelIds = [get_file_text('voice_channel')]

        # 現在時刻
        t_delta = datetime.timedelta(hours=9)
        JST = datetime.timezone(t_delta, 'JST')
        now = datetime.datetime.now(JST)
        d = now.strftime('%Y/%m/%d %H:%M:%S')

        # 退室通知
        if before.channel is not None and before.channel.id in announceChannelIds:
            await botRoom.send("[" + d + "] **" + before.channel.name + "** から、__" + member.name + "__  が抜けました！")
        # 入室通知
        if after.channel is not None and after.channel.id in announceChannelIds:
            await botRoom.send("[" + d + "] **" + after.channel.name + "** に、__" + member.name + "__  が参加しました！")

def get_file_text(file_path):
    if file_path is None:
        return None
    f = open(file_path, 'r', encoding='UTF-8')
    text = f.read()
    f.close()
    return text

if __name__ == '__main__':
    # Botのトークンを指定（デベロッパーサイトで確認可能）
    client.run(get_file_text('token'))
