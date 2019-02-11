import discord
import asyncio
import os

client = discord.Client()

@client.event
async def on_ready():
    print("login")

    print(client.user.name)

    print(client.user.id)

    print("------------------")

    await client.change_presence(game=discord.Game(name='!!!호노봇 <-명령어보기', type=1))


@client.event
async def on_message(message):
    if message.content.startswith('!!!호노봇'):
       await client.send_message(message.channel, "호노봇명령어 \n \n !호노봇말해 (할말) \n !호노봇안녕 \n !호노봇on \n !호노봇off \n "
                                                  "!호노봇몇살이야? \n !호노봇사랑해 \n !호노봇미쳤어? \n !호노봇그만해 \n !호노봇놀아줘 \n "
                                                  "!호노봇쿨한첫 \n !호노봇귀여운척 \n !호노봇치명적인척 \n !호노봇오늘나어때? \n !호노봇주인님이누구야?"
                                                  "\n !호노봇나랑사귈래? ")
    if message.content.startswith('!호노봇안녕'):
        await client.send_message(message.channel, "안녕하세요")

    if message.content.startswith('!호노봇off'):
        await client.send_message(message.channel, "으악! 꺼지기 싫어!")

    if message.content.startswith('!호노봇on'):
        await client.send_message(message.channel, "다시 태어났다!")

    if message.content.startswith('!호노봇몇살이야?'):
        await client.send_message(message.channel, "저는 2019년 2월 9일에 호노님이 만들어 주셨어요!")

    if message.content.startswith('!호노봇사랑해'):
        await client.send_message(message.channel, "나도 사랑해요!")

    if message.content.startswith('!호노봇그만해'):
        await client.send_message(message.channel, "싫어! 더할거야! 히히")

    if message.content.startswith('!호노봇미쳤어?'):
        await client.send_message(message.channel, "전 로봇이라 미칠 수 가 없습니다")

    if message.content.startswith('!호노봇놀아줘'):
        await client.send_message(message.channel, "싫어요 저는 잘생긴 주인님 호노님이랑 놀거에요")

    if message.content.startswith('!호노봇쿨한척'):
        await client.send_message(message.channel, "So cool~~")

    if message.content.startswith('!호노봇귀여운척'):
        await client.send_message(message.channel, "뀨우? ><")

    if message.content.startswith('!호노봇나랑사귈래?'):
        await client.send_message(message.channel, "죄송하지만...저는 주인님 꺼라서..")

    if message.content.startswith('!호노봇치명적인척'):
        await client.send_message(message.channel, "너의 마음에 뱅~ (찡긋)")

    if message.content.startswith('!호노봇오늘나어때?'):
        await client.send_message(message.channel, "헉! 너무 사랑스러워요>< ♥")

    if message.content.startswith('!호노봇주인님이누구야?'):
        await client.send_message(message.channel, "저의 주인님은 자상하시구 잘생기시구 또! 키도크시고 돈도많고! 목소리도 멋져요! 꺄악>< 주인님 사랑해요! 저를 가져욧♥")

    if message.content.startswith('!호노봇말해'):
        text = ""

        learn = message.content.split(" ")

        vrsize = len(learn)  # 배열크기

        vrsize = int(vrsize)

        for i in range(1, vrsize):  # 띄어쓰기 한 텍스트들 인식함

            text = text + " " + learn[i]

        channel = message.channel

        await client.send_message(channel, text)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
