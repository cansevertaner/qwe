# Generated by Django 2.0.9 on 2018-12-25 01:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oyunlar', '0022_auto_20181225_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 25, 4, 56, 1, 234348)),
        ),
    ]
