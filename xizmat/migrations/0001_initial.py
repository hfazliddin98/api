# Generated by Django 4.2.4 on 2023-08-18 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interaktiv_xizmatlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(blank=True, max_length=100)),
                ('link', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
