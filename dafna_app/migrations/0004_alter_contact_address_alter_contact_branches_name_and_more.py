# Generated by Django 4.1.7 on 2023-02-20 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dafna_app', '0003_alter_main_contacts_mebel_menejer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(max_length=252),
        ),
        migrations.AlterField(
            model_name='contact',
            name='branches_name',
            field=models.CharField(max_length=252),
        ),
        migrations.AlterField(
            model_name='contact',
            name='menefer',
            field=models.CharField(max_length=252),
        ),
        migrations.AlterField(
            model_name='main_contacts',
            name='mebel_menejer',
            field=models.CharField(max_length=252),
        ),
        migrations.AlterField(
            model_name='main_contacts',
            name='menejer',
            field=models.CharField(max_length=252),
        ),
        migrations.AlterField(
            model_name='main_contacts',
            name='operator',
            field=models.CharField(max_length=252),
        ),
    ]