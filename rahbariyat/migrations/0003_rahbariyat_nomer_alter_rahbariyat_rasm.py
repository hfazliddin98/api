# Generated by Django 4.2.4 on 2023-11-15 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rahbariyat', '0002_alter_rahbariyat_fish_alter_rahbariyat_lavozim_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rahbariyat',
            name='nomer',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='rahbariyat',
            name='rasm',
            field=models.FileField(blank=True, upload_to='rahbariyat/'),
        ),
    ]
