# Generated by Django 4.1 on 2024-01-05 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_comment_userchoice_remove_donation_userchoice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='description',
            field=models.TextField(default=321),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donation',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]