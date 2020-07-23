from django.db import models

# Create your models here.
class DiscordUser(models.Model):
    discord_id = models.CharField(
        'ID пользователя Discord',
        max_length = 32,
        null = False
    )
    username = models.CharField(
        'Имя пользователя Discord',
        max_length = 32,
        null = False
    )
    user_xp = models.PositiveIntegerField(
        'Опыт пользователя',
        default = 0
    )
    messages = models.PositiveIntegerField(
        'Количество сообщений',
        default = 0
    )

    class Meta:
        verbose_name = 'Пользователь Discord'
        verbose_name_plural = 'Пользователи Discord'

class Server(models.Model):
    server_id = models.CharField(
        'Discord ID Сервера',
        max_length = 32,
    )
    online_id = models.CharField(
        'Discord ID канала, в котором будет отображаться текущий онлайн',
        max_length = 32,
        null = True
    )
    users_id = models.CharField(
        'Discord ID канала, в котором будет отображаться количество пользователей',
        max_length = 32,
        null = True
    )

    class Meta:
        verbose_name = 'Сервер Discord'
        verbose_name_plural = 'Сервера Discord'

class Role(models.Model):
    role_id = models.CharField(
        "Discord ID роли",
        max_length = 32,
        null = False
    )
    role_xp = models.PositiveIntegerField(
        "Количество опыта для получения роли",
        null = False
    )

    class Meta:
        verbose_name = "Discord роль"
        verbose_name_plural = "Discord роли"