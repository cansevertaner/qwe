# Generated by Django 2.0.9 on 2018-12-24 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oyunlar', '0004_auto_20181224_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
