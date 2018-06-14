import discord
from discord.ext import commands
from discord.voice_client import VoiceClient

bot = commands.Bot("?")

@bot.event
async def on_ready():
    print("bot online")


@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("pong")


@bot.command(pass_context=True)
async def hello(ctx):
    await bot.say("hi :wave:")
    
    if __name__ == "__main__":
        for extension in startup_extensions:
            try:
                bot.load_extension(extension)
            except Exception as e:
                exc = "{}: {}".format(type(e).__name__, e)



bot.run("NDU2MDQ0NTUwMTM4NDk1MDA3.DgE4vQ.utuV-7gvVgs6W5bU4fhZRVwLpVw")
