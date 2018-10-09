# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform

client = Bot(description="WackyBot by Wesfun#0748", command_prefix="!", pm_help = True)

# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.
@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')
	print('Support Discord Server: TBA')
	print('Github Link: TBA')
	print('--------')
	print('You are running WackyBot v1.0')
	print('Created by Wesfun#0748')
	return await client.change_presence(game=discord.Game(name='on Discord!')) #This is buggy, let me know if it doesn't work.

# This is a basic example of a call and response command. You tell it do "this" and it does it.
@client.command()
async def ping(*args):

	await client.say(":ping_pong: Pong!")
	await asyncio.sleep(3)
	await client.say("This bot was created by **Wesfun#0748**, Hope you enjoy all the great things it will be able to do! ")
# After you have modified the code, feel free to delete the line above so it does not keep popping up everytime you initiate the ping commmand.
	
client.run('PUT THE BOT TOKEN HERE')

# WackyBot created by Wesfun#0748
