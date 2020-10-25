from discord.ext import commands
import random
import csv
import time

with open('cogs/familyfeud.csv', 'r') as csv_file:
   csv_reader = csv.reader(csv_file, delimiter=',')
   line_count = 0
   mark = 0
   percentage = 0

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
	  line_count = 0
	  rownum = random.range(1,len(csv_reader))
	  for row in csv_reader:
		  if line_count == 0:
			  await ctx.send(f'The quiz will be set up as ' + ''.join(row))
			  line_count +=1
		  elif line_count != rownum:
			  line_count += 1
			  continue
		  else:
			  await ctx.send(f' The question is "{row[0]}" \n Is the answer  \n a) {row[1]}, \n b) {row[2]} \n c) {row[3]} \n d) {row[4]}.\n')
			  line_count += 1
			  answer = input("Please enter a letter \n")
			  if(answer.upper() == str(f'{row[5]}').upper()):
				  await ctx.send("Correct answer\n")
				  time.sleep(1)
			  else:
				  await ctx.send(f"Wrong answer.The correct answer is {row[5]} \n")
				  
			
	  
def setup(client):
  client.add_cog(trivia(client))
