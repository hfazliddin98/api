# Generated by Django 4.2.4 on 2023-08-15 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fayl',
            name='anketa',
        ),
        migrations.RemoveField(
            model_name='fayl',
            name='ariza',
        ),
        migrations.RemoveField(
            model_name='fayl',
            name='diplom',
        ),
        migrations.RemoveField(
            model_name='fayl',
            name='kochirma',
        ),
        migrations.RemoveField(
            model_name='fayl',
            name='malumotnoma',
        ),
        migrations.RemoveField(
            model_name='fayl',
            name='pasport',
        ),
        migrations.RemoveField(
            model_name='fayl',
            name='royhat',
        ),
        migrations.RemoveField(
            model_name='fayl',
            name='yollanma',
        ),
    ]