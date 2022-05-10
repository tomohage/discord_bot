# discord_bot
ディスコードのボイスチャンネルの入退出のログをテキストチャンネルに書き出すbot

こちらのコードを参考にしました　https://tech-cci.io/archives/6412

チャンネル情報やトークンを別ファイルで管理できるように改修したのと、出力ログに時刻も追加しました。

## インストール
discord.pyのインストールをしてください。

```
$ python -m pip install -U discord.py
```
もしくは
```
$ python3 -m pip install -U discord.py
```
でpythonにdiscord.pyをpipでインストールしてください。

ちゃんとインストールできたかどうかはimport discordができるかどうかで確認してください。

## 実行
### 必要ファイル用意
main.pyと同じディレクトリに以下のファイル名のファイルを作ってください.

- voice_channel
  - 入退室の監視対象のボイスチャンネルのchannel_idを記入してください
- text_channel
  - 入退出ログを書き出すテキストチャンネルのchannel_idを記入してください
- token
  - botのトークンを記入してください

gitignoreでこれらのファイルはgithubにpushされないようにしています。

### 実行
以下のコマンドを実行
```
$ python main.py
```
