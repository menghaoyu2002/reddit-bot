import os
from discord.ext import commands
from randompost import RandomPost
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
RANDOMPOST = RandomPost()
SUBREDDITS = ["memes", 
              "makemesuffer", 
              "cringe", 
              "tiktok", 
              "mademesmile", 
              "wholesome", 
              "anime",
              "pain"]

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(name="get")
async def get(ctx, subreddit="get"):
    response = RANDOMPOST.get_post(subreddit)
    print(f"preparing to send post from r/{subreddit}")
    await ctx.send(response)  


@bot.command(name="help")
async def help(ctx):
    response = "Try the following commands: \n !get \n !get " + "\n !get ".join(SUBREDDITS)
    await ctx.send(response) 


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        await ctx.send("Sorry that command is not valid")
        await help(ctx)


if __name__ == "__main__":
    bot.run(TOKEN)