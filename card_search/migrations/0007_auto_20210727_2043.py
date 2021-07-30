# Generated by Django 2.2 on 2021-07-28 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('card_search', '0006_auto_20210727_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cmc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmc', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Mana_cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mana_cost', models.CharField(max_length=45)),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='type_line',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='cmc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='card_search.Cmc'),
        ),
        migrations.AddField(
            model_name='card',
            name='mana_cost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='card_search.Mana_cost'),
        ),
    ]
