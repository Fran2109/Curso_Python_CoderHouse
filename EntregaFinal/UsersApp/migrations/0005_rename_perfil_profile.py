# Generated by Django 4.1.7 on 2023-03-25 23:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UsersApp', '0004_rename_avatar_perfil'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Perfil',
            new_name='Profile',
        ),
    ]