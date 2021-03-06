# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-28 10:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bean',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('espresso_shots', models.PositiveIntegerField(default=1)),
                ('water', models.FloatField(default=0)),
                ('steamed_milk', models.BooleanField(default=False)),
                ('micro_foam', models.FloatField(blank=True, null=True)),
                ('extra_instructions', models.TextField(blank=True, null=True)),
                ('bean', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Bean')),
            ],
        ),
        migrations.CreateModel(
            name='Powder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Roast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Syrup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='coffee',
            name='powder',
            field=models.ManyToManyField(blank=True, null=True, to='main.Powder'),
        ),
        migrations.AddField(
            model_name='coffee',
            name='roast',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Roast'),
        ),
        migrations.AddField(
            model_name='coffee',
            name='syrup',
            field=models.ManyToManyField(blank=True, null=True, to='main.Syrup'),
        ),
    ]
