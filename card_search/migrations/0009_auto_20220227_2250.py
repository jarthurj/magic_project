# Generated by Django 2.2 on 2022-02-27 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card_search', '0008_auto_20211127_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='legal',
            name='card',
        ),
        migrations.RemoveField(
            model_name='legal',
            name='name',
        ),
        migrations.RemoveField(
            model_name='legalities',
            name='cards',
        ),
        migrations.RemoveField(
            model_name='card',
            name='digital',
        ),
        migrations.RemoveField(
            model_name='card',
            name='layout',
        ),
        migrations.DeleteModel(
            name='Digital',
        ),
        migrations.DeleteModel(
            name='Legal',
        ),
        migrations.DeleteModel(
            name='Legalities',
        ),
    ]