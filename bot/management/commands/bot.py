from django.core.management.base import BaseCommand
import discord
from discord.ext import commands
from discord.utils import get
from asgiref.sync import async_to_sync
import asyncio

from django.conf import settings
from bot.models import DiscordUser, Server

def change_user(discord_user):
    user, _ = DiscordUser.objects.get_or_create(
                    discord_id = discord_user.id,
                    defaults = {
                        'username': discord_user.name,
                    }
                )
    return user

def get_server():
        """Обращается в базу данных и возвращает данные сервера, который надо отслеживать"""
        server = Server.objects.all().first()
        if not server:
            return None
        return {
            'server_id': server.server_id,
            'online_id': server.online_id,
            'users_id': server.users_id
        }    

class Command(BaseCommand):
    """Реализаци команды создания бота"""
    help = "Start Discord Bot"
    server = get_server()

    
    def handle(self, *args, **options):
        bot = commands.Bot(command_prefix = settings.COMMAND_PREFIX)
        
        if not self.server:
            print("Please, add server data into DB")
            return
        
        async def check_users():
            while True:
                guild = bot.get_guild(int(self.server.get('server_id')))

                # Считаем пользователей в онлайне
                all_users = sum(member.status!=discord.Status.offline and \
                                not member.bot for member in guild.members)
                channel = bot.get_channel(int(self.server.get('online_id')))
                await discord.VoiceChannel.edit(channel, name=f"Онлайн: {all_users}")
                # Считаем общее количество пользователей на сервере
                all_users = sum(not member.bot for member in guild.members)
                channel = bot.get_channel(int(self.server.get('users_id')))
                await discord.VoiceChannel.edit(channel, name=f"Пользователей: {all_users}")
                
                await asyncio.sleep(120)

        @bot.event
        async def on_ready():
            print('Connect to Discord')
            bot.loop.create_task(check_users())   

        @bot.event
        async def on_message(message):
            if str(message.guild.id) == self.server.get('server_id'):
                if message.content.startswith(settings.COMMAND_PREFIX):
                    await bot.process_commands(message)
                else:
                    if message.author == bot.user:
                        return

                    user = change_user(message.author)
                    user.user_xp +=3
                    user.messages +=1
                    if message.author.name != user.username:
                        user.username = message.author.name
                    user.save()


        @bot.command(pass_context = True)
        async def info(ctx):
            user = change_user(ctx.author)
            embed=discord.Embed(title="Статистика пользователя", color=0x030303)
            embed.set_author(name=ctx.author.name)
            embed.add_field(name="Опыт", value=user.user_xp, inline=True)
            embed.add_field(name="Количество сообщений", value=user.messages, inline=True)
            embed.set_footer(text="А теперь уебывай на хуй")
            await ctx.send(embed=embed)

        bot.run(settings.DISCORD_BOT_TOKEN)

