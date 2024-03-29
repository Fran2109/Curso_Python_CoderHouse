# Generated by Django 4.1.7 on 2023-03-26 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UsersApp', '0006_profile_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('subtitulo', models.CharField(max_length=255)),
                ('contenido', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('fondo', models.ImageField(blank=True, null=True, upload_to='fondo/')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UsersApp.profile')),
            ],
        ),
    ]
