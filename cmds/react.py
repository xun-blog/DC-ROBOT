import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json','r',encoding='utf8') as jFile:
    jdata=json.load(jFile)

class React(Cog_Extension):

    @commands.command()
    async def gura(selF,ctx):
        random_gura=random.choice(jdata['random_gura'])
        random_gura=discord.File(random_gura)
        await ctx.send(file=random_gura)

    @commands.command()
    async def 你主人的成績是(self,ctx):
        pic = discord.File(jdata['21_game'])
        await ctx.send(file = pic)
        await ctx.send(f'最輸的那個')

    @commands.command()
    async def soso(self,ctx):
        random_soso=random.choice(jdata['random_soso'])
        random_soso = discord.File(random_soso)
        await ctx.send(file = random_soso)

def setup(bot):
    bot.add_cog(React(bot))