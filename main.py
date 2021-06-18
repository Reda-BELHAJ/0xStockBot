import discord
from discord.ext import commands
import os
import random
import utility
from keep_alive import keep_alive

client     = commands.Bot(command_prefix='$')

@client.command()
async def Invite(ctx):
    embed = discord.Embed(color=discord.Color.from_rgb(3, 252, 144))
    embed.description = "The Invite URL for Me! is : [Click Here](" + utility.Invite_URL+")" 
    await ctx.send(embed=embed)

@client.command()
async def Ping(ctx):
    embed = discord.Embed(color=discord.Color.from_rgb(3, 252, 144))
    embed.description = f':hourglass: {round(client.latency * 1000)}ms'
    await ctx.send(embed=embed)

@client.command()
async def Price(ctx, arg):
  if arg is not None:
    price = utility.getPrice(arg)
    if price != '0':
      embed = discord.Embed(color=discord.Color.from_rgb(20,52,116))

      embed.title = arg
      embed.add_field(name="Price", value=str(price)[0:10], inline=True)
      embed.set_footer(text="Information requested by: " + ctx.message.author.name)

      await ctx.send(embed=embed)
    else:
      embed = discord.Embed(color=discord.Color.from_rgb(255,0,0))
      embed.title = "Ticker Not Found"
      embed.add_field(name="Price Command Usage", value="$Price [Ticker]", inline=True)
      embed.add_field(name="Ticker Validation", value="Make sure that the ticker is verifed and in uppercase.", inline=True)
      embed.set_footer(text="Information requested by: " + ctx.message.author.name)
      await ctx.send(embed=embed)
  else:
    embed = discord.Embed(color=discord.Color.from_rgb(255,0,0))
    embed.title = "Command Not Found"
    embed.add_field(name="Price Command Usage", value="$Price [Ticker]", inline=True)
    embed.set_footer(text="Information requested by: " + ctx.message.author.name)

    await ctx.send(embed=embed)

@client.command()
async def Detail(ctx, arg):
  if arg is not None:
    Logo, URL, Description, Name, Industry, Symbol = utility.getDetails(arg)

    if Description != '':

      embed = discord.Embed(color=discord.Color.from_rgb(20,52,116))
      embed.title = Name
      embed.description = Description + " [Click Here](" + URL + ")."
      embed.set_thumbnail(url=Logo)

      embed.add_field(name="Industry", value=Industry, inline=True)
      embed.add_field(name="Symbol", value=Symbol, inline=True)

      embed.set_footer(text="Information requested by: " + ctx.message.author.name)

      await ctx.send(embed=embed)
    
    else:
      embed = discord.Embed(color=discord.Color.from_rgb(255,0,0))
      embed.title = "Ticker Not Found"
      embed.add_field(name="Detail Command Usage", value="$Detail [Ticker]", inline=True)
      embed.add_field(name="Ticker Validation", value="Make sure that the ticker is verifed and in uppercase.", inline=True)
      embed.set_footer(text="Information requested by: " + ctx.message.author.name)

      await ctx.send(embed=embed)
  else:
    embed = discord.Embed(color=discord.Color.from_rgb(255,0,0))
    embed.title = "Command Not Found"
    embed.add_field(name="Detail Command Usage", value="$Detail [Ticker]", inline=True)
    embed.set_footer(text="Information requested by: " + ctx.message.author.name)

    await ctx.send(embed=embed)

@client.command()
async def Help(ctx):
    embed = discord.Embed(color=discord.Color.from_rgb(20,52,116))
    embed.title = "Help"
    embed.description = "Here are the commands that you can use:"
    embed.set_thumbnail(url=client.user.avatar_url)

    embed.add_field(name="$Ping", value="This command returns the news of the ticker specified.", inline=True)
    embed.add_field(name="$News [Ticker]", value="This command returns the news of the ticker specified.", inline=True)
    embed.add_field(name="$Help", value="This command returns this message.", inline=True)
    embed.add_field(name="$Invite", value="This command sends you the invite link for the bot.", inline=True)
    embed.add_field(name="$Price [Ticker]", value="This command returns the current price of the ticker specified.", inline=True)
    embed.add_field(name="$Detail [Ticker]", value="This command returns the details of the ticker specified.", inline=True)

    embed.set_footer(text="Information requested by: " + ctx.message.author.name)

    await ctx.send(embed=embed)


@client.command()
async def News(ctx, arg):
    if arg is not None:
      description, url, title, image = utility.getNews(arg)

      if len(description) != 0:
        randomNumber = random.randint(0, int(len(description) - 1))
        
        news = description[randomNumber] + " [Click Here](" + url[randomNumber] + ")."

        embed = discord.Embed(color=discord.Color.from_rgb(20,52,116))
        embed.title = title[randomNumber]
        embed.description = news
        embed.set_image(url=image[randomNumber])
        embed.set_footer(text="Information requested by: " + ctx.message.author.name)

        await ctx.send(embed=embed)

      else:
          embed = discord.Embed(color=discord.Color.from_rgb(255,0,0))
          embed.title = "Ticker Not Found"
          embed.add_field(name="News Command Usage", value="$News [Ticker]", inline=True)
          embed.add_field(name="Ticker Validation", value="Make sure that the ticker is verifed and in uppercase.", inline=True)
          embed.set_footer(text="Information requested by: " + ctx.message.author.name)

          await ctx.send(embed=embed)

    else:
        embed = discord.Embed(color=discord.Color.from_rgb(255,0,0))
        embed.title = "Command Not Found"
        embed.add_field(name="News Command Usage", value="$News [Ticker]", inline=True)
        embed.set_footer(text="Information requested by: " + ctx.message.author.name)

        await ctx.send(embed=embed)

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

keep_alive()
client.run(os.getenv('TOKEN'))
