# Generated by Django 5.1.5 on 2025-01-30 05:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tyutor', '0005_topshiriq_fayl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fayl',
            name='topshiriq',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fayllar', to='tyutor.topshiriq'),
        ),
    ]
