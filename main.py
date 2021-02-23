import discord
from discord.ext import commands
import datetime

bot = commands.Bot(command_prefix='*')

@bot.command()
async def ping(ctx):
   await ctx.send('pong')

@bot.command()
async def suma(ctx, num1: int, num2: int):
   await ctx.send(num1 + num2)

@bot.command()
async def huevo(ctx):
   await ctx.send('comes')

@bot.command()
async def resta(ctx, num1: int, num2: int):
   await ctx.send(num1 - num2)

@bot.command()
async def info(ctx):
   embed = discord.Embed(title =f"{ctx.guild.name}", descripcion="esto es un servidor asadsaw", timestamp=datetime.datetime.utcnow())
   embed.add_field(name= "Server created at", value = f"{ctx.guild.created_at}")
   embed.add_field(name= "Server owner", value = f"{ctx.guild.owner}")
   embed.add_field(name= "Server region", value = f"{ctx.guild.region}")
   embed.add_field(name= "Server id", value = f"{ctx.guild.id}")
   

   await ctx.send(embed=embed)


@bot.command()
async def av(ctx, member: discord.Member):
   avatar = discord.Embed(
      color = discord.Color.green()
   )
   avatar.set_image(url="{}".format(member.avatar_url))

   await ctx.send(embed=avatar)


@bot.event
async def on_ready():
    print('el bot esta prendido')
    game = discord.Game("comer")
    await bot.change_presence(activity=game)



bot.run('insert token')
