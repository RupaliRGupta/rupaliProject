# Generated by Django 2.2 on 2020-01-21 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermodel',
            old_name='foodIdfk',
            new_name='emailIdfk',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='address',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='userIdfk',
        ),
    ]