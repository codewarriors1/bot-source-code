import discord
from discord.ext import commands
import json

class levelup(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print("levelup loaded")

  @commands.Cog.listener()
  async def on_message(self, message):
      if message.author.bot == False:
        try:
            with open('users.json', 'r') as f:
                users = json.load(f)

            await self.update_data(users, message.author)
            await self.add_experience(users, message.author, 5)
            await self.level_up(users, message.author, message)

            with open('users.json', 'w') as f:
                json.dump(users, f)
        except:
          print("Oh no. What if we don't exist.")
      await self.client.process_commands(message)


  async def update_data(users, user):
      if not f'{user.id}' in users:
          users[f'{user.id}'] = {}
          users[f'{user.id}']['experience'] = 0
          users[f'{user.id}']['level'] = 1


  async def add_experience(users, user, exp):
      users[f'{user.id}']['experience'] += exp


  async def level_up(users, user, message):
      experience = users[f'{user.id}']['experience']
      lvl_start = users[f'{user.id}']['level']
      lvl_end = int(experience ** (1 / 4))
      if lvl_start < lvl_end:
          await message.channel.send(f'{user.mention} has leveled up to level {lvl_end}')
          users[f'{user.id}']['level'] = lvl_end

  @commands.command()
  async def level(self, ctx, member: discord.Member):
      try:
        id = ctx.message.author.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['level']
        await ctx.send(f'{member} is at level {lvl}!')
      except:
        id = ctx.message.author.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['level']
        await ctx.send(f'You are at level {lvl}!')
      
  @commands.Cog.listener()
  async def on_member_join(self,member):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await self.update_data(users, member)

    with open('users.json', 'w') as f:
        json.dump(users, f)

def setup(client):
	client.add_cog(levelup(client))