from django.contrib import admin

from .models import DiscordUser, Server, Role
# Register your models here.

@admin.register(DiscordUser)
class DiscordUserAdmin(admin.ModelAdmin):
    list_display = ['discord_id', 'username', 'user_xp', 'messages']
    list_display_links = ['discord_id', 'username']
    search_fields = ['discord_id', 'username']
    readonly_fields = ['messages', 'discord_id', 'username']

@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ['server_id']
    search_fields = ['server_id']
    list_display_links = ['server_id']

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['role_id', 'role_xp']
    search_fields = ['role_id']
    list_display_links = ['role_id']