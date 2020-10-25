import discord
from discord.ext import commands

class mod(commands.Cog):

	def __init__(self, client):
		self.client = client
  
	@commands.Cog.listener()
	async def on_ready(self):
		print("mod.py loaded.")

	@commands.command()
	@commands.has_permissions(manage_messages=True)
	async def mute(self,ctx,member : discord.Member):
		muted = ctx.guild.get_role(765460547129835540)
	
		await member.add_roles(muted)
		await ctx.send(member.mention + " has been muted")


	@commands.command()
	@commands.has_permissions(manage_messages=True)
	async def unmute(self,ctx,member : discord.Member):
		muted = ctx.guild.get_role(765460547129835540)

		await member.remove_roles(muted)
		await ctx.send(member.mention + " has been unmuted")

	@commands.command()
	async def support(self,ctx):
		await ctx.send("here is our support server!	https://discord.gg/YGJFXz")

	@commands.command()
	@commands.has_permissions(manage_messages=True)
	async def clear(self,ctx,amount=2,):
		await ctx.message.delete()
		await ctx.channel.purge(limit=int(amount))
		author = ctx.author
		channel = commands.get_channel(765676846410760222)
		await channel.send (f"{author}" "has cleared amount of messages")

	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def ban(self,ctx, member: discord.Member, *, reason="for being a prick"):
		await member.send("You have been banned:" + reason)
		await member.ban(reason=reason)
		channel = commands.get_channel(765676846410760222)
		await channel.send ("member has been banned")

	@commands.command()
	@commands.has_permissions(kick_members=True)
	async def kick(self,ctx, member: discord.Member, *,reason="for being a prick"):
		await member.send("You have been kicked:" + reason)
		await member.kick(reason=reason)

	@commands.command()
	async def about(self,ctx):
		embed = discord.Embed(
        title = "Moderation commands prefix is !",
        description = """•kick @user reason - kicks the mentioned user and dms them the reason
				•ban @user reason - bans the user and dms them the reason
				•clear amount - clears that amount of messages 
				•mute @user makes the mentioned user not able to send messages
				•unmute @user unmutes the user so he can speak again
""",
        colour = discord.Colour(int("0dfaab", 16))
    )
		icon = str(ctx.guild.icon_url)
		embed.set_footer(text="Created using the power of teamwork")
		embed.set_image(url=icon)
		embed.set_author(name='@wakandawarrior & @Lxcky')
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/765815821561233428/766596676894326864/image0.png")
		embed.add_field(name="About the owners", value="I have been created to try to aid you and spice up  the daily use of this server. I am able to assist and humor you in many ways, shown if you use the !commands command. I hope that I am of great use to you all", inline=False)

		await ctx.send(embed=embed)


	@commands.command()
	@commands.has_permissions(manage_messages=True)
	async def assignrole(self, ctx, member : discord.Member, rolename):
			role = discord.utils.get(member.guild.roles, name=rolename)
			await discord.Member.add_roles(member, role)

	@commands.command()
	async def server(self,ctx):
			name = str(ctx.guild.name)
			owner = "@wakandawarrior and @lxcky"
			id = str(ctx.guild.id)
			region = str(ctx.guild.region)
			memberCount = str(ctx.guild.member_count)

			icon = str(ctx.guild.icon_url)

			embed = discord.Embed(
          title=name + " Server Information",
          description="""
          This is the testing ground which we use to develop the 
          latest features in our Discord.py bot.
          """,
          color=discord.Color.blue()
      )
			embed.set_thumbnail(url=icon)
			embed.add_field(name="Owners", value=owner, inline=True)
			embed.add_field(name="Server ID", value=id, inline=True)
			embed.add_field(name="Region", value=region, inline=False)
			embed.add_field(name="Member Count", value=memberCount, inline=True)	

			await ctx.send(embed=embed)

	@commands.command()
	async def add_roles(self,ctx, rolename):
		member = ctx.message.author
		role = discord.utils.get(member.guild.roles, name=rolename)
		await discord.Member.add_roles(member, role)
  
	@commands.command()
	@commands.is_owner()
	async def shutdown(self,ctx):
		await ctx.bot.logout()

def setup(client):
	client.add_cog(mod(client))
