# Generated by Django 4.1.7 on 2023-02-18 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dafna_app', '0003_rename_score_love_prodouct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='name',
        ),
    ]
