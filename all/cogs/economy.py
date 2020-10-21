import discord
from discord.ext import commands
import os
import json

class economy(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.Cog.listener()
  async def on_ready(self):
    print("economy.py loaded")

  @commands.command()
  async def balance(self, ctx):
    await open_account(ctx.author)

    users = await get_bank_data()
    user = ctx.author
    wallet_amt = users[str(user.id)]["wallet"] 
    
    bank_amt = users[str(user.id)]["bank"]
    em = discord.Embed(title = f"{ctx.author.name}'s balance", color = discord.Color.red())
    em.add_field(name = "wallet", value = wallet_amt)
    em.add_feild(name = "bank", value = bank_amt)
    await ctx.send(embed = em)





async def open_account(user):
	with open("mainbank.json", "r") as f:
		users = json.load(f)
	

	
	
	if str(user.id) in users:
		return False
	else:
	  users[str(user.id)]["wallet"] = 100
	users[str(user.id)]["bank"] = 0
	
	with open("mainbank.json", "w") as f:
		json.dump(users,f)
	return True


async def get_bank_data():
	with open("mainbank.json", "r") as f:
		users = json.load(f)
	
	return users

def setup(client):
  client.add_cog(economy(client))