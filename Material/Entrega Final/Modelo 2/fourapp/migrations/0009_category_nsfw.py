# Generated by Django 4.0.5 on 2022-07-28 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fourapp', '0008_remove_post_replycounter'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='nsfw',
            field=models.BooleanField(default=False),
        ),
    ]