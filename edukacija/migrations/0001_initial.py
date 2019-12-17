# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-07 16:45
from __future__ import unicode_literals

from django.db import migrations, models
import edukacija.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edukacija',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=edukacija.models.upload_image_path)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('link', models.URLField(blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]