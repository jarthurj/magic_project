# Generated by Django 2.2 on 2021-11-12 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('card_search', '0002_auto_20210731_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legal',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='legalities', to='card_search.Legalities'),
        ),
    ]
