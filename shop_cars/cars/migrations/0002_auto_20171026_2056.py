# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-26 20:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cars.Image'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='description',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='color',
            name='code_color',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
