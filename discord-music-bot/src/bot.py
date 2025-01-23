from discord.ext import commands
import json
import os

# Load configuration
with open(os.path.join(os.path.dirname(__file__), '../config/config.json')) as config_file:
    config = json.load(config_file)

# Initialize bot
bot = commands.Bot(command_prefix=config['command_prefix'])

# Load cogs
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    bot.load_extension('cogs.music')

# Run the bot
bot.run(config['token'])