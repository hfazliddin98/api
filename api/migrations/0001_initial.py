# Generated by Django 4.2.4 on 2023-08-17 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fayl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=100)),
                ('familya', models.CharField(max_length=100)),
                ('fan', models.CharField(max_length=100)),
                ('sana', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
