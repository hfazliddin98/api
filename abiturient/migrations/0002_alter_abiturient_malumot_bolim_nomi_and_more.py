# Generated by Django 4.2.4 on 2023-08-19 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abiturient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abiturient_malumot',
            name='bolim_nomi',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='abiturient_nomi',
            name='tur_nomi',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]