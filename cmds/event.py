import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json','r',encoding='utf8') as jFile:
    jdata=json.load(jFile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(int(jdata['Welcome_and_leave_channel']))
        await channel.send(f'啊{member}怎麼跑進來了')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(int(jdata['Welcome_and_leave_channel']))
        await channel.send(f'{member} 跑走了')

    @commands.Cog.listener()
    async def on_message(self, msg):
        laugh=['笑死','快笑死','好好笑','超好笑']
        if msg.content=="邱炳榮上台大的機率":
            await msg.channel.send('100%')
        elif msg.content=="蘇品禎補考考過的機率":
            await msg.channel.send('100%')
        elif msg.content.endswith('機率'):
            probability=(random.choice(jdata['probability']))
            await msg.channel.send(probability)
        if msg.content.endswith('是喔'):
            await msg.channel.send("敷衍")
        if msg.content.endswith('說謊'):
            await msg.channel.send("0")
        if msg.content.endswith('是哦'):
            await msg.channel.send("敷衍")
        if msg.content in laugh:
            await msg.channel.send("笑三小")
        if msg.content.endswith('臭欸'):
            await msg.channel.send("0")
        if msg.content.endswith('臭我'):
            await msg.channel.send("0")
        if msg.content.endswith('臭'):
            await msg.channel.send("0")
        if msg.content.endswith('呢'):
            await msg.channel.send("這次又要嘲諷誰")

def setup(bot):
    bot.add_cog(Event(bot))