import discord
from discord.ext import commands
import json
import random
import os
client = discord.Client()

with open('setting.json','r',encoding='utf8') as jFile:
    jdata=json.load(jFile)

intents=discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(F'cmds.{Filename[:-3]}')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(F'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(F'cmds.{extension}')
    await ctx.send(f'unloaded {extension} done')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(F'cmds.{extension}')
    await ctx.send(f'Reloaded {extension} done')

if __name__=="__main__":
    bot.run(jdata['TOKEN'])