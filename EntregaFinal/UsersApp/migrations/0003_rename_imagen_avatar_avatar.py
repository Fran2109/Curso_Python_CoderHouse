# Generated by Django 4.1.7 on 2023-03-25 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UsersApp', '0002_alter_avatar_imagen_alter_avatar_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avatar',
            old_name='imagen',
            new_name='avatar',
        ),
    ]
