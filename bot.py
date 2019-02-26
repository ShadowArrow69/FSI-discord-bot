import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import config

bot = commands.Bot(command_prefix='-')
MyID = "253417332406222848" 
chat_filter = ["NIGGA", "HENRY", "FUCK"]
bypass_list = ["253417332406222848"]
   
@bot.event
async def on_ready():
    print("bot online")
      
@bot.command()
async def add(left : int, right : int): 
    await bot.say(left + right)
      
@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)
     
@bot.command(pass_context=True)
async def cat(ctx):
    await bot.say("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")
   
@bot.command(pass_context=True)
async def dog(ctx):
    await bot.say("https://giphy.com/gifs/cheezburger-JfDNFU1qOZna")
      
@bot.command()
async def echo(*, message: str):
    await bot.say(message)   
    
@bot.event
async def on_message(message):
    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await bot.delete_message(message)
                    await bot.send_message(message.channel, "**Hey!** Don't use that fucking word!!!")
                except discord.errors.NotFound:
                    return
                
    await bot.process_commands(message)

    if message.content == "ur shit":
        await bot.send_message(message.channel, ":poop:")
    if message.content == "fuck you":
        await bot.send_message(message.channel, ":middle_finger:")
    if message.content == "ur gay":
        await bot.send_message(message.channel, ":joy:")
    if message.content == "i luv u":
        await bot.send_message(message.channel, ":kissing_heart:")
    if message.content == "hmmm":
        await bot.send_message(message.channel, ":thinking:")
    if message.content == "george":
        await bot.send_message(message.channel, ":couple_mm:")
    if message.content == "kelvin":
        await bot.send_message(message.channel, ":hear_no_evil:")
    if message.content == "nicolas":
        await bot.send_message(message.channel, ":cake:")
    if message.content == "william":
        await bot.send_message(message.channel, ":baby::skin-tone-5:")
     if message.content == "benji":
        await bot.send_message(message.channel, ":girl::skin-tone-5:")    
    if message.content == "yummy":
        await bot.send_message(message.channel, ":hamburger: :fries: :taco: :ramen: :stew: :bento: :ice_cream: :chocolate_bar: :cookie:")
    if message.content == "allahu akbar":
        await bot.send_message(message.channel, ":bomb:")
    if message.content == "shadowarrow":
        await bot.send_message(message.channel, ":six: :nine:")
    if message.content == "which country am i from?":
        await bot.send_message(message.channel, ":flag_ng:")
    if message.content == "urmumgaylol":
        await bot.send_message(message.channel, ":regional_indicator_n: :regional_indicator_o:       :regional_indicator_u: ")
    if message.content == "come":
        await bot.send_message(message.channel, ":eggplant: :sweat_drops: :tongue:")
    if message.content.startswith('fact'):
        userID = message.author.id
        await bot.send_message(message.channel, "<@%s> Henry's the best!" % (userID))
    if message.content.startswith('say'):
        args = message.content.split(" ")
        await bot.send_message(message.channel, "%s" % (" ".join(args[1:])))
    if message.content.startswith('status') and message.author.id == MyID:
        game = message.content[6:]
        await bot.change_presence(game=discord.Game(name=game))
        await bot.send_message(message.channel, "Status has been changed to 'playing" + game + "'")

bot.run(config.token)
