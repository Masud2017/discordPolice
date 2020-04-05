import discord
import re


client = discord.Client()
@client.event
async def on_message(message):
    censoredLang = ["snitch","xxx","fuck","chudi"]
    for x in censoredLang:
        if re.search(x,message.content,re.IGNORECASE):
            censored = re.search(x,message.content,re.IGNORECASE)


    if message.content.find("!hello") != -1:
        await message.channel.send("Hi from bot :D")
    elif message.content == "!whatIsYourName":
        await message.channel.send("My name is : Discord-Police\nI am here for save you guys from censored verse :D")

    elif message.content == "!whoIsYourMaster":
        await message.channel.send("My Master is : Md.Masud karim\nHe creted me at Saturday 4 April 2020\nTime: 6:16 PM\nHis facebook link is : forbidden.masud")

    elif censored: #doing the actuall filtering from here.
        await message.delete()
        await message.channel.send("Gali dewa moha pap.. hawar pola bujhos na ?")

@client.event
async def on_member_join(member):
    await channel.send("Welcome new member".str(member))

client.run("YOUR_TOKEN_WILL_BE_PLACED_HERE")
