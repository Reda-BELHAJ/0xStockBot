import discord
import os
import random
import utility
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Invite'):
        embed = discord.Embed(color=discord.Color.from_rgb(3, 252, 144))
        embed.description = "The Invite URL for Me! is : [Click Here](" + utility.Invite_URL +")" 
        await message.channel.send(embed=embed)

    if message.content.startswith('$Ping'):
        embed = discord.Embed(color=discord.Color.from_rgb(3, 252, 144))
        embed.description = f':hourglass: {round(client.latency * 1000)}ms'
        await message.channel.send(embed=embed)


    if message.content.startswith('$Detail'):
      if len(message.content.split()) > 1 and len(message.content.split()) < 3:
        Logo, URL, Description, Name, Industry, Symbol = utility.getDetails(message.content.split()[1])

        if Description != '':

          embed = discord.Embed(color=discord.Color.from_rgb(20,52,116))
          embed.title = Name
          embed.description = Description + " [Click Here](" + URL + ")."
          embed.set_thumbnail(url=Logo)

          embed.add_field(name="Industry", value=Industry, inline=True)
          embed.add_field(name="Symbol", value=Symbol, inline=True)

          embed.set_footer(text="Information requested by: " + message.author.display_name)

          await message.channel.send(embed=embed)
        
        else:
          embed = discord.Embed(color=discord.Color.from_rgb(255,0,0))
          embed.title = "Ticker Not Found"
          embed.add_field(name="Detail Command Usage", value="$Detail [Ticker]", inline=True)
          embed.add_field(name="Ticker Validation", value="Make sure that the ticker is verifed and in uppercase.", inline=True)
          embed.set_footer(text="Information requested by: " + message.author.display_name)

          await message.channel.send(embed=embed)

      else:
          embed = discord.Embed(color=discord.Color.from_rgb(255,0,0))
          embed.title = "Command Not Found"
          embed.add_field(name="Detail Command Usage", value="$Detail [Ticker]", inline=True)
          embed.set_footer(text="Information requested by: " + message.author.display_name)

          await message.channel.send(embed=embed)

    if message.content.startswith('$Help'):
        embed = discord.Embed(color=discord.Color.from_rgb(20,52,116))
        embed.title = "Help"
        embed.description = "Here are the commands that you can use:"
        embed.set_thumbnail(url=client.user.avatar_url)

        embed.add_field(name="$Ping", value="This command returns the news of the ticker specified.", inline=True)
        embed.add_field(name="$News [Ticker]", value="This command returns the news of the ticker specified.", inline=True)
        embed.add_field(name="$Help", value="This command returns this message.", inline=True)
        embed.add_field(name="$Invite", value="This command sends you the invite link for the bot.", inline=True)
        embed.add_field(name="$Chart [Ticker]", value="This command returns a chart of the ticker specified.", inline=True)
        embed.add_field(name="$Detail [Ticker]", value="This command returns the details of the ticker specified.", inline=True)

        embed.set_footer(text="Information requested by: " + message.author.display_name)

        await message.channel.send(embed=embed)

    if message.content.startswith('$News'):
        if len(message.content.split()) > 1 and len(message.content.split()) < 3:

          description, url, title, image = utility.getNews(message.content.split()[1])

          if len(description) != 0:
            randomNumber = random.randint(0, int(len(description) - 1))
            
            news = description[randomNumber] + " [Click Here](" + url[randomNumber] + ")."

            embed = discord.Embed(color=discord.Color.from_rgb(20,52,116))
            embed.title = title[randomNumber]
            embed.description = news
            embed.set_image(url=image[randomNumber])
            embed.set_footer(text="Information requested by: " + message.author.display_name)

            await message.channel.send(embed=embed)

          else:
              embed = discord.Embed(color=discord.Color.from_rgb(255,0,0))
              embed.title = "Ticker Not Found"
              embed.add_field(name="News Command Usage", value="$News [Ticker]", inline=True)
              embed.add_field(name="Ticker Validation", value="Make sure that the ticker is verifed and in uppercase.", inline=True)
              embed.set_footer(text="Information requested by: " + message.author.display_name)

              await message.channel.send(embed=embed)

        else:
            embed = discord.Embed(color=discord.Color.from_rgb(255,0,0))
            embed.title = "Command Not Found"
            embed.add_field(name="News Command Usage", value="$News [Ticker]", inline=True)
            embed.set_footer(text="Information requested by: " + message.author.display_name)

            await message.channel.send(embed=embed)

keep_alive()
client.run(os.getenv('TOKEN'))