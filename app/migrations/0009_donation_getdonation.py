# Generated by Django 5.0 on 2024-01-05 14:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_donation_description_donation_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='getdonation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.getdonation'),
            preserve_default=False,
        ),
    ]
