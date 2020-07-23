# Generated by Django 3.0.8 on 2020-07-22 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_id', models.CharField(max_length=64, verbose_name='ID Сервера')),
                ('online_id', models.CharField(max_length=64, verbose_name='ID канала, в котором будет отображаться текущий онлайн')),
                ('users_id', models.CharField(max_length=64, verbose_name='ID канала, в котором будет отображаться количество пользователей')),
            ],
            options={
                'verbose_name': 'Сервер Discord',
                'verbose_name_plural': 'Сервера Discord',
            },
        ),
        migrations.AlterModelOptions(
            name='discorduser',
            options={'verbose_name': 'Пользователь Discord', 'verbose_name_plural': 'Пользователи Discord'},
        ),
        migrations.AddField(
            model_name='discorduser',
            name='messages',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество сообщений'),
        ),
        migrations.AlterField(
            model_name='discorduser',
            name='user_xp',
            field=models.PositiveIntegerField(default=0, verbose_name='Опыт пользователя'),
        ),
    ]