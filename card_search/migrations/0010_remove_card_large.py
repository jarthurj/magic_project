# Generated by Django 2.2 on 2022-05-30 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card_search', '0009_auto_20220227_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='large',
        ),
    ]
