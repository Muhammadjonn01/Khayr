# Generated by Django 4.1 on 2024-01-05 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_post_getdonation_userchoice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='userchoice',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='userchoice',
        ),
        migrations.RemoveField(
            model_name='getdonation',
            name='userchoice',
        ),
        migrations.DeleteModel(
            name='UserChoice',
        ),
    ]