# Generated by Django 2.0.9 on 2018-12-24 23:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oyunlar', '0017_auto_20181225_0227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='game_file',
        ),
        migrations.AlterField(
            model_name='comments',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 25, 2, 31, 57, 317572)),
        ),
    ]
