# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-11 22:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('site_ended', models.CharField(choices=[('T', 'Terrorists'), ('CT', 'Counter-Terrorists')], max_length=255)),
                ('rounds_for', models.IntegerField()),
                ('rounds_against', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GamePlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kills', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('deaths', models.IntegerField()),
                ('mvps', models.IntegerField()),
                ('points', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('rank', models.CharField(blank=True, choices=[(1, 'Silver I'), (2, 'Silver II'), (3, 'Silver III'), (4, 'Silver IV'), (5, 'Silver Elite'), (6, 'Silver Elite Master'), (7, 'Gold Nova I'), (8, 'Gold Nova II'), (9, 'Gold Nova III'), (10, 'Gold Nova Master'), (11, 'Master Guardian I'), (12, 'Master Guardian II'), (13, 'Master Guardian Elite'), (14, 'Distinguished Master Guardian'), (15, 'Legendary Eagle'), (16, 'Legendary Eagle Master'), (17, 'Supreme Master First Class'), (18, 'The Global Elite')], max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='gameplayer',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='game_map',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.Map'),
        ),
        migrations.AddField(
            model_name='game',
            name='players',
            field=models.ManyToManyField(through='stats.GamePlayer', to='stats.Player'),
        ),
    ]
