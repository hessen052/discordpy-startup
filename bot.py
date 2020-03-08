import discord

client = discord.Client()

ID_ROLE_MEMBER = 663185140675117057

import sys
print(sys.version)

@client.event
async def on_member_join(member):
    print(member)
    # 用意したIDから Role オブジェクトを取得
    role = member.guild.get_role(ID_ROLE_MEMBER)

    # 入ってきた Member に役職を付与
    await member.add_roles(role)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)


client.run("Njg1OTgxODA2MTgwMzAyODgy.XmQksg.-_DSAiBT0u2gpEeWxIP6DnC1yP4")