import discord
from discord.ext import commands

TOKEN = 'MTE2MTc1MDczMDQwNzk0MDExNg.GxboTK.uR0gJonqjgzYyCd_8lflNLE4rGu-_B7VBXTnXk'

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1143351805431001098)  # ايدي_کانال را با ايدي کانال مورد نظر خود جايگزين کنيد

    # ايجاد يک ايمبد
    embed = discord.Embed(
        message=" Welcome {member.mention} 👋 ",
        AVATAR_URL="https://www.bing.com/images/blob?bcid=sv3TEwSKJj8GNZ7JLLHLFblnj0OA.....1k",
        Header="S T A R  C U L T",
        Thumbnail_image=set_image(url=member.avatar_url),
        title=f"Welcome to STAR CULT Server, {member.name}! 👋 ",
        description=f"Welcome {member.mention} to our server! 👋 ",
        Embed_image="https://cdns.klimg.com/resized/1200x600/p/headline/arti-welcome-beserta-dengan-penggunaan--690a6d.jpg",
        Footer_image="https://www.bing.com/images/blob?bcid=sv3TEwSKJj8GNZ7JLLHLFblnj0OA.....1k",
        Footer="S T A R  C U L T",
        color=#a006f8
      embed)
    
    # ارسال پيام با ايمبد
    await channel.send(embed=embed)

bot.run(TOKEN)
