import discord
from discord.ext import commands
import random
import json
from datetime import datetime
import pytz

client = commands.Bot(command_prefix="!")
local_tz = timezone('Asia/Dubai')
nowtime = datetime.now(local_tz)

class Slapper(commands.Converter):
	async def convert(self, ctx, argument):
		to_slap = random.choice(ctx.guild.members)
		return '{0.author} slapped {1} because *{2}*'.format(ctx, to_slap, argument)

@client.event
async def on_ready():
	print("Bot is ready")

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
    await ctx.send("Hi there, " + str(ctx.author) + " of the " + str(ctx.guild) + ".")

@client.command()
async def greet(ctx, timezonename):
  cur_tz = pytz.timezone(timezonename)
  current_time = cur_tz.localize(nowtime)
  if current_time >= '06:00' and current_time < '12:00':
    await ctx.send("Good morning, " + ctx.message.author.mention + ". The time is " + current_time)
  elif current_time >= '12:00' and current_time < '17:00':
    await ctx.send("Good afternoon, " + ctx.message.author.mention + ". The time is " + current_time)
  elif current_time >= '17:00' and current_time < '19:00':
    await ctx.send("Good evening, " + ctx.message.author.mention + ". The time is " + current_time)
  else:
    await ctx.send("Good night, " + ctx.message.author.mention + ". The time is " + current_time + ". You should probably go to sleep.")


@client.command()
async def help(ctx):
    embed = discord.Embed(
        title = "Introduction to AutoMod",
        description = """AutoMod is a bot made by @wakandawarrior and @Lxcky to spice up and try to aid all of those involved in this server. If you have any ideas as to how I may be improved, please talk to us (preferably not DMs)
**__Level-up system__**
Each user will gain experience for each message sent in this server to directly to the bot. 
There may be special features to be unlocked if the server gains enough participation, so please try to contribute
to the further development of the bot

**__fun commands__**
slap @user - slaps the mentioned user.

**__moderation commands__**
clear amount - clears as many messages as you want.
ban @user reason - bans the mentioned user and dms them the reason
kick @user reason - kicks the mentioned user and dms them the reason
mute @user mutes the user until you unmute them
unmute @user unmutes the user so they will be able to talk again
server - gives information about the server

to use the commands you must have certain permissions example manage messgae permissions to clear messages with the bot,ban members permissions to ban members using the bot,kick members permissions to kick members with the bot.
**__Plain old nice commands__**
greet  - We will just greet you with a good morning, afternoon and evening (depending on the time of course)
if you need help say !support
""",
        colour = discord.Colour(int("0dfaab", 16))
    )

    icon = str(ctx.guild.icon_url)
    embed.set_footer(text="Created using the power of teamwork")
    embed.set_image(url=icon))
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/750429563028242512/2642f6de2a014e54f1ef29ccdfa9a1a3.png')
    embed.set_author(name='@wakandawarrior & @Lxcky', icon_url='https://cdn.discordapp.com/avatars/684973286438076437/11d7951e4e89d4b97b7f93b641770917.png')
    embed.add_field(name='!server',value='', inline=False)
    embed.add_field(name='!support', value='!support can be used to gain access to our tesing server' , inline=False) 
    await ctx.send(embed=embed)
    
@client.command()
async def add_roles(ctx, rolename):
    member = ctx.message.author
    role = discord.utils.get(member.guild.roles, name=rolename)
    await discord.Member.add_roles(member, role)

@client.event
async def on_member_join(member):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_data(users, member)

    with open('users.json', 'w') as f:
        json.dump(users, f)


@client.event
async def on_message(message):
    if message.author.bot == False:
        with open('users.json', 'r') as f:
            users = json.load(f)

        await update_data(users, message.author)
        await add_experience(users, message.author, 5)
        await level_up(users, message.author, message)

        with open('users.json', 'w') as f:
            json.dump(users, f)

    await client.process_commands(message)


async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 1


async def add_experience(users, user, exp):
    users[f'{user.id}']['experience'] += exp


async def level_up(users, user, message):
    with open('levels.json', 'r') as g:
        levels = json.load(g)
    experience = users[f'{user.id}']['experience']
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(experience ** (1 / 4))
    if lvl_start < lvl_end:
        await message.channel.send(f'{user.mention} has leveled up to level {lvl_end}')
        users[f'{user.id}']['level'] = lvl_end

@client.command()
async def level(ctx, member: discord.Member = None):
    if not member:
        id = ctx.message.author.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['level']
        await ctx.send(f'You are at level {lvl}!')
    else:
        id = member.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['level']
        await ctx.send(f'{member} is at level {lvl}!')
	
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="none"):
  await member.send("you have been kicked:" + reason)
  await member.kick(reason=reason)



@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="none"):
  await member.send("you have been banned:" + reason)
  await member.ban(reason=reason)

  channel = bot.get_channel(765676846410760222)
  await channel.send ("member has been bnned")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(
        ctx,
        amount=2,
):
  await ctx.message.delete()
  await ctx.channel.purge(limit=int(amount))
  author = ctx.author
  channel = bot.get_channel(765676846410760222)
  await channel.send ("{author.mention} has cleared amount of messages")

@bot.command()
async def support(ctx):
  await ctx.send("here is our support server! https://discord.gg/tsYHXq3")
		    
@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx,member : discord.Member):
  muted = ctx.guild.get_role(765460547129835540)

  await member.add_roles(muted)
  await ctx.send(member.mention + " has been muted")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx,member : discord.Member):
  muted = ctx.guild.get_role(765460547129835540)

  await member.remove_roles(muted)
  await ctx.send(member.mention + " has been unmuted")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def assignrole(ctx, member : discord.Member, rolename):
    role = discord.utils.get(member.guild.roles, name=rolename)
    await discord.Member.add_roles(member, role)

@bot.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)	

client.run(token)
