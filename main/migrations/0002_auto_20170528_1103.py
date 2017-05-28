# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-28 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='powder',
            field=models.ManyToManyField(blank=True, to='main.Powder'),
        ),
        migrations.AlterField(
            model_name='coffee',
            name='syrup',
            field=models.ManyToManyField(blank=True, to='main.Syrup'),
        ),
    ]