import re
import asyncio
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse
import random
import discord
import random
import os
import datetime
import urllib
import bs4
import datetime
import openpyxl
import requests
from requests import post
import youtube_dl
import dbkrpy
from requests import get
from urllib.request import urlopen, Request
import json
import sys
from json import loads
client = discord.Client()


@client.event
async def on_ready():
    user = len(client.users)
    server = len(client.guilds)
    await client.change_presence(status=discord.Status.offline)
    game = discord.Game("미독 현 다이아2")
    await client.change_presence(status=discord.Status.online, activity=game)
    


       

@client.event
async def on_message(message):
    print(message.content)
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕하세요")
    if message.content.startswith("!다딱"):
        await message.channel.send("다딱다딱")
    if message.content.startswith("!미독"):
        await message.channel.send("다따기")
    if message.content.startswith("!왕이 양옆에있으면?"):
        await message.channel.send("우왕좌왕")
    if message.content.startswith("!미독바보"):
        await message.channel.send("ㅇㅈ")
    if message.content == "!카파봇출력":
        await message.channel.send("Python Bot에 의해 출력됨.")
    if message.content.startswith("!카파봇1부터10"):
        for x in range(10):
            await message.channel.send(x+1)
    if message.content.startswith("!채팅청소"):
        if message.author.guild_permissions.manage_messages:
            try:
                amount = message.content[6:]
                await message.channel.purge(limit=int(amount))
                await message.channel.send(f"**{amount}**개의 메시지를 지웠습니다.")
            except ValueError:
                await message.channel.send("청소하실 메시지의 **수**를 입력해 주세요.")
        else:
            await message.channel.send("권한이 없습니다.")
    if message.content.startswith("!실검"):
        url = "https://m.search.naver.com/search.naver?query=%EC%8B%A4%EA%B2%80"
        html = urlopen(url)
        parse = BeautifulSoup(html, "html.parser")
        result = ""
        tags = parse.find_all("span", {"class" : "tit _keyword"})
        for i, e in enumerate(tags):
            result = result + (str(i+1))+"위 | "+e.text+"\n"
        await message.channel.send(result)
    if message.content.startswith('!게임룰렛'):
        randomlist = ["듀링","옵치","스타","롤","룬테라","마크","어몽어스","동물의숲","테트리스","gta5"]
        ran = random.randint(0, len(randomlist)-1)
        await message.channel.send(randomlist[ran])
    if message.content.startswith('!투표'):
            vote = message.content[4:].split("/")
            await message.channel.send("⭐투표 - **" + vote[0] + "**")
            for i in range(1, len(vote)):
                choose = await message.channel.send("**" + vote[i] + "**")
                await choose.add_reaction('👍')
    if message.content.startswith("-"):
        if message.author.id == 456633518882160642:
            prepix = message.content[1:]
            channel = client.get_channel(872859090454458458)
            await channel.send(prepix)
        else:
            pass
    if message.content.startswith("!킥"):
        DevID = [630034414302396416,299895531701010442,543361804924092427,717044065635532810]
        if message.author.id in DevID:
            kickusermention = message.content[4:]
            kickuserid = kickusermention[2:20]
            kickuser = message.guild.get_member(int(kickuserid))
            await message.guild.kick(kickuser)
            await message.channel.send("관리자 권한으로 " + str(kickuser) + "님을 추방했어요!")
         
            
    if message.content.startswith('!eval'):
        DevID = [630034414302396416,299895531701010442,543361804924092427,717044065635532810]
        if message.author.id in DevID:
            try:
                f = open("eval.txt", 'w')
                f.write(f"{str(message.author)} 님께서 eval을 사용하였습니다.")
                f.close()
                print(f"{str(message.author)} 님께서 eval을 사용하였습니다.")
                cmd = message.content[6:]
                output = eval(cmd)
                embed = discord.Embed(title="EVAL 실행 결과", description=f"**Input**\n```{cmd} ```\n**Output**\n```{output}```", color=0x00ff00)
                await message.channel.send(embed=embed)
            except Exception as e:
                embed = discord.Embed(title="EVAL 실행 결과", description=f"**Input**\n```{cmd} ```\n**Output**\n```{e}```", color=0xff0000)
                await message.channel.send(embed=embed)
        else:
            pass
    if message.content.startswith("!시간"):
        now = datetime.datetime.now()
        await message.channel.send(str(now.year)+"년"+str(now.month)+"월"+str(now.day)+"일"+str(now.hour)+"시"+str(now.minute)+"분"+str(now.second)+"초 입니다")
    if message.content.startswith('hellothisisverification'):
        await message.channel.send("kafa#4560")
    if message.content.startswith("!기능"):
        embed = discord.Embed(title="카파봇 안내", description="카파봇은 롤 전적 검색과 룰렛 투표 기능이 있는 봇입니다 자주 업데이트 되고 원하시는 기능 카파#4560 이나 지원 서버 오셔서 말해주세요^^", color=0x00ff00)
        embed.add_field(name="명령어 안내", value="롤전적 (닉네임) !실검 !채팅청소 (숫자) !게임룰렛 !시간 !카파봇배워 물음/답 카파봇 OOO 자동 등급 지급(kafa#4560으로 dm을 주셔야 가능합니다)", inline=True)
        embed.add_field(name="기능 요청 안내", value="[카파봇 지원 서버](https://discord.gg/xU8WSHE) 또는 !건의 (내용) ", inline=True)
        embed.set_footer(text="제작자 kafa#4560   카파봇은 AI Online 소속 봇입니다")
        await message.channel.send(embed=embed)
    
    
    if message.content == "!가위" or message.content == "!바위" or message.content == "!보":

        bot_response = random.randint(1, 3)
        if bot_response == 1:
            if message.content == "!가위":
                await message.channel.send("가위 VS 가위 비겼습니다!")
            elif message.content == "!바위":
                await message.channel.send("바위 VS 가위 제가 졌습니다!")
            else:
                await message.channel.send("보 VS 가위 제가 이겼습니다!")
        elif bot_response == 2:
            if message.content == "!가위":
                await message.channel.send("제가 이겼습니다")
            elif message.content == "!바위":
                await message.channel.send("비겼습니다")
            else:
                await message.channel.send("제가 졌습니다")
        else:
            if message.content == "!가위":
                await message.channel.send("제가 졌습니다")
            elif message.content == "!바위":
                await message.channel.send("제가 이겼습니다")
            else:
                await message.channel.send("비겼습니다")
    if message.content.startswith("!공지"):
        DevID = [630034414302396416,717044065635532810]
        if message.author.id in DevID:
            for g in client.guilds:
                for c in g.text_channels:
                    if '공지' in c.name:
                        try:
                            embed = discord.Embed(title="카파봇 공지사항", description=""[4:], color=0x00ff00)
                            embed.add_field(name="공지 내용", value="**" + message.content[4:] + "**\n\n[카파봇 지원 서버](https://discord.gg/fUkZWhk)",inline=True)
                            embed.set_footer(text="작성자: " + message.author.name + " | 카파봇#1318",icon_url=message.author.avatar_url)
                            await c.send(embed=embed)
                        except discord.errors.Forbidden:
                            pass
                                              
    if message.content.startswith('!exec'):
        DevID = [630034414302396416,299895531701010442,543361804924092427,717044065635532810]
        if message.author.id in DevID:
            try:
                cmd = message.content[6:]
                output = exec(cmd)
                embed = discord.Embed(title="EXEC 실행 결과", description=f"**Input**\n```{cmd} ```\n**Output**\n```{output}```", color=0x00ff00)
                await message.channel.send(embed=embed)
            except Exception as e:
                embed = discord.Embed(title="EXEC 실행 결과", description=f"**Input**\n```{cmd} ```\n**Output**\n```{e}```", color=0xff0000)
                await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(title="EXEC 실행 실패", description=f"**{message.author.name}**님은 이 명령어를 사용 할 권한이 없습니다.", color=0xff0000)
            await message.channel.send(embed=embed)     
    if message.content.startswith("!dm"):
        for i in message.guild.members:
            if i.bot == False:
                a = message.content[4:]
                await i.send(a)
            else:
                pass
    if message.content.startswith("!건의"):
        prepix = message.content[4:]
        channel = client.get_channel(735480228213686284)
        await channel.send(prepix)
    else:
        pass
    if message.content.startswith("!개인dm"):
        message = message.content[6:]
        getusermention = client.get_user(379186329747193857,)
    if message.content.startswith("storm"):
        await message.channel.send("?")
    if message.content.startswith("!뮤트"):
        DevID = [630034414302396416]
        if message.author.id in DevID:
            firstid = message.content[4:]
            author = message.guild.get_member(int(firstid[2:20]))
            role = discord.utils.get(message.guild.roles, name="뮤트")
            await author.add_roles(role)
            await message.channel.send("I've given you a mute.")
        else:
            await message.channel.send('It is developer only')
    if message.content.startswith("!언뮤트"):
        DevID = [630034414302396416]
        if message.author.id in DevID:
            firstid = message.content[5:]
            author = message.guild.get_member(int(firstid[2:20]))
            role = discord.utils.get(message.guild.roles, name="뮤트")
            await author.remove_roles(role)
            await message.channel.send("I remove mute")
        else:
            await message.channel.send("you don't have a owner")
    if message.content.startswith("!갈리오"):
        await message.channel.send("김주환 바보")
    if message.content.startswith("0"):
        prepix = message.content[2:]
        channel = client.get_channel(705251317123383326)
        await channel.send(prepix)
    if message.content == "!핑" or message.content == "!ping":
        la = client.latency
        embed = discord.Embed(title="핑", description="현재 카파봇의 핑: " + str(round(la * 1000)) + "ms")
        await message.channel.send(embed=embed)
    if message.content.startswith("로또추첨"):
        os.system("cls")
        x = random.sample(range(1, 47), 6)
        await message.channel.send("과연 당첨자는 누구인가?")
        await asyncio.sleep(6)
        await message.channel.send(x)
        await message.channel.send("모두 감사합니다 다음에 또 참여해주시기 바랍니다")
    if message.content.startswith("!로또응모"):
        await message.channel.send("로또번호 여섯자리를 /와 함께 입력해주세요 ex:/1,2,3,4,5,6 (이번상품: 니트로 2개월)")
    if message.content.startswith("/"):
        try:
            role = discord.utils.get(member.guild.roles, name='버스터')
            await member.add_roles(role)
        except:
            pass
    
       


            


@client.event

async def on_ready():
    twitch_Client_ID = 'ip9wt02c8w9rxlvqzpg7wpwc557umh'

    twitch_Client_secret = 'xvc3dt8o07eo1g1h5sqe1fv4y680ti'




    discord_channelID = 813436385909669918


    twitchID = 'midok98'

    ment = '귀여운 미도기 방송중'



    print(client.user.id)

    print("ready")






    # 채팅 채널 설정

    channel = client.get_channel(discord_channelID)



    # 트위치 api 2차인증

    oauth_key = requests.post("https://id.twitch.tv/oauth2/token?client_id=" + twitch_Client_ID + "&client_secret=" + twitch_Client_secret + "&grant_type=client_credentials")

    access_token = loads(oauth_key.text)["access_token"]

    token_type = 'Bearer '

    authorization = token_type + access_token

    print(authorization)



    check = False     #여기 오류를 수정합니다



    while True:

        print("ready on Notification")



        # 트위치 api에게 방송 정보 요청

        headers = {'client-id': twitch_Client_ID, 'Authorization': authorization}

        response_channel = requests.get('https://api.twitch.tv/helix/streams?user_login=' + twitchID, headers=headers)

        print(response_channel.text)

        # 라이브 상태 체크

        try:

            # 방송 정보에서 'data'에서 'type' 값이 live 이고 체크상태가 false 이면 방송 알림(오프라인이면 방송정보가 공백으로 옴)

            if loads(response_channel.text)['data'][0]['type'] == 'live' and check == False:

                await channel.send(ment +'\n https://www.twitch.tv/' + twitchID)

                print("Online")

                check = True

        except:

            print("Offline")

            check = False



        await asyncio.sleep(30)            






@client.event
async def on_member_join(member):
    try:
        syscha = member.guild.system_channel
        await syscha.send(f"{member.mention} 님, 환영합니다!")
        role = discord.utils.get(member.guild.roles, name='시청자')
        await member.add_roles(role)
    except:
        pass








client.run('NzU3OTgxMjY3MDUxNDEzNTE1.X2oTEA.9zBrGfHdp3arjM2Ta_wtobFm__k')