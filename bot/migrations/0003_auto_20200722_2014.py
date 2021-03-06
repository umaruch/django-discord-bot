# Generated by Django 3.0.8 on 2020-07-22 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_auto_20200722_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_id', models.CharField(max_length=32, verbose_name='Discord ID роли')),
                ('role_xp', models.PositiveIntegerField(verbose_name='Количество опыта для получения роли')),
            ],
            options={
                'verbose_name': 'Discord роль',
                'verbose_name_plural': 'Discord роли',
            },
        ),
        migrations.AlterField(
            model_name='discorduser',
            name='discord_id',
            field=models.CharField(max_length=32, verbose_name='ID пользователя Discord'),
        ),
        migrations.AlterField(
            model_name='discorduser',
            name='username',
            field=models.CharField(max_length=32, verbose_name='Имя пользователя Discord'),
        ),
        migrations.AlterField(
            model_name='server',
            name='online_id',
            field=models.CharField(max_length=32, null=True, verbose_name='Discord ID канала, в котором будет отображаться текущий онлайн'),
        ),
        migrations.AlterField(
            model_name='server',
            name='server_id',
            field=models.CharField(max_length=32, verbose_name='Discord ID Сервера'),
        ),
        migrations.AlterField(
            model_name='server',
            name='users_id',
            field=models.CharField(max_length=32, null=True, verbose_name='Discord ID канала, в котором будет отображаться количество пользователей'),
        ),
    ]
