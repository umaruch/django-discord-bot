import discord
from discord.ext import commands
from discord.utils import get

from django.conf import settings

def create_bot(bot_token):
    try:
        bot = commands.Bot(command_prefix=settings.COMMAND_PREFIX)
        bot.remove_command('help')
        return bot
    except Exception as e:
        print(e)
        return None
