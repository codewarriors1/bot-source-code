import discord
from discord.ext import commands

class gen(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print("General.py loaded")
	
	@commands.command()
	async def delmulti(self, ctx):
		print("testing")

	@commands.command()
	async def ping(self, ctx):
		await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

	@commands.command()
	async def invite(self, ctx):
		await ctx.send("[hello](discord.gg/test)")

def setup(client):
	client.add_cog(gen(client))