# Generated by Django 4.1.7 on 2023-02-19 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Katalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=225)),
                ('discrpition', models.CharField(max_length=225)),
                ('img_url', models.TextField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Main_contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator', models.TextField(max_length=25)),
                ('menejer', models.TextField(max_length=25)),
                ('mebel_menejer', models.TextField(max_length=25)),
                ('guarantee', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=225)),
                ('discrpition', models.CharField(max_length=225)),
                ('video_url', models.TextField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Prodouct_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('img_url', models.TextField(max_length=225)),
                ('katalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dafna_app.katalog')),
            ],
        ),
        migrations.CreateModel(
            name='Prodouct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=225)),
                ('discrpition', models.CharField(max_length=225)),
                ('img_url', models.TextField(max_length=225)),
                ('price', models.IntegerField()),
                ('color', models.TextField(max_length=25)),
                ('manufacturer', models.TextField(max_length=25)),
                ('material', models.TextField(max_length=25)),
                ('prodouct_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dafna_app.prodouct_type')),
            ],
        ),
        migrations.CreateModel(
            name='Love',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodouct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dafna_app.prodouct')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branches_name', models.TextField(max_length=225)),
                ('address', models.TextField(max_length=225)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('menefer', models.TextField(max_length=225)),
                ('main_contacts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dafna_app.main_contacts')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodouct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dafna_app.prodouct')),
            ],
        ),
    ]
