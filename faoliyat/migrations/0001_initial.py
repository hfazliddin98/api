# Generated by Django 4.2.16 on 2024-09-11 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Akademik_litsey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(blank=True, max_length=100)),
                ('malumot', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ilmiy_faoliyat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(blank=True, max_length=100)),
                ('malumot', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jamoatchlik_kengashi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(blank=True, max_length=100)),
                ('malumot', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Madaniyat_marifat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(blank=True, max_length=100)),
                ('malumot', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Oquv_uslubiy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(blank=True, max_length=100)),
                ('malumot', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Yoshlar_bilan_ishlash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(blank=True, max_length=100)),
                ('malumot', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
