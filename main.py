import discord
import json,requests
import re,os,hashlib


client = discord.Client()
@client.event
async def on_message(message):
    censoredLang = ["snitch","xxx","fuck"]
    for x in censoredLang:
        if re.search(x,message.content,re.IGNORECASE):
            censored = re.search(x,message.content,re.IGNORECASE)


    
    if message.content.find("!hello") != -1:
        await message.channel.send("Hi from bot :D")
    elif message.content.find("!show") != -1:
        # data will be shown here
        req = requests.get("https://www.googleapis.com/youtube/v3/channels?id=UCyQSAi4Xh5ZQKpMPLEUPSrA&key=AIzaSyBYzmjpQYOb15ueTx3-Y2QcgI8_21Xlhr0&part=snippet,statistics&fields=items(id,snippet,statistics)")
        reqData = json.loads(req.text)
        await message.channel.send(reqData["error"]["errors"][0]["domain"])
    elif message.content == "!whoIsYourMaster":
        await message.channel.send("My Master is : Md.Masud karim\nHe creted me at Saturday 4 April 2020\nTime: 6:16 PM\nHis facebook link is : forbidden.masud")

    elif censored:
        await message.delete()
        await message.channel.send("Gali dewa moha pap.. hawar pola bujhos na ?")

@client.event
async def on_member_join(member):
    await channel.send("Welcome new member".str(member))

client.run(PLACE_YOUR_TOKEN)
