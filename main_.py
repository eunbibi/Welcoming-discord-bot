import discord
from discord.ext import commands

token = 'put ur token here'

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Over This Server'))

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

#responding new joiner
@client.event
async def on_member_join(member): 

    #team server                  
    #guild = client.get_guild(814620705425195049)   #serverID
    #channel = guild.get_channel(814620705794687017)   #channelID
    
    #testing server
    guild = client.get_guild(829979114362241025)
    channel = guild.get_channel(830186715737489428)

    print('join info: ',member.name)

    #welcome the member on server
    await channel.send(f':computer: Welcome, its COMP216/SEC401 Group 2 {member.mention} ! :nerd:')
    #welcome the member on direct msg
    await member.send(f':computer: Welcome to {guild.name}, {member.name}! :nerd:')
    
@client.event
async def on_message(message):
    if message.content == '$hi':
        await message.channel.send('Hello! We are group 2')

    elif message.content.startswith('$members'):
        await message.channel.send('a\nb\nc\nd\ne')

    elif message.content.startswith('$description'):
        await message.channel.send('The goal of our project is making a Discord Bot that will perform automated processes. Automated programs that look and act like users and automatically respond to events and commands on Discord are called bots. Discord bot users (or just bots) have nearly unlimited applications due to its “middle man”, like nature. This allows for flexable ideas/features which can be as simple as a string response when messaging the bot with a user, or using the bot to connect and display data on a database site.')

    elif message.content.startswith("$help"):
        emd = discord.Embed(
            title="Here is what I can do!",
            colour=0xad42f5
        )
        emd.add_field(name="I'm a welcoming bot, I welcome users :partying_face:", value="--------------------------------------------", inline=False)
        emd.add_field(name="$hi", value="Greeting", inline=False)
        emd.add_field(name="$members", value="Team members", inline=False)
        emd.add_field(name="$description", value="Project Description", inline=False)
        await message.channel.send(embed=emd)

client.run(token)