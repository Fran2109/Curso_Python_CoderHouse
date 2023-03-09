# Generated by Django 4.1.7 on 2023-03-09 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InflablesApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cant_personas', models.PositiveIntegerField()),
                ('ancho', models.FloatField()),
                ('largo', models.FloatField()),
            ],
        ),
    ]
