import discord
import pandas
from discord.ext import commands

with open('cogs/familyfeud.csv', 'r') as csv_file:
    csv = pandas.read_csv('cogs/familyfeud.csv', index_col="Question" )
    line_count = 0
    print(f'Processed {line_count} lines.')

class trivia(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.Cog.listener()
  async def on_message(self, message):
	  await self.client.process_commands(message)

  @commands.Cog.listener()
  async def on_ready(self):
    print("Trivia.py loaded")

  @commands.command()
  async def askme(self, ctx):
	  await ctx.send("Mission successful")
	  print(csv)

def setup(client):
  client.add_cog(trivia(client))
