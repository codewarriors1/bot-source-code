import discord
from discord.ext import commands
from colorama import Fore as C
from colorama import Style as S
import colorama
import random

gayrate = ["you are 1% gay", "you are 2% gay", "you are 3% gay","you are a-ok", "", "","", "", "",]

d = ["=", "==", "===", "====",]

class fun(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
   print("fun.py")

  @commands.command()
  async def say(self, ctx,*, sentence):
    await ctx.send(sentence)

  @commands.command(aliases=['8ball'])
  async def _8ball(self, ctx, *, question):
        responses = ['It is certain.',
                     'It is decidedly so.',
                     'Without a dobut.',
                     'Yes - definitely.',
                     'You may rely on it.',
                     'As I see it, yes.',
                     'Most likely.',
                     'Outlook good.',
                     'Yes.',
                     'Signs point to yes.',
                     'Reply hazy, try again.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Concentrate and ask again.',
                     "Don't count on it.",
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Very doubtful.']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


  @commands.command()
  async def gayrate(self, ctx,):
    await ctx.send( random.choice(gayrate)) 

  commands.command()
  async def lol(self,ctx):
    await ctx.send(random.choice(d))
   
def setup(client):
	client.add_cog(fun(client))
