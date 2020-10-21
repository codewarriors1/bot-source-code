import discord
from discord.ext import commands
import random
from datetime import datetime
import pytz
import os
 
client = commands.Bot(command_prefix="!",)
local_tz = pytz.timezone('Asia/Dubai')
nowtime = datetime.now()
client.remove_command("help")

class Slapper(commands.Converter):
	async def convert(self, ctx, argument):
		to_slap = random.choice(ctx.guild.members)
		return '{0.author} slapped {1} because *{2}*'.format(ctx, to_slap, argument)

@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing, name="AutoMod  | !about | !support"))

@client.command()
async def slap(ctx, *, reason: Slapper):
	await ctx.send(reason)

@client.command()
async def slaphard(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = " and ".join(x.name for x in members)
    await ctx.send('{} just got slapped for {}'.format(slapped, reason))
  
@client.command()
async def joined(ctx, *, member: discord.Member):
    await ctx.send('{0} joined on {0.joined_at}'.format(member))

@client.command()
async def hello(ctx):
    await ctx.send("Hi there, " + str(ctx.author.mention) + " of the " + str(ctx.guild) + " guild.")

@client.command()
async def greet(ctx,timezonename):
  cur_tz = pytz.timezone(timezonename)
  nowtime = datetime.now(cur_tz)
  current_time = nowtime.strftime('%H:%M:%S')
  if current_time >= '06:00' and current_time < '12:00':
    await ctx.send("Good morning, " + ctx.message.author.mention + ". The time is " + current_time)
  elif current_time >= '12:00' and current_time < '17:00':
    await ctx.send("Good afternoon, " + ctx.message.author.mention + ". The time is " + current_time)
  elif current_time >= '17:00' and current_time < '19:00':
    await ctx.send("Good evening, " + ctx.message.author.mention + ". The time is " + current_time)
  else:
    await ctx.send("Good night, " + ctx.message.author.mention + ". The time is " + current_time + ". You should probably go to sleep.")


@client.command()
async def load(ctx, extention):
	client.load_extension(f'cogs.{extention}')

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')




@client.command()
async def help(ctx):
  embed = discord.Embed(
    title="Commands",
    description="""
    **__Level-up system__**
Each user will gain experience for each message sent in this server to directly to the bot. 
There may be special features to be unlocked if the server gains enough participation, so please try to contribute
to the further development of the bot

**__fun commands__**
slap **reason** - slaps a random user and gives a reason for its actions

slaphard **User** **reason** - slaps the mentioned user(s) and gives a reason for your actions


**__Plain old nice commands__**
greet (timezone)  - We will just greet you with a good morning, afternoon and evening (depending on the time of course)
if you need help say !support
""",
colour = discord.Colour(int("f0d869", 16))
  )

  embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/750429563028242512/2642f6de2a014e54f1ef29ccdfa9a1a3.png')
  embed.add_field(name='!server',value='!server can be used to display more information about the server', inline=False)
  embed.add_field(name='!support', value='!support can be used to gain access to our tesing server' , inline=False)

  await ctx.send(embed=embed)

client.run("<REDACTED>")
