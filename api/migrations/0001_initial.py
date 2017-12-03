# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenreModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MovieModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('popularity_99', models.DecimalField(decimal_places=1, max_digits=4)),
                ('imdb_score', models.DecimalField(decimal_places=1, max_digits=4)),
                ('genre', models.ManyToManyField(to='api.GenreModel')),
            ],
        ),
    ]
