import requests
import discord
from discord.ext import commands
 
 
bot = commands.Bot(command_prefix='!')
 
@bot.command()
async def bypass(ctx, arg):
  r=requests.get('https://bypass.bot.nu/bypass2?url='+arg)
  a = ('%'+r.text)
  chunks = a.split(',')
  dest = chunks[1]
  stripped = dest.split('"')
  #await ctx.send(chunks[1])
  embed = discord.Embed()
  embed.set_thumbnail(url="https://thumbs.gfycat.com/PlainHonestAzurevase-size_restricted.gif")
  embed.add_field(name="Bypassed Link:", value=stripped[3], inline=False)
  await ctx.send(embed=embed)
 
 
bot.run('TOKEN')
