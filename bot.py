
import os
import discord
from dotenv import load_dotenv
from discord.utils import get
import random
import emoji
from discord.ext import commands


intents = discord.Intents.all()
client = discord.Client(intents=intents)
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#GUILD = os.getenv('DISCORD_GUILD')
guild = ""


@client.event
async def on_ready():
    Channel = client.get_channel(816293259286020126)
    Text= "**Welcome to Lab de Jogos Discord Server**\n\n"\
        "Much like the physical \"Laboratório de Jogos\" room this is a place to support the Game's courses at IST.\n"\
        "Here you can work with your colleagues, ask questions to teachers, share your latest projects and what you've been playing. \n\n" \
        "Before you're allowed to talk in other channels, react to the courses are you attending this semester: \n\n" \
          "*First Semester* \n"\
          ":one: Artificial Intelligence for Games \n" \
          ":two: Computer Graphics for Games \n" \
          ":three: Game Design \n" \
          ":four: Three-Dimensional Vizualization and Animation \n\n" \
         "*Second Semester* \n" \
         ":five: Game Development Methodology \n\n" \
        "If you think your role is not described above please send a message to one of our @admin or write it here\n"\
        "Thank you \n"


    Moji = await client.send_message(Channel, Text)


 #   await client.add_reaction(Moji, emoji='🏃')


@client.event
async def on_reaction_add(reaction, user):
    print("addedReaction " + str(reaction))
    Channel = client.get_channel(816293259286020126)
    if reaction.message.channel.id != Channel.id:
        return
    roles = client.guilds[0]._roles
    for y in roles.values():
        if y.name == "@student":
            break
    emojiString = emoji.demojize(reaction.emoji)
    print(emoji)
    if '1' in emojiString:
      roles = client.guilds[0]._roles
      for x in roles.values():
          if x.name == "@iaj":
              break

      await user.add_roles(x)
      await user.add_roles(y)

    elif '2' in emojiString:
        print("CGJ")
        roles = client.guilds[0]._roles
        for x in roles.values():
            if x.name == "@cgj":
                break

        await user.add_roles(x)
        await user.add_roles(y)

    elif '3' in emojiString:
        print("DJ")
        roles = client.guilds[0]._roles
        for x in roles.values():
            if x.name == "@dj":
                break

        await user.add_roles(x)
        await user.add_roles(y)

    elif '5' in emojiString:
        roles = client.guilds[0]._roles
        for x in roles.values():
            if x.name == "@mdj":
                break

        await user.add_roles(x)
        await user.add_roles(y)

    elif '4' in emojiString:
        roles = client.guilds[0]._roles
        for x in roles.values():
            if x.name == "@avt":
                break

        await user.add_roles(x)
        await user.add_roles(y)




@client.event
async def on_raw_reaction_remove(payload):
    print("raw reaction remove")
    message_id = payload.message_id
    channelID = payload.channel_id
    # Que merda
    if channelID == 816293259286020126:  # This can be changed but i was using an individual message
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)  # This gets the guild
        #members = guild.fetchMembers()
        emojiString = emoji.demojize(payload.emoji.name)
        if '1' in emojiString:  # This is the name of the emoji that is used
            role = discord.utils.get(guild.roles, name='@iaj')  # Enter the role name here
        elif '2' in emojiString:  # This is the name of the emoji that is used
            role = discord.utils.get(guild.roles, name='@cgj')  # Enter the role name here
        elif '3' in emojiString:  # This is the name of the emoji that is used
            role = discord.utils.get(guild.roles, name='@dj')  # Enter the role name here
        elif '4' in emojiString:  # This is the name of the emoji that is used
            role = discord.utils.get(guild.roles, name='@avt')  # Enter the role name here
        elif '5' in emojiString:  # This is the name of the emoji that is used
            role = discord.utils.get(guild.roles, name='@mdj')  # Enter the role name here

        if role is not None:  # If role exists
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)  # Gets the member
            if member is not None:  # Checks if member is real
                await member.remove_roles(role)  # Gives the role
            else:
                print("Member not found")
        else:
            print("Role not found")


@client.event
async def on_reaction_remove(reaction, user):
    print("On reaction removed " + str(reaction))
    Channel = client.get_channel(816293259286020126)
    if reaction.message.channel.id != Channel.id:
        return
    roles = client.guilds[0]._roles
    for y in roles.values():
        if y.name == "@student":
            break
    emojiString = emoji.demojize(reaction.emoji)
    print(emoji)
    if '1' in emojiString:
      roles = client.guilds[0]._roles
      for x in roles.values():
          if x.name == "@iaj":
              break

      await user.remove_roles(x)
      await user.remove_roles(y)

    elif '2' in emojiString:
        print("CGJ")
        roles = client.guilds[0]._roles
        for x in roles.values():
            if x.name == "@cgj":
                break

        await user.remove_roles(x)
        await user.remove_roles(y)

    elif '3' in emojiString:
        print("DJ")
        roles = client.guilds[0]._roles
        for x in roles.values():
            if x.name == "@dj":
                break

        await user.remove_roles(x)
        await user.remove_roles(y)

    elif '5' in emojiString:
        roles = client.guilds[0]._roles
        for x in roles.values():
            if x.name == "@mdj":
                break

        await user.remove_roles(x)
        await user.remove_roles(y)

    elif '4' in emojiString:
        roles = client.guilds[0]._roles
        for x in roles.values():
            if x.name == "@avt":
                break

        await user.remove_roles(x)
        await user.remove_roles(y)

@client.event
async def add_reaction(Moji, emoji):
    print(emoji)

@client.event
async def send_message(channel, message):
    await channel.send(message)



#Old TOKEN
client.run("ODE2MjczMjY2NDY0NjUzMzMy.YD4juA.I3IqStdjPacAgylei6yVgjI6mUM")