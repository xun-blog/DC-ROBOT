import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import datetime
import json

with open('setting.json','r',encoding='utf8') as jFile:
    jdata=json.load(jFile)

class Main(Cog_Extension):

    @commands.command()
    async def ping(selF,ctx):
        await ctx.send(f'{round(selF.bot.latency*1000)} ms')

    @commands.command()
    async def PSH8(selF,ctx):
        embed=discord.Embed(title="PoorSuperHero8", url="https://youtu.be/dQw4w9WgXcQ", description="這裡可以換字", color=0x34bddf,timestamp=datetime.datetime.utcnow())
        embed.set_author(name="PSH8", url="https://youtu.be/dQw4w9WgXcQ", icon_url="https://i.imgur.com/LPCPlDm.jpg")
        embed.set_thumbnail(url="https://i.imgur.com/3MwIbGu.jpg")
        embed.add_field(name="蘇品禎", value="https://www.instagram.com/1127_pjhen/", inline=False)
        embed.add_field(name="黃芷嫺", value="https://www.instagram.com/r_xian_0111/", inline=False)
        embed.add_field(name="曾竑勳", value="https://www.instagram.com/true_red.xun/", inline=False)
        embed.add_field(name="邱炳榮", value="https://www.instagram.com/2003_11_21_nmsl/",inline=False)
        embed.set_footer(text="這邊可以換字")
        await ctx.send(embed=embed)

    @commands.command()
    async def say(self,ctx,msg):
        #await ctx.message.delete()
        channel = self.bot.get_channel(int(jdata['PSH8']))
        await channel.send(msg)
        
    
    @commands.command()
    async def clean(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)

def setup(bot):
    bot.add_cog(Main(bot))