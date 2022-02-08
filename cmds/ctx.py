import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json','r',encoding='utf8') as jFile:
    jdata=json.load(jFile)

class Ctx(Cog_Extension):
    @commands.command()
    async def 雲端(self,ctx):
        await ctx.send(f'https://drive.google.com/drive/folders/1BD_ZwdvhWRTBJha2vlXbfHjbM0OgwOD3')

    @commands.command()
    async def 編年史(self,ctx):
        await ctx.send(jdata['history'])
 
    @commands.command()
    async def 這隻機器人是(self,ctx):
        await ctx.send(f'我是PSH8的血汗勞工')

    @commands.command()
    async def 猜拳(self,ctx):
        random_game=(random.choice(jdata['random_game']))
        await ctx.send(random_game)

    @commands.command()
    async def 數數(self,ctx):
        random_count=(random.choice(jdata['random_count']))
        await ctx.send(random_count)
    
    @commands.command()
    async def 早餐(self,ctx):
        random_food_type=(random.choice(jdata['food_type']))
        await ctx.send(random_food_type)
    
    @commands.command()
    async def 午餐(self,ctx):
        random_food_type=(random.choice(jdata['food_type']))
        await ctx.send(random_food_type)

    @commands.command()
    async def 晚餐(self,ctx):
        random_food_type=(random.choice(jdata['food_type']))
        await ctx.send(random_food_type)
    
    @commands.command()
    async def 下午茶(self,ctx):
        random_food_a=(random.choice(jdata['food_a']))
        await ctx.send(random_food_a)

    @commands.command()
    async def 宵夜(self,ctx):
        random_food_m=(random.choice(jdata['food_m']))
        await ctx.send(random_food_m)

    
def setup(bot):
    bot.add_cog(Ctx(bot))