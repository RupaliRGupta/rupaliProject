# Generated by Django 2.2 on 2020-02-11 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_adminmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='addr',
            field=models.CharField(default='NA', max_length=30),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='contact',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='name',
            field=models.CharField(default='NA', max_length=30),
        ),
    ]
